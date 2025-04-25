from tkinter import *
def Addfunction():
    Mylist.insert(END,E1.get() + '\n')
    E1.delete(0,END)
    
def delonefunction():
    Mylist.delete(ANCHOR)
    
win=Tk()
win.geometry('800x600')
win.title('To Do List')

L1=Label(win, text='Task Name:', font=('Bnazanin',  18 , 'bold'))
L1.place(x=0,y=5)

E1=Entry(win, font=('Bnazanin',  18 , 'bold'))
E1.place(x=140,y=5)

B1=Button(win, text='Add to list', bg='green', command=Addfunction)
B1.place(x=500,y=5)
B2=Button(win, text='Delete from List', bg='red', command=delonefunction)
B2.place(x=600,y=5)

Mylist=Listbox(win,height=13,width=45,bg='light blue',font=('Bnazanin',  18 , 'bold'))
Mylist.place(x=100,y=80)

win.mainloop
