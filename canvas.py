from tkinter import *
root = Tk()
root.geometry('300x300')
root.title("Lindokuhle's code")
c = Canvas(root,width=250, height=250,bg="blue")
c.pack()
myButton = Button(text="Click me")
myButton.pack()
root.mainloop()
