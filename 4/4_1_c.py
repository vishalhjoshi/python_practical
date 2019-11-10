db = 'student.txt'

def insert(file_name, stud_name, roll_no, marks):
    num_lines = sum(1 for line in open(file_name))
    if num_lines == 0:
        stud_id = 1
    else:
        stud_id = num_lines + 1
    with open(file_name, 'a') as af:
        af.write("{},{},{},{}\n".format(stud_id, stud_name, roll_no, marks))
    print("Record Inserted !")


def update(file_name, std_id, name, roll_no, marks):
    with open(file_name, 'r') as rf:
        lst_tuples = []
        for line in rf:
            line = tuple(line.strip('\n').split(','))
            lst_tuples.append(line)
        # print(len(lst_tuples))
        if len(lst_tuples) == 0:
            print("Data Not Found In File")
            return
        elif int(std_id) < 1 or int(std_id) > len(lst_tuples):
            print("Student Id Not Found Database")
            return
        else:
            with open(file_name, 'w') as wf:
                given_id = std_id
                given_data = (name, roll_no, marks)
                for student in lst_tuples:
                    stud_id, stud_name, roll_no, marks = student
                    if stud_id == str(given_id):
                        stud_name, roll_no, marks = given_data
                    wf.write("{},{},{},{}\n".format(stud_id, stud_name, roll_no, marks))
            print("Record Updated !")


def delete(file_name, std_id):
    with open(file_name, 'r') as rf:
        lst_tuples = []
        for line in rf:
            line = tuple(line.strip('\n').split(','))
            lst_tuples.append(line)
        # print(len(lst_tuples))

        if len(lst_tuples) == 0:
            print("Data Not Found In File")
            return
        elif int(std_id) < 1 or int(std_id) > len(lst_tuples):
            print("Student Id Not Found Database")
            return
        else:
            given_id = std_id
            for i in lst_tuples:
                if i[0] == str(given_id):
                    lst_tuples.remove(i)

            with open(file_name, 'w') as wf:
                for student in lst_tuples:
                    stud_id, stud_name, roll_no, marks = student
                    if int(stud_id) > int(given_id):
                        wf.write("{},{},{},{}\n".format(int(stud_id) - 1, stud_name, roll_no, marks))
                    else:
                        wf.write("{},{},{},{}\n".format(stud_id, stud_name, roll_no, marks))

                print("Record Deleted !")


def read(file_name):
    num_lines = sum(1 for line in open(file_name))
    if num_lines == 0:
        print("No Data Found !")
    else:
        with open(file_name, 'r') as file:
            print("id|name|roll_no|marks")
            for students in file:
                student = tuple(students.strip('\n').split(','))
                stud_id, stud_name, roll_no, marks = student
                # print(student)
                print("{}|{}|{}|{}".format(stud_id, stud_name, roll_no, marks))


def menu():
    print()
    print('------------MENU------------')
    print('1.SHOW ALL STUDENTS')
    print('2.INSERT NEW STUDENT')
    print('3.UPDATE EXISTING STUDENT')
    print('4.DELETE STUDENT')
    print('5.EXIT')


menu()
option = input("Enter Option from Above Menu ! >> ")

if option == '1':
    read(db)
elif option == '2':
    name = input("Enter Student Name >> ")
    roll_no = input("Enter Student Roll Number >> ")
    marks = input("Enter Student Marks >> ")
    insert(db, stud_name=name, roll_no=roll_no, marks=marks)
elif option == '3':
    std_id = input("Enter Student Id >> ")
    name = input("Enter Student Name To  Update >> ")
    roll_no = input("Enter Student Roll Number To  Update >> ")
    marks = input("Enter Student Marks To  Update >> ")
    update(db, std_id=std_id, name=name, roll_no=roll_no, marks=marks)
elif option == '4':
    std_id = input("Enter Student Id >> ")
    delete(db, std_id=std_id)
elif option == '5':
    exit(0)
else:
    print("Please Enter Valid Input !")





















































































