import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x450+600+300')
        self.main_window.title('Password Checker')

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.password_label = tkinter.Label(self.top_frame, text="Enter a string for a password: ")
        self.password_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width=20)
        self.password_label.pack(side='left', pady=10)
        self.password_entry.pack(side='left', pady=10)

        enter_button = tkinter.Button(self.button_frame, text='Enter', command=self.main)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        enter_button.pack(side='left')
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light grey', height=2, width=20, relief=tkinter.FLAT)
        self.result_ta.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack(pady=5)

        tkinter.mainloop()

    def len_check(self):
        password = self.password_entry.get()
        while len(password) < 8:
            return "invalid"

    def symbol_check(self):
        password = self.password_entry.get()
        sym_check = password.isalnum()
        if sym_check:
            return "valid"
        else:
            return "invalid"

    def number_check(self):
        password = self.password_entry.get()
        if len([x for x in password if x.isdigit()]) < 2:
            return "invalid"
        else:
            return "valid"

    def validity_check(self):
        if self.len_check() == "invalid":
            return "invalid password"
        elif self.symbol_check() == "invalid":
            return "invalid password"
        elif self.number_check() == "invalid":
            return "invalid password"
        else:
            return "valid password"

    def main(self):
        if self.validity_check() == "invalid password":
            self.result_ta.insert('1.0', "invalid password")
        else:
            self.result_ta.insert('1.0', "valid password")

my_gui = MyGUI()
