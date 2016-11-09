# Python 3
# from tkinter import Frame, Tk, Label, Button, filedialog, W, SUNKEN, X
# Python 2
from Tkinter import Frame, Tk, Label, Button, W, SUNKEN, X
import tkFileDialog

# - Note: Will re-import when status bar is working again.
# from tkinter import BOTTOM
#  - Experimentation:
# from tkinter import Frame, Tk, Label, Entry, Button, BOTH, Text, Menu, END, filedialog


class PmaConvert:
    def __init__(self, root):
        # Root
        root.geometry('700x250')
        root.title('PMA Convert')
        # root.title('PMA Convert, by Joe Flack & James Pringle')

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
            self.file_selection = tkFileDialog.askopenfilename(filetypes=file_types, title='Open one or more files.',
                                                        message='Open one or more files', multiple=1)
            if self.file_selection != '':
                self.set_status('Click on Convert to convert files.')
                log_output = 'File(s) ready for conversion: ' + str(self.file_selection)
                self.log.configure(text=log_output)
                print(log_output)

    def set_status(self, newStatus):
        self.status_bar.configure(text=newStatus)

    def log_text(self, newText):
        self.log.configure(text=self.log['text'] + '\n' + newText)

    def convert(self):
        if self.file_selection != '' and self.is_converting == False:
            self.is_converting = True
            self.log_text('Converting...')

            # This is a test. Move into if statement afterwards.
            # f = '/Users/joeflack4/Desktop/KER5-Household-Questionnaire-v12-jef.xls'
            f = self.file_selection

            # Note: May be best to avoid 'call' and use python 2.
            versions = ['python', 'python2', 'python27']

            # Testing alternative to call()
            # from qtools2 import convert as qtools_convert
            # from subprocess import call
            from subprocess import Popen, PIPE

            for version in versions:
                command_args = [version, '-m', 'qtools2.convert', '-v2']
                for file in f:
                    command_args.append(str(file))
                # command_args =[version, '-m',  'qtools2.convert',  '-v2', '/Users/joeflack4/Desktop/KER5-Female-Questionnaire-v12-jef.xls', '/Users/joeflack4/Desktop/KER5-Household-Questionnaire-v12-jef.xls']
                p = Popen(command_args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # p = Popen([version, ' -m qtools2.convert -v2 ' + '/Users/joeflack4/Desktop/KER5-Female-Questionnaire-v12-jef.xls /Users/joeflack4/Desktop/KER5-Household-Questionnaire-v12-jef.xls'],
                #           stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output, err = p.communicate(b"input data that is passed to subprocess' stdin")
                rc = p.returncode
                self.log_text(str(rc))
                self.log_text(str(err))
                # self.log_text(str(output))


                # call(self.run_conversion(version, f), shell=True)

            # call(self.run_conversion('python27', f), shell=True)
            # call(self.run_conversion('python2', f), shell=True)
            # call(self.run_conversion('python', f), shell=True)
            # TODO: This error handling needs fixing. It's not working at the moment because no error is registered, as a separate process is being run. Need a way to either get feedback from that process, or otherwise try another route perhaps. Maybe check using OS to see if an .xml file appeared.
            # TODO: Also have any errors display in the log.
            # try:
            #     call(self.run_conversion('python27', f), shell=True)
            # except:
            #     try:
            #         call(self.run_conversion('python2', f), shell=True)
            #     except:
            #         try:
            #             call(self.run_conversion('python', f), shell=True)
            #         except:
            #             self.log_text('Unexpected conversion error. Please contact your administrator.')

    def run_conversion(self, python_version, files):
        # TODO: Restore this when ready. But also need to break up this tuple first.
        # command = python_version + ' -m qtools2.convert -v2 ' + str(files)
        f = ''
        for file in files:
            f += ' ' + str(file)
        command = python_version + ' -m qtools2.convert -v2' + f
        # command = python_version + ' -m qtools2.convert -v2 ' + '/Users/joeflack4/Desktop/KER5-Female-Questionnaire-v12-jef.xls /Users/joeflack4/Desktop/KER5-Household-Questionnaire-v12-jef.xls'
        return command

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
# TODO: Get feedback in log when conversion is sucessful. This may require some work with qtools2, or otherwise find a way to get info from the console.
# TODO: Log needs to have fixed width.
# TODO: May be able to try multiple versions of python by checking the return code. And only return log text if conversion was successful.
# TODO: Need to reset window as well after giving feedback.
# - Medium Priority
# TODO: Might want to add some options.
# TODO: Alert on load if dependencies do not exist (try/except, perhaps)
# TODO: Make an installer.
# - Low Prioirity
# TODO: Position in middle of screen on load.
# TODO: Have in focus in front on load.
# TODO: Fix positioning issues (fill, anchor, expand, etc), or use grid instead.
# TODO: Add a dynamic cancel button.
# TODO: Add an error alert / message when buttons are clicked, but have been disabled.