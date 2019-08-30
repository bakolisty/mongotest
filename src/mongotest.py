from mongoengine import *
from tkinter import *

connect('mongotest')


class Question(Document):
    qtext = StringField(required=True)
    svalue = IntField()


Question(qtext='Who here likes pizza?', svalue=0).save()

# Logic for submit button
def add_question():
    Question(qtext=qname.get(), svalue=svalue.get()).save()

# Creating Window
win = Tk()

# Create submit button and set position
Button(win, text="Add Question", command=add_question).grid(row=0, column=0)

# Variable that holds question string
qname = StringVar()

# Create text entry field and set position
Entry(win, textvariable=qname).grid(row=0, column=1, columnspan=2)

# Set label for radio buttons
Label(win, text="What is this questions severity?").grid(row=1, columnspan=3)

# Variable that holds radio button value
svalue = IntVar()

# Create radio buttons and set position
Radiobutton(win, text="not severe", variable=svalue, value=0).grid(row=2, column=0,)
Radiobutton(win, text="kinda severe", variable=svalue, value=1).grid(row=2, column=1)
Radiobutton(win, text="SUPER SEVERE", variable=svalue, value=2).grid(row=2, column=2)

# Label for question options
Label(win, text="What answers should this question have?").grid(row=3, columnspan=3)

# Create check buttons for question answers
cvalue1 = IntVar()
Checkbutton(win, text="Yes", variable=cvalue1).grid(row=4, column=0)
cvalue2 = IntVar()
Checkbutton(win, text="No", variable=cvalue2).grid(row=4, column=1)
cvalue3 = IntVar()
Checkbutton(win, text="NA", variable=cvalue3).grid(row=4, column=2)

# Label for wrong answer selection
Label(win, text="What answer is wrong?").grid(row=5, columnspan=2)

# Variable to store wrong value
wvalue = IntVar()

# Create radio buttons and set position
Radiobutton(win, text="Yes", variable=wvalue, value=0).grid(row=6, column=0,)
Radiobutton(win, text="No", variable=wvalue, value=1).grid(row=6, column=1)


# Running Window
win.mainloop()

