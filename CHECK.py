try:
    from tkinter import *
    from tkinter.messagebox import *
except:
    from Tkinter import *
    from Tkinter.messagebox import *


                                                # CREATING DATABASE
import sqlite3

con=sqlite3.Connection("PROJECT")
cur=con.cursor()






                                                    #WINDOWS CONFIGURE
divs=Tk()
divs.title("CHECK_TICKET")
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()#SET GUI TO SCREEN SIZE
divs.geometry('%dx%d'%(w,h))


img=PhotoImage(file='.\\Bus_for_project.png')#ADD BUS IMAGE
Label(divs,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=w//50)


#ONLINE BUS BOOKING SYSTEM
Label(divs,text="Online Bus Booking System",relief="ridge",font="Arial 30 bold",fg="Red",bg="Light Blue").grid(row=1,column=0,columnspan=w//50)

#CHECK YOUR BOOKING
Label(divs,text=" ").grid(row=2,column=0)
Label(divs,text="Check Your Booking",font="Arial 20 bold",relief="ridge",fg="Green",bg="Light Green").grid(row=3,column=0,columnspan=w//50)

#ENTER YOUR NAME
Label(divs,text=" ").grid(row=4,column=0)
Label(divs,text=" ").grid(row=5,column=0,padx=w//7)
Label(divs,text="Enter your mobile number :",font="bold 15").grid(row=5,column=1)
M_No=Entry(divs,font=" Arial 15 bold",width=20)
M_No.grid(row=5,column=2) 




                                                                #DATABASE USED IN SHOW TICKET
def check():
    mno=M_No.get()
    if(len(mno)==0):
        showerror('INCOMPLETE','YOU HAVE NOT FILLED ALL FIELDS')
        return 1
    cur.execute("select passen_phone from booking")
    catch=cur.fetchall()
    print(catch)
    mno_yes=0
    for i in range(len(catch)):
        if( int(mno) in catch[i]):
            mno_yes+=1
    if(mno_yes!=0):
        cur.execute("select * from booking")
        detail_passen=cur.fetchall()

        

                                                #BUS TICKET

        
        Label(divs,text=" ").grid(row=6,column=0)#CREATE SPACE BETWEEN ROWS
        Label(divs,text=" ").grid(row=7,column=0)#CREATE SPACE BETWEEN ROWS
        frame=Frame(divs,relief="ridge",bd=8)#CAN ALSO USE GROOVE OR RAISED INSTEAD OF RIDGE
        frame.grid(row=8,column=0,columnspan=w//50)
        Label(frame,text="Passengers : " + detail_passen[0][0] + "      " +"Gender : " + detail_passen[0][7] ,font="Arial 15 bold").grid(row=8,column=0)
        #Label(text="Gender :",font="Arial 15 bold").grid(row=5,column=1)
        #Label(divs,text=" ").grid(row=6,column=0)#CREATE SPACE BETWEEN ROWS
        Label(frame,text="No. of seats : " + str(detail_passen[0][1]) + "      " + "Phone : " + str(detail_passen[0][6]),font="Arial 15 bold").grid(row=10,column=0)
        #Label(text="Phone :",font="Arial 15 bold").grid(row=7,column=1)
        #Label(divs,text=" ").grid(row=8,column=0)#CREATE SPACE BETWEEN ROWS
        Label(frame,text="Age : " + str(detail_passen[0][8])+ "      " + "Fare Rs : " + str(detail_passen[0][2]),font="Arial 15 bold").grid(row=12,column=0)
        #Label(text="Fare Rs :",font="Arial 15 bold").grid(row=9,column=1)
        #Label(divs,text=" ").grid(row=10,column=0)#CREATE SPACE BETWEEN ROWS
        Label(frame,text="Travel On : " + detail_passen[0][5]+"      " + "Bus Details : " + detail_passen[0][9],font="Arial 15 bold").grid(row=14,column=0)
        #Label(text="Bus Details :",font="Arial 15 bold").grid(row=11,column=1)
        #Label(divs,text=" ").grid(row=12,column=0)#CREATE SPACE BETWEEN ROWS
        #Label(text="Booked On :",font="Arial 15 bold").grid(row=13,column=1)
        #Label(divs,text=" ").grid(row=14,column=0)#CREATE SPACE BETWEEN ROWS
        Label(frame,text="Destination : " + detail_passen[0][4]+"      " + "Boarding Point : " + detail_passen[0][3],font="Arial 15 bold").grid(row=16,column=0)
        #Label(text="Boarding Point :",font="Arial 15 bold").grid(row=15,column=1)


        Label(frame,text="*Total amount Rs " + str(detail_passen[0][2])+" to be paid at the time of boarding the bus",font="Arial 12 italic").grid(row=17,column=0)

    else:
        QUE=askyesno("NOT FOUND","There is no bus found booked by this no...\n\nDo you want to book bus by this number ?")
        if(QUE):
            con.close()
            divs.destroy()
            import BOOKING                                
            '''CONNECT TO BOOKING GUI'''
        else:
            return 1
            
#BUTTON
Button(divs,text="Check Booking",font="bold 15",command=check).grid(row=5,column=3)


                                
Label(divs,text=" ").grid(row=6,column=0)#CREATE SPACE BETWEEN ROWS
Label(divs,text=" ").grid(row=7,column=0)#CREATE SPACE BETWEEN ROWS

for i in range(4,10):
    Label(divs,text= " ").grid(row=5,column=i)


divs.mainloop()
