from create_tables import Group, Teacher, Subject, Student, Grade, Session
from sqlalchemy import func
from functools import wraps
from sqlalchemy.exc import SQLAlchemyError


def handle_database_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except SQLAlchemyError as e:
            print(f"An error occurred while working with the database: {e}")
            return None
    return wrapper


@handle_database_errors
def select_1():
    result = session.query(Student.name, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade) \
        .group_by(Student.student_id) \
        .order_by(func.avg(Grade.grade).desc()) \
        .limit(5) \
        .all()
    print('; '.join(f"{row[0]} : {row[1]:.2f}" for row in result))


@handle_database_errors
def select_2(student_name='Melissa Wright', subject_name='Chemistry'):
    student_name, avg_grade = session.query(Student.name, func.avg(Grade.grade).label('avg_grade')) \
        .join(Grade) \
        .join(Subject) \
        .filter(Student.name == student_name, Subject.subject_name == subject_name) \
        .group_by(Student.student_id) \
        .first()
    print(f"{student_name}: {avg_grade:.2f}")


@handle_database_errors
def select_3(subject_name='Computer_science'):
    result = session.query(Group.group_id, func.avg(Grade.grade).label('avg_grade')) \
        .select_from(Group) \
        .join(Student) \
        .join(Grade) \
        .join(Subject) \
        .filter(Subject.subject_name == subject_name) \
        .group_by(Group.group_id) \
        .all()
    print(", ".join([f"Group {group_id}: {avg_grade:.2f}" for group_id, avg_grade in result]))


@handle_database_errors
def select_4():
    result = session.query(func.avg(Grade.grade).label('avg_grade')).scalar()
    print(result)


@handle_database_errors
def select_5(teacher_name='Ronald Floyd'):
    result = session.query(Subject.subject_name) \
        .join(Teacher) \
        .filter(Teacher.name == teacher_name) \
        .all()
    print('; '.join(f"{row[0]} " for row in result))


@handle_database_errors
def select_6(group_name='Group 1'):
    result = session.query(Student.name) \
        .join(Group) \
        .filter(Group.group_name == group_name) \
        .all()
    print('; '.join([student.name for student in result]))


@handle_database_errors
def select_7(group_name='Group 1', subject_name='Physics'):
    result = session.query(Student.name, Grade.grade) \
        .join(Group) \
        .join(Grade) \
        .join(Subject) \
        .filter(Group.group_name == group_name, Subject.subject_name == subject_name) \
        .all()
    print('; '.join(f"{row[0]} : {row[1]:.2f}" for row in result))


@handle_database_errors
def select_8(teacher_name='Ronald Floyd'):
    result = session.query(Teacher.name, func.avg(Grade.grade).label('avg_grade')) \
        .select_from(Teacher) \
        .join(Subject, Teacher.teacher_id == Subject.teacher_id) \
        .join(Grade, Subject.subject_id == Grade.subject_id) \
        .filter(Teacher.name == teacher_name) \
        .group_by(Teacher.teacher_id) \
        .all()
    print(', '.join(f"{row[0]} : {row[1]:.2f}" for row in result))


@handle_database_errors
def select_9(student_name='Lauren Sweeney'):
    result = session.query(Subject.subject_name) \
        .join(Grade) \
        .join(Student) \
        .filter(Student.name == student_name) \
        .all()
    print(", ".join([row[0] for row in result]))


@handle_database_errors
def select_10(student_name='David Copeland', teacher_name='Jasmine Perez'):
    result = session.query(Subject.subject_name) \
        .join(Grade, Subject.subject_id == Grade.subject_id) \
        .join(Student, Grade.student_id == Student.student_id) \
        .join(Teacher, Subject.teacher_id == Teacher.teacher_id) \
        .filter(Student.name == student_name, Teacher.name == teacher_name) \
        .all()
    print(", ".join(row[0] for row in result))


script_list = {'1': select_1,
               '2': select_2,
               '3': select_3,
               '4': select_4,
               '5': select_5,
               '6': select_6,
               '7': select_7,
               '8': select_8,
               '9': select_9,
               '10': select_10
               }
if __name__ == "__main__":
    print('''List of supported scripts:
        1 - Find the 5 students with the highest average grade across all subjects.
        2 - Find the student with the highest average grade in a specific subject.
        3 - Calculate the average grade for each group in a specific subject.
        4 - Calculate the overall average grade across all grades.
        5 - List the subjects taught by a specific teacher.
        6- Find the list of students in a specific group. 
        7 query_7.sql - Get the grades of students in a particular group for a specific subject.
        8 - Calculate the average grade given by a specific teacher across all their subjects.
        9 - Find the list of courses attended by a specific student.
        10 - Find the list of courses a specific teacher teaches to a particular student.
        exit - Close the program''')
    session = Session()
    while True:
        input_script = input('Input script number (or "exit" to quit): ')
        if input_script.lower() == 'exit':
            print("Program closed")
            break
        selected_function = script_list.get(input_script)
        if selected_function is not None:
            selected_function()
        else:
            print("Invalid script number")
