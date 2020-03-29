from sys import getsizeof, exit
from argparse import ArgumentParser
import sqlite3
from functools import wraps
from time import time
from typing import Iterable, Any, Tuple


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("\nWywołano {} z argumentami:".format(f.__name__), end=' ')
        for arg in args:
            print(arg, end=' ')
        for key, value in kwargs.items():
            print("{}={}".format(key, value), end=' ')
        print()
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Wykonano w czasie: {}'.format(end - start))
        return result

    return wrapper


# Funkcja do wykrywania ostatniej iteracji
def signal_last(it: Iterable[Any]) -> Iterable[Tuple[bool, Any]]:
    iterable = iter(it)
    ret_var = next(iterable)
    for val in iterable:
        yield False, ret_var
        ret_var = val
    yield True, ret_var


query_create_table_tracks = """
    CREATE TABLE IF NOT EXISTS tracks(
    id CHAR(18) PRIMARY KEY,
    track_id CHAR(18),
    artist_name VARCHAR(256),
    track_title VARCHAR(256));
"""

query_create_table_stats = """
    CREATE TABLE IF NOT EXISTS stats(
    user_id CHAR(40),
    track_id CHAR(18),
    time VARCHAR(10));
"""

query_create_view_top5_tracks = """
    CREATE VIEW top5_tracks AS
        SELECT track_title, plays
        FROM 
            (SELECT track_id as 'track', COUNT() as plays 
            FROM stats 
            GROUP BY track_id
            ORDER BY 2 DESC
            LIMIT 5) 
        INNER JOIN tracks ON tracks.track_id=track;
"""

query_create_view_top_artist = """
    CREATE VIEW top_artist AS 
        SELECT artist_name, SUM(plays) as plays
        FROM 
            (SELECT track_id as 'track', COUNT() as plays 
            FROM stats 
            GROUP BY track_id 
            ORDER BY 2 DESC) 
        INNER JOIN tracks ON tracks.track_id=track
        GROUP BY artist_name 
        ORDER BY 2 DESC
        LIMIT 1;
"""


@timeit
def import_file_values(conn, file_name, table_name):
    query_template = None
    data = []
    try:
        tf = open(file_name, encoding='ISO-8859-2')
        with tf:
            for is_last, line in signal_last(tf):
                if query_template is None:
                    # Tworzenie zapytania z odpowiednia iloscia argumentow
                    query_template = 'INSERT INTO ' + str(table_name) + \
                                     ' VALUES(' + '?' + ',?' * (len(line.split('<SEP>')) - 1) + ')'

                data.append(tuple(line.strip().split('<SEP>')))

                if conn is not None and (getsizeof(data) > 200000 or is_last):
                    with conn:
                        conn.executemany(query_template, data)
                        data = []
    except FileNotFoundError as Ex:
        # Nazwy tabel są hardcodowane, więc można użyć format
        conn.execute("DROP TABLE IF EXISTS {}".format(table_name))
        exit('Nie znaleziono pliku {}'.format(Ex.filename))
    except sqlite3.IntegrityError as Ex:
        exit("{}\nZalecane usunięcie bazy danych i stworzenie nowej".format(Ex))


@timeit
def execute_query(conn, query):
    return conn.execute(query)


def main():
    parser = ArgumentParser("Zadanie ETL")
    parser.add_argument('-p', '--path', dest='path', type=str, required=True)
    parser.add_argument('-t', '--tracks', dest='tracks', type=str, required=False, default='./unique_tracks.txt')
    parser.add_argument('-s', '--stats', dest='stats', type=str, required=False, default='./triplets_sample_20p.txt')

    args = parser.parse_args()
    print('Zadanie ETL\n\n'
          'Oczekiwane ścieżki plików:')
    for key, value in vars(args).items():
        print('--{} = {}'.format(key, value))

    db_connector = sqlite3.connect(args.path)

    with db_connector:
        cursor = db_connector.cursor()
        cursor.execute("SELECT COUNT() FROM sqlite_master WHERE type='table' AND name IN ('tracks','stats')")

        # Nazwy tabel muszą mieć unikalne nazwy, dlatego to sprawdzenie jest wiarygodne
        if cursor.fetchone()[0] == 2:
            print('\nBaza posiada wymagane tabele')
        else:
            print('\nTworzenie bazy danych')
            db_connector.execute(query_create_table_tracks)
            db_connector.execute(query_create_table_stats)

            print('Importowanie danych')
            import_file_values(db_connector, args.tracks, 'tracks')
            import_file_values(db_connector, args.stats, 'stats')

            # Widoki są tworzone dopiero po pomyślnym importowaniu danych
            print('Tworzenie widoków')
            db_connector.execute(query_create_view_top5_tracks)
            db_connector.execute(query_create_view_top_artist)

        # Zabezpieczenie przed niezaimportowanymi danymi
        cursor.execute("SELECT COUNT() FROM sqlite_master WHERE type='view' AND name IN ('top5_tracks','top_artist')")
        if cursor.fetchone()[0] == 2:
            print('\nWidoki dostępne (Dane prawdopodobnie zaimportowane)')
            # SQL View ogranicza widok do jednej krotki, stąd użycie fetchone
            top_artist = execute_query(db_connector, "SELECT artist_name, plays FROM top_artist").fetchone()
            print("\nArtysta z największą liczbą odsłuchań: {} ({})".format(top_artist[0], top_artist[1]))

            # Można zastosować takie obejście, ponieważ jawnie oczekujemy 2 kolumn
            for top, (track, plays) in enumerate(
                    execute_query(db_connector, "SELECT track_title, plays FROM top5_tracks")):
                if top == 0:
                    print("\nTop 5 utworów:")
                print("{} {} ({})".format(top + 1, track, plays))
        else:
            print('Błąd! Brak widoków (Możliwe niezaimportowane dane)')


if __name__ == '__main__':
    main()
