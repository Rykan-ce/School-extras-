
#id, fname, lname, age, course
students = [
    [1, "John Michael", "Orias", 23, "IT"],
    [2, "Maryss", "De Juras", 19, "Psychology"],
    [3, "Rhaiven", "Cano", 20, "Entrepreneur"],
    [4, "Zhay", "Lorica", 18, "Teacher"]
]


def add_s(fname, lname, age, course):
    global students
    id = get_id()
    students.append([id, fname, lname, age, course])
    print('done')
    print_s()

def print_s():
    global students
    for student in students:
        print(student)

def get_id():
    if students:
        return max([student[0] for student in students]) + 1
    else:
        return 1

keep_running = True
def run():
    global keep_running
    while keep_running == True:
        print('[1] Add Student')
        print('[2] Student List')
        print('[3] Student List by Age ')
        print('[4] Student List by Last Name')
        print('[5] Exit')
        print('Choose a number: ')
        x = input()
        if x == "1":
            print('Enter student first name: ')
            fname = input()
            print('Enter student last name: ')
            lname = input()
            print('Enter students age: ')
            age = int(input())
            print('Enter student course: ')
            course = input()
            add_s(fname, lname, age, course)
            
        elif x == "2":
            print_s()
            
        elif x == "3":
            students.sort(key=lambda x: x[3]) # sort base on index 2 (price)
            for row in students:
                print(row)
            print()
        elif x == "4":
            sorted_lname = sorted(students, key=lambda product: product[2])
            for student in sorted_lname:
                print(student)
            
        else:
            keep_running = False
            print('the end!')
run()
