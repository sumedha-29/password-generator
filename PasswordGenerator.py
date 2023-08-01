from tkinter import*
import random,string

#gui tittle and geometry
root = Tk()
root.geometry("400x280")
root.title("password Generator")
title = StringVar()

#gui inside label
label = Label(root,textvariable=title).pack()
title.set("The strength of password:")

#strength selection
def selection():
    selection=choice.get()
choice = IntVar()
R1=Radiobutton(root,text="POOR",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2=Radiobutton(root,text="AVG",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3=Radiobutton(root,text="ADV",variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice = Label(root)
labelchoice.pack()
lengthlabel = StringVar()
lengthlabel.set("password length")

lengthtitle = Label(root,textvariable=lengthlabel).pack() 

#passwordlength box
val = IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack() 

#retun function
def callback():
    buttonlabel.config(text=passgen())
passgenButton = Button(root,text="Gen pass",bd=5,height=2,command=callback,pady=3).pack()


#passgenButton.pack()
password=str(callback)
buttonlabel=Label(root,text="")
buttonlabel.pack(side=BOTTOM)
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="~!@#$%^&*()_+{}[]\|:;<>,.?/"
advance=poor+average+symbols

#logic function
def passgen():
    if choice.get()==1:
        return''.join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return''.join(random.sample(average,val.get()))
    elif choice.get()==3:
        return''.join(random.sample(advance,val.get())) 
root.mainloop()