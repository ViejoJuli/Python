"""
We are creating a grid
"""
from tkinter import*
root=Tk()
e= Entry(root,width=50,borderwidth=5)
e.insert(0,"Only characters")
e.pack()
def myClick():
    myLabel= Label(root, text="Hello " +e.get())
    myLabel.pack() #Pack put onto screen
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My Name is Julian")
myButton= Button(root, text="Enter Your Name",padx=50, command=myClick,fg="#000000",bg="red") #Dont put parentesis
#Shoving (empujar) it onto (in a particular place) the screen
#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=0,column=2) #Its relative, if i dont have more columns
myButton.pack()

root.mainloop()
