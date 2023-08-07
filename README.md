# Homework 7

This package contains a set of Python scripts to generate a university database and fake data for it.
Also, this package contains a bunch of examples that could be used **only** with the UNIVERSITY.db file, which is included in this package.

## Package contains:

**Tools to create a new database:**
1. create_tables.py - create a new database  
2. fake_data.py - generate random names and other data for students, groups, teachers, subjects, and grades.  

**Tools for working with the previously created database:**  
1. university_sqlite.db - completed database  
2. my_select.py - Execute the queries using the  scripts. When prompted, enter the number of script you want to execute.  
1 - Find the 5 students with the highest average grade across all subjects.  
2 - Find the student with the highest average grade in a specific subject.  
3 - Calculate the average grade for each group in a specific subject.  
4 - Calculate the overall average grade across all grades.  
5 - List the subjects taught by a specific teacher.  
6 - Find the list of students in a specific group.
7 - Get the grades of students in a particular group for a specific subject.  
8 - Calculate the average grade given by a specific teacher across all their subjects.  
9 - Find the list of courses attended by a specific student.  
10 - Find the list of courses a specific teacher teaches to a particular student.  

**Installation**  
Clone the repository to your local machine:  

	git clone https://github.com/SvMyko/PyWebHW7.git

 Install the required libraries:
 
 	pip install faker
       pip install alembic
       pip install sqlachemy

**License**  
This project is licensed under the MIT License.
