import Employee


def main():
    employee1_info = Employee.Employee('Susanna Myer', 47899, 'Accounting', 'Vice President')
    employee2_info = Employee.Employee('Mark Joseph', 39119, 'Info Tech', 'Programmer')
    employee3_info = Employee.Employee('Joyce Roberts', 81774, 'Manufacturing', 'Engineer')

    print('Employee 1 Info:')
    display_info(employee1_info)
    print()
    print('Employee 2 Info:')
    display_info(employee2_info)
    print()
    print('Employee 3 Info:')
    display_info(employee3_info)
    print()


def display_info(info):
    print('Name: ', info.get_name())
    print('ID Number: ', info.get_id_num())
    print('Department: ', info.get_department())
    print('Job Title: ', info.get_job_title())


main()