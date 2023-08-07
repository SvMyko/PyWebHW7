from create_tables import Group, Teacher, Subject, Student, Grade, Session
from faker import Faker
import random

fake = Faker()


def generate_data(session, num_students=50, num_groups=3, num_teachers=3, num_subjects=5):
    students_data = [(fake.name(), random.randint(1, num_groups)) for _ in range(num_students)]
    groups_data = [(f"Group {group_id}",) for group_id in range(1, num_groups + 1)]
    teachers_data = [(fake.name(),) for _ in range(num_teachers)]
    subjects_data = [
        ("Chemistry", random.randint(1, num_teachers)),
        ("Physics", random.randint(1, num_teachers)),
        ("Mechatronics", random.randint(1, num_teachers)),
        ("Computer_science", random.randint(1, num_teachers)),
        ("Math", random.randint(1, num_teachers))
    ]

    grades_data = []
    for student_id in range(1, num_students + 1):
        for subject_id in range(1, num_subjects + 1):
            grades_data.append((
                student_id,
                subject_id,
                random.randint(1, 100),
                fake.date_between(start_date='-1y', end_date='today')
            ))

    for group_name in groups_data:
        session.add(Group(group_name=group_name[0]))

    for teacher_name in teachers_data:
        session.add(Teacher(name=teacher_name[0]))

    for subject_name, teacher_id in subjects_data:
        session.add(Subject(subject_name=subject_name, teacher_id=teacher_id))

    for student_name, group_id in students_data:
        session.add(Student(name=student_name, group_id=group_id))

    for student_id, subject_id, grade, date_received in grades_data:
        session.add(Grade(student_id=student_id, subject_id=subject_id, grade=grade, date_received=date_received))

    session.commit()


if __name__ == "__main__":
    session = Session()
    generate_data(session)
    session.close()
    print('Job done')