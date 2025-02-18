import Employee
import pickle


LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
DISPLAY = 6

FILENAME = 'employees.dat'


def main():
    employees = load_employees()
    choice = 0
    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)
        elif choice == DISPLAY:
            disp(employees)

    save_employees(employees)


def load_employees():
    try:
        input_file = open(FILENAME, 'rb')
        employee_dict = pickle.load(input_file)
        input_file.close()
    except IOError:
        employee_dict = {}

    return employee_dict


def get_user_choice():
    print()
    print('Menu')
    print('----------------------------------------')
    print("1. Look up an Employee's Info")
    print("2. Add a new Employee's Info")
    print("3. Change and existing Employee's Info")
    print("4. Delete an Employee's Info")
    print('5. Quit the program')
    print("6. Display all Employee's Info")
    print()
    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > DISPLAY:
        choice = int(input('The choice you entered is invalid.'
                           ' Please enter a valid choice: '))

    return choice


def look_up(employees):
    id_num = input("Enter an Employee's ID number: ")
    print(employees.get(id_num, 'The specified ID number was not found'))


def add(employees):
    name = input("Enter the name: ")
    id_num = input("Enter the ID number: ")
    department = input("Enter the department: ")
    job_title = input("Enter the Job Title: ")

    new_employee = Employee.Employee(name, id_num, department, job_title)

    if id_num not in employees:
        employees[id_num] = new_employee
        print('The new Employee has been added.')
    else:
        print('An Employee with that ID already exists.')


def change(employees):
    id_num = input("Enter Employee's ID number: ")

    if id_num in employees:
        name = input('Enter new name: ')
        department = input('Enter new department: ')
        job_title = input('Enter the new job title: ')

        new_employee = Employee.Employee(name, id_num, department, job_title)

        employees[id_num] = new_employee
        print("Employee's information updated.")
    else:
        print('The specified ID Number was not found.')


def delete(employees):
    id_num = input("Enter Employee's ID number: ")

    if id_num in employees:
        del employees[id_num]
        print("Employee's information deleted.")
    else:
        print('The specified ID number was not found.')


def disp(employees):
    dictionary_items = employees.items()
    for id_num in employees:
        print("=================")
        print(str(employees[id_num]))


def save_employees(employees):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employees, output_file)
    output_file.close()

main()