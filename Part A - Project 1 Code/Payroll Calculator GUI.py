import tkinter


class MyGUI:
    def result(self):

        fullname = str(self.name_entry.get())
        last_name = fullname.split()[-1]
        hours = float(self.hours_entry.get())
        pay_rate = float(self.hourly_rate_entry.get())
        gross_pay = float(hours*pay_rate)
        tax_percentage = float(self.tax_rate_entry.get())*100
        tax = gross_pay*(float(self.tax_rate_entry.get()))
        medicare_percentage = float(self.medicare_entry.get())*100
        medicare_levy = gross_pay*(float(self.medicare_entry.get()))
        total_deduction = float(medicare_levy+tax)
        net_pay = float(gross_pay-total_deduction)

        hours_1dp = ("{:.1f}".format(hours))
        pay_rate_2dp = ("{:.2f}".format(pay_rate))
        gross_pay_2dp = ("{:.2f}".format(gross_pay))
        tax_percentage_1dp = ("{:.1f}".format(tax_percentage))
        tax_2dp = ("{:.2f}".format(tax))
        medicare_percentage_1dp = ("{:.1f}".format(medicare_percentage))
        medicare_levy_2dp = ("{:.2f}".format(medicare_levy))
        total_deduction_2dp = ("{:.2f}".format(total_deduction))
        net_pay_2dp = ("{:.2f}".format(net_pay))

        result = (
            f"Employee Name: {last_name}\n"
            f"Hours Worked: {hours_1dp}\n"
            f"Pay Rate: ${pay_rate_2dp}\n"
            f"Gross Pay: ${gross_pay_2dp}\n"
            "Deductions: \n"
            f"   ATO tax ({tax_percentage_1dp}%): ${tax_2dp}\n"
            f"   Medicare Levy ({medicare_percentage_1dp}%): ${medicare_levy_2dp}\n"
            f"   Total Deduction: ${total_deduction_2dp}\n"
            "\n"
            f"Net Pay: ${net_pay_2dp}\n"
            "\n"
        )

        self.result_ta.insert('1.0', result)

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x450+600+300')
        self.main_window.title("Payroll Calculator")

        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        name_label = tkinter.Label(self.frame1, text="Enter Employee's Name: ")
        self.name_entry = tkinter.Entry(self.frame1, bg='light grey', bd=2, width=20)
        name_label.pack(side='left')
        self.name_entry.pack(side='left')

        hours_label = tkinter.Label(self.frame2, text="Enter number of hours worked in a week: ")
        self.hours_entry = tkinter.Entry(self.frame2, bg='light grey', bd=2, width=20)
        hours_label.pack(side='left')
        self.hours_entry.pack(side='left')

        hourly_rate_label = tkinter.Label(self.frame3, text="Enter hourly pay rate: ")
        self.hourly_rate_entry = tkinter.Entry(self.frame3, bg='light grey', bd=2, width=20)
        hourly_rate_label.pack(side='left')
        self.hourly_rate_entry.pack(side='left')

        tax_rate_label = tkinter.Label(self.frame4, text="Enter ATO tax withholding rate: ")
        self.tax_rate_entry = tkinter.Entry(self.frame4, bg='light grey', bd=2, width=20)
        tax_rate_label.pack(side='left')
        self.tax_rate_entry.pack(side='left')

        medicare_label = tkinter.Label(self.frame5, text="Enter Medicare Levy rate: ")
        self.medicare_entry = tkinter.Entry(self.frame5, bg='light grey', bd=2, width=20)
        medicare_label.pack(side='left')
        self.medicare_entry.pack(side='left')

        enter_button = tkinter.Button(self.button_frame, text='Enter', command=self.result)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        enter_button.pack(side='left')
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light grey', height=20, width=150)
        self.result_ta.pack()

        self.frame1.pack(pady=2)
        self.frame2.pack(pady=2)
        self.frame3.pack(pady=2)
        self.frame4.pack(pady=2)
        self.frame5.pack(pady=2)
        self.button_frame.pack(pady=5)
        self.result_frame.pack(padx=50, pady=10)

        tkinter.mainloop()


my_gui = MyGUI()

