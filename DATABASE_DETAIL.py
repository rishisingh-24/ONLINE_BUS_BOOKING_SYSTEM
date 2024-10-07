try:
    from tkinter import *
except:
    from Tkinter import *

#WINDOWS CONFIGURE
divs=Tk()
divs.title("CHECK_TICKIT")
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()#SET GUI TO SCREEN SIZE
divs.geometry('%dx%d'%(w,h))



img=PhotoImage(file='.\\Bus_for_project.png')#ADD BUS IMAGE
Label(divs,image=img).grid(row=0,column=0,padx=w//2.5,columnspan=w//90)


#ONLINE BUS BOOKING SYSTEM
Label(divs,text="Online Bus Booking System",relief="ridge",font="Arial 30 bold",fg="Red",bg="Light Blue").grid(row=1,column=0,columnspan=w//90)


#CREATE SPACE
Label(divs,text=" ").grid(row=2,column=0)
Label(divs,text=" ").grid(row=3,column=0)
Label(divs,text="Add new details to database",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=w//90)

def destroy_1():
    divs.destroy()
    import ADD_BUS_OPERATOR
def destroy_2():
    divs.destroy()
    import ADD_BUS
def destroy_3():
    divs.destroy()
    import ADD_RUN
def destroy_4():
    divs.destroy()
    import ADD_ROUTE




#BUTTONS
Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text=" ").grid(row=6,column=0)
Label(divs,text=" ").grid(row=7,column=0,padx=w//8)
Button_1=Button(divs,text="NEW OPERATOR",command=destroy_1,font="Arial 15 bold",bg="sky blue")
Button_1.grid(row=7,column=1)
Button_2=Button(divs,text="NEW BUS",command=destroy_2,font="Arial 15 bold",bg="tomato")
Button_2.grid(row=7,column=2)
Button_3=Button(divs,text="NEW ROUTE",command=destroy_3,font="Arial 15 bold",bg="sandy brown")
Button_3.grid(row=7,column=3)
Button_4=Button(divs,text="NEW RUN",command=destroy_4,font="Arial 15 bold",bg="PaleVioletRed1")
Button_4.grid(row=7,column=4)


divs.mainloop()
