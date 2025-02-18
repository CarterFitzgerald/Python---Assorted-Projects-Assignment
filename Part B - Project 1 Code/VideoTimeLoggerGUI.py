import tkinter
from tkinter import messagebox
from tkinter import simpledialog


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('750x450+600+300')
        self.main_window.title('Video Time Logger Write Program')

        self.top_frame = tkinter.Frame()
        self.frame1 = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.num_videos_label = tkinter.Label(self.top_frame, text='How many videos are in the project? ')
        self.num_video_entry = tkinter.Entry(self.top_frame, bg='light grey', bd=2, width=10)
        self.btn_write_video_data = tkinter.Button(self.frame1, text="Prepare Video Times",
                                                   command=self.write_video_data)
        self.num_videos_label.pack(side='left')
        self.num_video_entry.pack(side='left')
        self.btn_write_video_data.pack(side='left')

        self.video_data_ta = tkinter.Text(self.result_frame, height=20, width=70)
        self.video_data_ta.configure(bg='light grey')
        self.btn_read_video_data = tkinter.Button(self.bottom_frame, text="Display Video Times",
                                                  command=self.read_video_report)
        self.quit_btn = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.video_data_ta.pack()
        self.btn_read_video_data.pack(side='left')
        self.quit_btn.pack(side='left')

        self.top_frame.pack(pady=5)
        self.frame1.pack()
        self.result_frame.pack(pady=5)
        self.bottom_frame.pack(pady=5, padx=5)

        tkinter.mainloop()

    def write_video_data(self):
        try:
            num_videos = int(self.num_video_entry.get())
            video_data_report = open('video_times.txt','w')
            messagebox.showinfo("showinfo", "'Enter the running times for each video.'")
            for count in range(1, num_videos+1):
                video_data = float(simpledialog.askstring(title="Video #" + str(count),
                                                          prompt='Enter running times for each video.'))
                video_data_report.write(str(video_data)+'\n')
            video_data_report.close()
            messagebox.showinfo("showinfo", "The times have now been saved.\n "
                                            "Now click on Display Video Times Button")
        except ValueError:
            messagebox.showinfo("Error", "Please enter a number")

    def read_video_report(self):
        disp_str = ""
        try:
            video_data_report = open("video_times.txt", 'r')
            total = 0.0
            disp_str += "Here are the running times for each video:"
            count = 0
            for line in video_data_report:
                video_data = float(line)
                count += 1
                disp_str += "\n Video #"+ str(count)+': '+ str(video_data)
                total += video_data

            disp_str += "\nThe total running time is " + str("{:,.1f}".format(total))+ ' seconds.'
            self.video_data_ta.insert('1.0', disp_str)

            video_data_report.close()
        except IOError:
            messagebox.showinfo("Error", "Could not open file")


my_gui = MyGUI()
