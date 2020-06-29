from tkinter import *

def printhello() :
    print('hi')


root = Tk()


w = Label(root, text="Python Test")
b = Button(root, text="Hello python", command=printhello)
c = Button(root, text="Quit", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
