import pyodbc
from student_info.student import *

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-7OVA01V;"
                      "Database=ScheduleDB;"
                      "Trusted_connection=yes;")

cursor = cnxn.cursor()

def check_student(chat_id):
    rows = cursor.execute('SELECT * FROM Students')
    for row in rows:
        if(row[0] == chat_id):
            print('Already in data base')
            return True

def add_student(student):
    student_id = student.get_chat_id()
    path = 'D:\PyProjects\ScheduleBot\home_works\\' + str(student_id) + '.txt';
    hw_file = open("D:\PyProjects\ScheduleBot\home_works\\" + str(student_id) + ".txt", "w+")
    cursor.execute('INSERT INTO Students VALUES(?, ?, ?, ?, ?)',
                   student_id,
                   student.get_direction(),
                   student.get_course(),
                   student.get_group(),
                   path)
    hw_file.close()
    cnxn.commit()



