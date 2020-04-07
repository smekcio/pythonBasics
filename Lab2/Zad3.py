from Lab2.gradebook import GradeBook, Student
import logging


def main():
    debug = False
    logging.getLogger().setLevel(20 if debug else 30)

    student = Student('1', 'Jan Kowalski')
    gradebook = GradeBook('Programowanie laboratorium')

    gradebook.add_student(student)
    gradebook.add_student('Andrzej Morawiecki')
    gradebook.add_student('Mateusz Duda')

    print('Lista studentów:')
    for s in gradebook.student_list:
        print(s)

    gradebook.grade_student(1, 5, 1)
    gradebook.grade_student(1, 4, 2)
    gradebook.grade_student(1, 3, 3)
    gradebook.grade_student(2, 3, 1)
    gradebook.grade_student(2, 3, 1)
    gradebook.grade_student(2, 5, 5)
    gradebook.grade_student(3, 2, 5)
    gradebook.grade_student(3, 4, 2)
    gradebook.grade_student(3, 3, 2)

    gradebook.list_grades(student)
    gradebook.list_grades('Andrzej Morawiecki')
    gradebook.list_grades(3)

    gradebook.get_report()

    przepis = gradebook.based_gradebook('Programowanie wykład', gradebook)
    przepis.grade_student(1, 5, 1)
    przepis.grade_student(2, 5, 1)
    przepis.grade_student(3, 5, 1)
    przepis.get_report()


if '__main__' == __name__:
    main()
