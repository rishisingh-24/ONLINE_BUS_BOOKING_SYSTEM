try:
    from tkinter import *
except:
    from Tkinter import *

#WINDOWS CONFIGURE    
divs=Tk()
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()
divs.geometry('%dx%d'%(w,h))
divs.title("MAIN")#MAIN WHICH SHOW NAME

img=PhotoImage(file='.\\Bus_for_project.png')#BUS IMAGE 
Label(divs,image=img).grid(row=0,column=0,padx=w//2.5)


Label(divs,text="Online Bus Booking System",font="Arial 35 bold",fg="Red",bg="Light Blue").grid(row=1,column=0)#INSIDE MAIN

#Label(divs,text=" ").grid(row=1,column=1,rowspan=10)

for i in range(2,6):#TO CREATE SPACE BETWEEN ROWS
    Label(divs,text=' ').grid(row=i,column=0)
Label(divs,text="Name : Rishi Singh",font="Arial 20 bold",fg="Blue").grid(row=6,column=0)#INSIDE MAIN

#Label(divs,text=" ").grid(row=2,column=0)


Label(divs,text=' ').grid(row=7,column=0)#TO CREATE SPACE BETWEEN ROWS
Label(divs,text=' ').grid(row=8,column=0)#TO CREATE SPACE BETWEEN ROWS
Label(divs,text="Enrollment Number : 211B256",font="Arial 20 bold",fg="Blue").grid(row=9,column=0)#INSIDE MAIN

#Label(divs,text=" ").grid(row=3,column=0)

Label(divs,text=' ').grid(row=10,column=0)#TO CREATE SPACE BETWEEN ROWS
Label(divs,text=' ').grid(row=11,column=0)#TO CREATE SPACE BETWEEN ROWS
Label(divs,text="Mobile : 9303163297",font="Arial 20 bold",fg="Blue").grid(row=12,column=0)#INSIDE MAIN


for i in range(13,17):#TO CREATE SPACE BETWEEN ROWS
    Label(divs,text=' ').grid(row=i,column=0)
#Label(divs,text=" ").grid(row=4,column=0)
Label(divs,text="Submitted to : Dr.Mahesh Kumar",font="Arial 25 bold",fg="Red",bg="Light Blue").grid(row=17,column=0)#INSIDE MAIN

#Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text="Project Based Learning",font="Arial 20 bold",fg="Red").grid(row=18,column=0)#INSIDE MAIN


def destroy(e=0):
    divs.destroy()
    import HOME
divs.bind("<Key>",destroy)

divs.mainloop()
