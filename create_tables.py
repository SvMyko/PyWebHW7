from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager


database_path = 'sqlite:///university_sqlite.db'
Base = declarative_base()
engine = create_engine(database_path, echo=False)
Session = sessionmaker(bind=engine)


@contextmanager
def create_connection():
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String)

class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String)

class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.group_id'))

class Grade(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade = Column(Integer)
    date_received = Column(Date)


if __name__ == "__main__":
    with create_connection() as connection:
        if connection is not None:
            Base.metadata.create_all(engine)
        else:
            print("Connection lost")
