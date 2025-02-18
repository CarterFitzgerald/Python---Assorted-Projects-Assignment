import tkinter
from tkinter import *


class MyGUI:
    def result(self):
        days = int(self.entry3.get())
        start_pop = int(self.entry1.get())
        growth_rate = int(self.entry2.get().strip().replace('%', ''))
        new_growth_rate = (growth_rate/100)+1

        day_list = []
        for i in range(1, (days+1)):
            day_list.append(i)
        pop_list = [start_pop]
        while (days-1) > 0:
            new_growth = (start_pop * new_growth_rate) - start_pop
            start_pop += new_growth
            start_pop_format = (round(start_pop, 5))
            pop_list.append(start_pop_format)
            days -= 1

        self.result_ta.insert('1.0', "Day Approximate\n")
        self.result2_ta.insert('1.0', "Population\n")
        for day in day_list:
            self.result_ta.insert(END, str(day) + '\n')
        for pop in pop_list:
            self.result2_ta.insert(END, str(pop) + '\n')

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x450+600+300')
        self.main_window.title("Organism Population Tracker")

        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        self.result2_frame = tkinter.Frame()

        self.starting_organism_label = tkinter.Label(self.frame1, text="Starting number of organisms: ")
        self.entry1 = tkinter.Entry(self.frame1, bg='light grey', bd=2, width=10)
        self.starting_organism_label.pack(side='left')
        self.entry1.pack(side='left')
        self.daily_increase_label = tkinter.Label(self.frame2, text="Average daily population increase"
                                                                    "as a percentage: ")
        self.entry2 = tkinter.Entry(self.frame2, bg='light grey', bd=2, width=10)
        self.daily_increase_label.pack(side='left')

        self.entry2.pack(side='left')
        self.multiply_days_label = tkinter.Label(self.frame3, text="Number of days the organism will "
                                                                   "be left to multiply: ")
        self.entry3 = tkinter.Entry(self.frame3, bg='light grey', bd=2, width=10)
        self.multiply_days_label.pack(side='left')
        self.entry3.pack(side='left')

        enter_button = tkinter.Button(self.button_frame, text='Enter', command=self.result)
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        enter_button.pack(side='left')
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg='light grey', height=20, width=20, relief=FLAT)
        self.result_ta.pack()
        self.result2_ta = tkinter.Text(self.result2_frame, bg='light grey', height=20, width=20, relief=FLAT)
        self.result2_ta.pack()

        self.frame1.pack(pady=3)
        self.frame2.pack(pady=3)
        self.frame3.pack(pady=3)
        self.button_frame.pack(pady=5)
        self.result_frame.pack(anchor='e', side='left', expand=True)
        self.result2_frame.pack(anchor='w', side='right', expand=True)

        tkinter.mainloop()


my_gui = MyGUI()
