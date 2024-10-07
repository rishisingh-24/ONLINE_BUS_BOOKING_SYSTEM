from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox

#WINDOW CONFIGURE
divs=Tk()
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()
divs.geometry('%dx%d'%(w,h))
divs.title("Bus Ticket")


                                                # CREATING DATABASE
import sqlite3

con=sqlite3.Connection("PROJECT")
cur=con.cursor()




img=PhotoImage(file='.\\Bus_for_project.png')#INSERTING BUS IMAGE
Label(divs,image=img).grid(row=0,column=0,columnspan=1,padx=w//2.5)


Label(divs,text="Online Bus Booking System",font="Arial 30 bold",fg="Red",bg="Light Blue",relief="ridge").grid(row=1,column=0,columnspan=1)#INSIDE TICKET

Label(divs,text=" ").grid(row=2,column=0)#CREATE SPACE BETWEEN ROWS
Label(divs,text="Bus Ticket",font="Arial 15 bold underline",).grid(row=3,column=0,columnspan=1)

                                #BUS TICKET
cur.execute("select * from booking")
detail_passen=cur.fetchall()

l=len(detail_passen)
frame=Frame(divs,relief="ridge",bd=8)#CAN ALSO USE GROOVE OR RAISED INSTEAD OF RIDGE
frame.grid(row=5,column=0,columnspan=1)#CREATING FRAME FOR BOX
Label(divs,text=" ").grid(row=4,column=0)#CREATE SPACE BETWEEN ROWS
Label(frame,text="Passengers : " + detail_passen[l-1][0] + "      " +"Gender : " + detail_passen[l-1][7] ,font="Arial 15 bold").grid(row=5,column=0)
#Label(text="Gender :",font="Arial 15 bold").grid(row=5,column=1)
#Label(divs,text=" ").grid(row=6,column=0)#CREATE SPACE BETWEEN ROWS
Label(frame,text="No. of seats : " + str(detail_passen[l-1][1]) + "      " + "Phone : " + str(detail_passen[l-1][6]),font="Arial 15 bold").grid(row=7,column=0)
#Label(text="Phone :",font="Arial 15 bold").grid(row=7,column=1)
#Label(divs,text=" ").grid(row=8,column=0)#CREATE SPACE BETWEEN ROWS
Label(frame,text="Age : " + str(detail_passen[l-1][8])+ "      " + "Fare Rs : " + str(detail_passen[l-1][2]),font="Arial 15 bold").grid(row=9,column=0)
#Label(text="Fare Rs :",font="Arial 15 bold").grid(row=9,column=1)
#Label(divs,text=" ").grid(row=10,column=0)#CREATE SPACE BETWEEN ROWS
Label(frame,text="Travel On : " + detail_passen[l-1][5]+"      " + "Bus Details : " + detail_passen[l-1][9],font="Arial 15 bold").grid(row=11,column=0)
#Label(text="Bus Details :",font="Arial 15 bold").grid(row=11,column=1)
#Label(divs,text=" ").grid(row=12,column=0)#CREATE SPACE BETWEEN ROWS
#Label(text="Booked On :",font="Arial 15 bold").grid(row=13,column=1)
#Label(divs,text=" ").grid(row=14,column=0)#CREATE SPACE BETWEEN ROWS
Label(frame,text="Destination : " + detail_passen[l-1][4]+"      " + "Boarding Point : " + detail_passen[l-1][3],font="Arial 15 bold").grid(row=13,column=0)
#Label(text="Boarding Point :",font="Arial 15 bold").grid(row=15,column=1)

for i in range(8,12):
    Label(divs,text=" ").grid(row=i,column=0)
#Label(rishi,text=" ").grid(row=11,column=0)

Label(divs,text="Do you want to move to the home page",font="Arial 20 bold",fg="Red",bg="Light Blue",relief="ridge").grid(row=13,column=0)
def fun(c=0):
    status=messagebox.askyesno(title='Seat Booked',message="Move to home page")
    if status==True:
        divs.destroy()
        import HOME
    else:
        divs.destroy()
Button(divs,text="Click Here",command=fun,font="Aerial 12",bg="orange red").grid(row=14,column=0,pady=10)
divs.bind('keypress',fun)


Label(frame,text="*Total amount Rs " + str(detail_passen[l-1][2])+" to be paid at the time of boarding the bus",font="Arial 12 italic",).grid(row=14,column=0)

showinfo('Success',"Seat Booked.....")



'''AFTER CLOSING THIS MESSAGE BOX SHOULD APPEAR THAT WILL SHOW TO GO TO HOME PAGE'''

divs.mainloop()
