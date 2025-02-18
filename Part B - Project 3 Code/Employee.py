class Employee:
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        result = ""
        result += '\n==============================' + \
            '\nName: ' + self.get_name() + \
            '\nID Number: ' + str(self.__id_num()) + \
            '\nDepartment: ' + str(self.__department()) + \
            '\nJob Title: ' + str(self.__job_title())

        return result


class ShiftEmployee(Employee):
    def __init__(self, name, id_num, department, job_title, shift_num, hrly_rate):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

        Employee.__init__(self, name, id_num, department, job_title)

        self.__shift_num = shift_num
        self.__hrly_rate = hrly_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_hrly_rate(self, hrly_rate):
        self.__hrly_rate = hrly_rate

    def get_shift_num(self):
        return self.__shift_num

    def get_hrly_rate(self):
        return self.__hrly_rate

    def __str__(self):
        result = ""
        result += Employee.__str__(self) + '\nShift Number: ' + \
            str(self.get_shift_num()) + \
            '\nHourly Rate: ' + str(self.get_hrly_rate())

        return result


class Contractor(Employee):
    def __init__(self, name, id_num, department, job_title, cont_end_date, abn, fixed_salary):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

        Employee.__init__(self, name, id_num, department, job_title)

        self.__cont_end_date = cont_end_date
        self.__abn = abn
        self.__fixed_salary = fixed_salary

    def set_cont_end_date(self, cont_end_date):
        self.__cont_end_date = cont_end_date

    def set_abn(self, abn):
        self.__abn = abn

    def set_fixed_salary(self, fixed_salary):
        self.__fixed_salary = fixed_salary

    def get_cont_end_date(self):
        return self.__cont_end_date

    def get_abn(self):
        return self.__abn

    def get_fixed_salary(self):
        return self.__fixed_salary

    def __str__(self):
        result = ""
        result += Employee.__str__(self) + '\nContract End Date: ' + \
            str(self.get_cont_end_date()) + \
            '\nAustralian Business Number (ABN): ' + str(self.get_abn()) + \
            '\nFixed Contract Salary: ' + str(self.get_fixed_salary())

        return result