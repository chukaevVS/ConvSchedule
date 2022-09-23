import pyodbc
from student_info.student import *

cnxn = pyodbc.connect("Driver={SQL Server};"
                      "Server=DESKTOP-7OVA01V;"
                      "Database=ScheduleDB;"
                      "Trusted_connection=yes;")

cursor = cnxn.cursor()

def find_chat_id(chat_id, rows):
    for row in rows:
        if(row[0] == chat_id):
            return True


def add_student(student):
    rows = cursor.execute('SELECT * FROM Students')
    student_id = student.get_chat_id()
    if(find_chat_id(student_id, rows) == True):
        print('Already in data base')
    else:
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


