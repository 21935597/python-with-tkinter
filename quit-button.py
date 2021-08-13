from tkinter import *
root = Tk()
root.geometry('300x300')
root.title("Lindokuhle's code")
c = Canvas(root,width=250, height=250,bg="blue")
c.pack()
myButton = Button(text="exit",command=quit)
myButton.pack()
def click():
    print("you have clicked a button")

    
myButton1 = Button(text="Hello",command=click())
myButton1.pack()
root.mainloop()
