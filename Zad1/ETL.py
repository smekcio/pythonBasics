from sys import getsizeof
from argparse import ArgumentParser
import sqlite3
from functools import wraps
from time import time
from typing import Iterable, Any, Tuple


def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print("Wywołano {} z argumentami:".format(f.__name__), end=' ')
        for arg in args:
            print(arg, end=' ')
        for key, value in kwargs.items():
            print("{}={}".format(key, value), end=' ')
        print('w czasie: {}'.format(end - start))
        return result

    return wrapper


def signal_last(it: Iterable[Any]) -> Iterable[Tuple[bool, Any]]:
    iterable = iter(it)
    ret_var = next(iterable)
    for val in iterable:
        yield False, ret_var
        ret_var = val
    yield True, ret_var


query_create_table_tracks = """
    CREATE TABLE IF NOT EXISTS tracks(
    track_id CHAR(18) PRIMARY KEY,
    artist_id CHAR(18),
    artist_name VARCHAR(256),
    track_title VARCHAR(256))
"""

query_create_table_stats = """
    CREATE TABLE IF NOT EXISTS stats(
    user_id CHAR(40),
    track_id CHAR(18),
    time CHAR(10))
"""

db_connector = None


@timeit
def insert_file_values(file_name, table_name):
    query_template = None
    data = []
    try:
        with open(file_name, encoding='ISO-8859-2') as tf:
            for is_last, line in signal_last(tf):
                if query_template is None:
                    # Tworzenie zapytania z odpowiednia iloscia argumentow
                    query_template = 'INSERT INTO ' + str(table_name) + \
                                     ' VALUES(' + '?' + ',?' * (len(line.split('<SEP>')) - 1) + ')'

                data.append(tuple(line.strip().split('<SEP>')))

                if db_connector is not None and (getsizeof(data) > 200000 or is_last):
                    with db_connector:
                        db_connector.executemany(query_template, data)
                        data = []
    except FileNotFoundError as Ex:
        print(Ex)
    except sqlite3.IntegrityError as Ex:
        print(Ex)


def main():
    parser = ArgumentParser("Zadanie ETL")
    parser.add_argument('-p', '--path', dest='path', type=str, required=True)
    parser.add_argument('-t', '--tracks', dest='tracks', type=str, required=False, default='./unique_tracks.txt')
    parser.add_argument('-s', '--stats', dest='stats', type=str, required=False, default='./triplets_sample_20p.txt')

    args = parser.parse_args()
    print(args)

    global db_connector
    db_connector = sqlite3.connect(args.path)

    with db_connector:
        db_connector.execute(query_create_table_tracks)
        db_connector.execute(query_create_table_stats)

        insert_file_values(args.tracks, 'tracks')
        insert_file_values(args.stats, 'stats')
        # db_cursor = db_connector.cursor()


if __name__ == '__main__':
    main()
