import mysql.connector
from tkinter import *
def search():
    mdb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='afshindatabase'
    )
    myconection=mdb.cursor()
    name_kala=name_entry.get()
    sql_statement='select capital , language from afshintable where country=%s'
    myconection.execute(sql_statement,(name_kala,))
    r=myconection.fetchall()
    for x in r:
        print (x)
win =Tk()
win.geometry("500x400")
name_entry=Entry(win)
name_entry.place(x=50 , y=100)
search_button=Button(win, text='search', command=search)
search_button.place(x=200 , y=100)
win.mainloop()
