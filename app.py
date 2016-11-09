from tkinter import Frame, Tk, Label, Button, filedialog, W, SUNKEN, X
# - Note: Will re-import when status bar is working again.
# from tkinter import BOTTOM
#  - Experimentation:
# from tkinter import Frame, Tk, Label, Entry, Button, BOTH, Text, Menu, END, filedialog



class PmaConvert:
    def __init__(self, root):
        # Root
        root.geometry("700x400")
        root.title("PMA Convert, by Joe Flack & James Pringle")

        # UI
        ## Frames
        self.centerFrame = Frame(root)
        self.centerFrame.place(relx=.5, rely=.5, anchor='c')

        ## Components
        self.q1_label = Label(self.centerFrame, text='1. Choose XLSForm (.xls or .xlsx) file(s) for conversion.')
        self.q1_label.pack()
        self.q1_button = Button(self.centerFrame, text='Choose file...', fg='black', command=self.on_open)
        self.q1_button.pack()

        # self.q2_label = Label(topFrame, text='2. Choose location for output file(s).').pack()
        # self.q4_button = Button(topFrame, text='Choose location...', fg='black').pack()

        # self.q3_label = Label(topFrame, text='3. Choose conversion options.').pack()

        self.q4_label = Label(self.centerFrame, text='2. Run conversion.')
        self.q4_label.pack()
        self.log = Label(self.centerFrame, text='', bd=1, relief=SUNKEN, anchor=W)
        self.file_selection = ''
        self.is_converting= False
        self.q4_button = Button(self.centerFrame, text='Convert', fg='black', command=self.convert)
        self.q4_button.pack()
        self.log.pack(fill=X, expand=1)

        self.status_bar = Label(self.centerFrame, text='Awaiting file selection.', bd=1, relief=SUNKEN, anchor=W)
        # - Note: Strangely this stopped anchoring to bottom suddenly, for some reason. So it is temporarily disabled.
        # self.status_bar.pack(side=BOTTOM, fill=X)

        # Run
        root.mainloop()

    # Functions
    def on_open(self):
        if self.is_converting == False:
            file_types = [('XLS Files', '*.xls'), ('XLSX Files', '*.xlsx'), ('All files', '*')]
            self.file_selection = filedialog.askopenfilename(filetypes=file_types, title='Open one or more files.',
                                                        message='Open one or more files', multiple=1)
            if self.file_selection != '':
                self.set_status('Click on Convert to convert files.')
                self.log.configure(text='File(s) ready for conversion: '+str(self.file_selection))

    def set_status(self, newStatus):
        self.status_bar.configure(text=newStatus)

    def logText(self, newText):
        self.log.configure(text=self.log['text'] + '\n' + newText)

    def convert(self):
        if self.file_selection != '' and self.is_converting == False:
            self.is_converting = True
            self.logText('Converting...')

if __name__ == '__main__':
    pma_convert = PmaConvert(Tk())

    # TESTING - anchor, fill, expand still not working.
    # root = Tk()
    # root.geometry("550x600")
    # frame = Frame(root)
    # frame.pack()
    # q4_entry = Label(frame, text='testing', anchor=W)
    # q4_entry.pack(fill=X, expand=1)
    # root.mainloop()

# Tasks
# - High Priority
# TODO: Get conversion working.
# - Medium Priority
# TODO: Alert on load if dependencies do not exist (try/except, perhaps)
# TODO: Make an installer.
# - Low Prioirity
# TODO: Position in middle of screen on load.
# TODO: Have in focus in front on load.
# TODO: Fix positioning issues (fill, anchor, expand, etc), or use grid instead.
# TODO: Add a dynamic cancel button.
# TODO: Add an error alert / message when buttons are clicked, but have been disabled.