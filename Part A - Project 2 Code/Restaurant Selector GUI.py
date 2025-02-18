import tkinter
from tkinter import *


class MyGUI:
    def result(self):
        vegetarian_input = str(self.checkvar1.get())
        vegan_input = str(self.checkvar2.get())
        gluten_free_input = str(self.checkvar3.get())

        if vegetarian == 1 and vegan == 1 and gluten_free == 1:
            result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "\n"
        elif vegetarian == 1 and vegan == 1 and gluten_free == 0:
            result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "\n"
        elif vegetarian == 1 and vegan == 0 and gluten_free == 1:
            result = "Here are your restaurant choices: \n"\
                      "   Main Street Pizza Company\n" \
                      "   Corner Cafe\n" \
                      "   The Chef's Kitchen\n"\
                      "\n"
        elif vegetarian == 0 and vegan == 1 and gluten_free == 1:
            result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "\n"
        elif vegetarian == 0 and vegan == 1 and gluten_free == 0:
            result = "Here are your restaurant choices: \n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "\n"
        elif vegetarian == 0 and vegan == 0 and gluten_free == 1:
            result = "Here are your restaurant choices: \n" \
                     "   Main Street Pizza Company\n" \
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "\n"
        elif vegetarian == 1 and vegan == 0 and gluten_free == 0:
            result = "Here are your restaurant choices: \n" \
                     "   Main Street Pizza Company\n"\
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "   Mama's Fine Italian\n"\
                     "\n"
        else:
            result = "Here are your restaurant choices: \n" \
                     "   Joe's Gourmet Burgers\n"\
                     "   Main Street Pizza Company\n"\
                     "   Corner Cafe\n"\
                     "   The Chef's Kitchen\n"\
                     "   Mama's Fine Italian\n"\
                     "\n"

        self.result_ta.insert('1.0', result)

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x450+600+300')
        self.main_window.title('Restaurant Selector')

        self.Frame1 = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()

        self.checkvar1 = IntVar()
        self.checkvar2 = IntVar()
        self.checkvar3 = IntVar()

        self.title_label = tkinter.Label(text="Does anyone in the party require any of the below?")
        self.title_label.pack()
        self.C1 = Checkbutton(self.Frame1, text="Vegetarian", variable=self.checkvar1,
                              onvalue='yes', offvalue='no', height=0, width=20)
        self.C2 = Checkbutton(self.Frame1, text="Vegan", variable=self.checkvar2,
                              onvalue='yes', offvalue='no', height=0, width=20)
        self.C3 = Checkbutton(self.Frame1, text="Gluten-Free", variable=self.checkvar3,
                              onvalue='yes', offvalue='no', height=0, width=20)

        enter_button = tkinter.Button(self.button_frame, text='Enter', command=self.result)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        enter_button.pack(side='left')
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light grey', height=20, width=150)
        self.result_ta.pack()

        self.C1.pack()
        self.C2.pack()
        self.C3.pack()
        self.Frame1.pack(side=tkinter.TOP)
        self.button_frame.pack(pady=5)
        self.result_frame.pack(padx=50, pady=10)

        tkinter.mainloop()


my_gui = MyGUI()
