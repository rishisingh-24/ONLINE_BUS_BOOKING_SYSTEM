try:
    from tkinter import *
except:
    from Tkinter import *

divs=Tk()
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()
divs.geometry('%dx%d'%(w,h))
divs.title("HOME")


img=PhotoImage(file='.//Bus_for_project.png')#BUS IMAGE 
Label(divs,image=img).grid(row=0,column=0,padx=w//2.4,columnspan=3)



Label(divs,text="ONLINE BUS BOOKING SYSTEM",font="Arial 30 bold",relief="ridge",fg="Red",bg="Light Blue").grid(row=1,column=0,columnspan=3)#INSIDE HOME

for  i in range(2,5):#TO CREATE COLUMN SPACES
    Label(divs,text=" ").grid(row=i,column=0)

def destroy_1():
    divs.destroy()
    import BOOKING
def destroy_2():
    divs.destroy()
    import CHECK
def destroy_3():
    divs.destroy()
    import DATABASE_DETAIL
Button(divs,text="Seat Booking",font="Arial 20 bold",bg="Light Green",command=destroy_1).grid(row=5,column=0)#BUTTON FOR SEAT BOOKING AND CONNECT TO BOOKING GUI

Button(divs,text="Check Booked Seat",font="Arial 20 bold",bg="Light Green",command=destroy_2).grid(row=5,column=1)#BUTTON FOR CHECKING BOOKED SEAT AND CONNECT TO CHECK GUI

Button(divs,text="Add Bus Details",font="Arial 20 bold",bg="Light Green",command=destroy_3).grid(row=5,column=2)#BUTTON FOR ADDING BUS DETAILS AND CONNECT TO ADDING GUI

Label(divs,text=" ").grid(row=6,column=0)#TO CREATE SPACE BETWEEN ROWS
Label(divs,text=" For Admins Only",font="Arial 15 bold",fg="Red").grid(row=7,column=2)

divs.mainloop()

    
