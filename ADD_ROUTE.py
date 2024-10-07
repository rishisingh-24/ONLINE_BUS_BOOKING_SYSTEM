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
divs.title("ADD ROUTE")
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()#SET GUI TO SCREEN SIZE
divs.geometry('%dx%d'%(w,h))


#ADD BUS IMAGE
img=PhotoImage(file='.\\Bus_for_project.png')
Label(divs,image=img).grid(row=0,column=0,columnspan=14,padx=w//2.5)


#ONLINE BUS BOOKING SYSTEM
Label(divs,text="Online Bus Booking System",relief="ridge",font="Arial 30 bold",fg="Red",bg="Light Blue").grid(row=1,column=0,columnspan=14)


#CREATE SPACE
Label(divs,text=" ").grid(row=2,column=0)
Label(divs,text=" ").grid(row=3,column=0)
Label(divs,text="Add Bus Route Details",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=14)

#DETAILS
Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text=" ").grid(row=6,column=0)
Label(divs,text=" ").grid(row=7,column=0)
Label(divs,text="Route Id: ",font="Arial 15 bold").grid(row=7,column=1)
R_ID=Entry(divs,font="Arial 15 bold",width=15)
R_ID.grid(row=7,column=2)

Label(divs,text="Station From : ",font="Arial 15 bold").grid(row=7,column=3)
S_F=Entry(divs,font="Arial 15 bold",width=15)
S_F.grid(row=7,column=4)

Label(divs,text="Station To : ",font="Arial 15 bold").grid(row=7,column=5)
S_T=Entry(divs,font="Arial 15  bold",width=15)
S_T.grid(row=7,column=6)


Label(divs,text="Station Id From : ",font="Arial 15 bold").grid(row=7,column=7)
S_ID=Entry(divs,font="Arial 15 bold",width=15)
S_ID.grid(row=7,column=8)

Label(divs,text="Station Id To : ",font="Arial 15 bold").grid(row=7,column=9)
S_ID_2=Entry(divs,font="Arial 15 bold",width=15)
S_ID_2.grid(row=7,column=10)



Label(divs,text="Example - 1,2,3,4....",font="Arail 10 bold",fg='gray64').grid(row=8,column=2)
Label(divs,text="Example - station",font="Arail 10 bold",fg='gray64').grid(row=8,column=4)
Label(divs,text="Example - 1,2,3,4....",font="Arail 10 bold",fg='gray64').grid(row=8,column=8)
Label(divs,text="Example - station",font="Arail 10 bold",fg='gray64').grid(row=8,column=6)
Label(divs,text="Example - 1,2,3,4....",font="Arail 10 bold",fg='gray64').grid(row=8,column=10)


#WHEN ADD BUS IS CLICKED
def Add_route():
    r=R_ID.get()
    s_f=S_F.get()
    s_t=S_T.get()
    s_id=S_ID.get()
    s_id_2=S_ID_2.get()
    if(len(s_t)==0 or len(r)==0 or len(s_id)==0 or len(s_id_2)==0 or len(s_f)==0):
        showerror("INCOMPLETE","You have not filled all fields")

    else:
        cur.execute("select distinct route_id from route_run_seat")
        catch=cur.fetchall()
        count=0
        for i in range(len(catch)):
            if(int(r) in catch[i]):
                count+=1
        if(count==0):
            showerror("DUPLICATE DATA","This route already exists....")
        else:
            cur.select("insert into route_run_seat (route_id,station_id,station_From) values(?,?,?)",(r,s_id,s_t))
            cur.select("insert into route_run_seat (route_id,station_id,station_To) values(?,?,?)",(r,s_id_2,s_t))
            Label(divs,text=r+', '+s_f+', '+s_id+', '+s_t+','+s_id_2,font="Arial 12 bold",fg='gray64').grid(row=10,column=0,columnspan=14)
            Label(divs,text=" ").grid(row=11,column=0)
            con.commit()
            showinfo("Route Insertion","Route Record Added Successfully....")

    
#WHEN EDIT BUS IS CLICKED
def Delete_route():
    r=R_ID.get()
    s_f=S_F.get()
    s_t=S_T.get()
    s_id=S_ID.get()
    s_id_2=S_ID_2.get()
    if(len(s_t)==0 or len(r)==0 or len(s_id)==0 or len(s_id_2)==0 or len(s_f)==0):
        showerror("INCOMPLETE","You have not filled all fields")
    else:
        Label(divs,text=" ").grid(row=11,column=0)
        '''if(DATA DOES EXIT)'''
        '''SHOW DATA IN ROW 9'''
        showinfo ("Route Deletion","Route Record Deleted Successfully...")
        
        '''if(DATA DOES NOT  EXIT)'''
        '''showerror("Route Deletion Error ","Route Record Does not exists....")'''



#BUTTONS
Button(divs,text="Add Route",font="arial 0 bold",bg="Light Green",command=Add_route).grid(row=12,column=6)
Button(divs,text="Delete Route",font="arial  0 bold",bg="Light Green",command=Delete_route).grid(row=12,column=7)

 
#BUTTON TO GO TO HOME PAGE

def destroy():
    con.close()
    divs.destroy()
    import DATABASE_DETAIL


img_1=PhotoImage(file='.\\home.png')
Button(divs,image=img_1,command=destroy).grid(row=12,column=8)




divs.mainloop()
