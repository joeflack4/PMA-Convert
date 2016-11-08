from tkinter import *


# Root
root = Tk()


# Frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

# Components
label1 = Label(topFrame, text='Label 1')
label1.pack()
button1 = Button(topFrame, text='Button 1', fg='black')
button1.pack()

label2 = Label(bottomFrame, text='Label 2')
label2.pack()
button2 = Button(bottomFrame, text='Button 2', fg='black')
button2.pack()

# Run
root.mainloop()
