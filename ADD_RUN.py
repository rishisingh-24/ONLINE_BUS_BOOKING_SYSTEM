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
divs.title("ADD RUN")
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
Label(divs,text="Add Bus Running Details",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=14)

#DETAILS
Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text=" ").grid(row=6,column=0)
Label(divs,text=" ").grid(row=7,column=0,padx=100)
Label(divs,text="Bus Id: ",font="Arial 15 bold").grid(row=7,column=1)
B_ID=Entry(divs,font="Arial 15 bold",width=15)
B_ID.grid(row=7,column=2)

Label(divs,text="Running Date : ",font="Arial 15 bold").grid(row=7,column=3)
R_D=Entry(divs,font="Arial 15 bold",width=15)
R_D.grid(row=7,column=4)

Label(divs,text="Seat Available : ",font="Arial 15 bold").grid(row=7,column=5)
Seat_A=Entry(divs,font="Arial 15  bold",width=15)
Seat_A.grid(row=7,column=6)

Label(divs,text="Route Id: ",font="Arial 15 bold").grid(row=7,column=7)
R_ID=Entry(divs,font="Arial 15 bold",width=15)
R_ID.grid(row=7,column=8)


Label(divs,text=' ').grid(row=8,column=0)
Label(divs,text=' ').grid(row=9,column=0)

#WHEN ADD BUS IS CLICKED
def Add_Run():
    r=R_ID.get()
    r_d=R_D.get()
    b=B_ID.get()
    s=Seat_A.get()
    if(len(r_d)==0 or len(r)==0 or len(s)==0 or len(b)==0):
        showerror("INCOMPLETE","You have not filled all fields")

    else:
        cur.execute("Select distinct(route_bus_id) from route_run_seat")
        catch_1=cur.fetchall()
        print(catch_1)
        for i in range(len(catch_1)):
            if(int(b)==catch_1[i][0]):
                showerror("DUPLICATE ERROR","This bus run already exists.....")
                return 1
            
        cur.execute("Select distinct run_date,route_id from route_run_seat")
        catch_2=cur.fetchall()
        print(catch_2)
        for i in range(len(catch_2)):
            if(r_d==catch_2[i][0] and int(r)==catch_2[i][1]):
                showerror("DUPLICATE ERROR)","This run date at this route already exists.....")
                return 1
            
        cur.execute("Select distinct(route_id) from route_run_seat")
        catch_3=cur.fetchall()
        count=0
        for i in range(len(catch_3)):
            if( int(r) in catch_3[i]):
                count+=1
        if(count==0):
            QUE=askyesno("ROUTE ERROR","This route does not exits.\nDo you want to add route")
            if(QUE):
                con.close()
                divs.destroy()
                import ADD_ROUTE
            else:
                return 1

        cur.execute("insert into route_run_seat (route_bus_id,route_id,run_date,route_seat) values(?,?,?,?)",(b,r,r_d,s))
        cur.execute("select * from route_run_seat")
        catch=cur.fetchall()
        print(catch)
        Label(divs,text=' ').grid(row=11,column=0)
        Label(divs,text=b+', '+r_d+', '+s+', '+r,font="Arial 12 bold",fg='gray64').grid(row=10,column=0,columnspan=14)
        '''SHOW DATA IN ROW 10'''
        con.commit()
        showinfo("Run Insertion","Run Record Added Successfully....")

Label(divs,text=' ').grid(row=11,column=0)
#WHEN EDIT BUS IS CLICKED
def Delete_Run():
    r=R_ID.get()
    r_d=R_D.get()
    b=B_ID.get()
    s=Seat_A.get()
    if(len(r_d)==0 or len(r)==0 or len(s)==0 or len(b)==0):
        showerror("INCOMPLETE","You have not filled all fields")

    else:            
        cur.execute("Select distinct(route_id) from route_run_seat")
        catch_3=cur.fetchall()
        count_1=0
        for i in range(len(catch_3)):
            if( int(r) in catch_3[i]):
                count_1+=1
            
        cur.execute("Select distinct(run_date) from route_run_seat")
        catch_3=cur.fetchall()
        count_2=0
        for i in range(len(catch_3)):
            if( r_d in catch_3[i]):
                count_2+=1
            
        cur.execute("Select distinct(route_seat) from route_run_seat")
        catch_3=cur.fetchall()
        count_3=0
        for i in range(len(catch_3)):
            if( int(s) in catch_3[i]):
                count_3+=1
            
        cur.execute("Select distinct(route_bus_id) from route_run_seat")
        catch_3=cur.fetchall()
        count_4=0
        for i in range(len(catch_3)):
            if( int(b) in catch_3[i]):
                count_4+=1

        if(count_1!=0 and count_2!=0 and count_3!=0 and count_4!=0):
            cur.execute("delete from route_run_seat where route_id=(?) and route_bus_id=(?) and route_seat=(?) and run_date=(?)",(r,b,s,r_d))
        else:
            showerror("NOT EXISTS","This run does not exists....")
            return 1
        con.commit()
        Label(divs,text=' ').grid(row=11,column=0)
        showinfo ("Run Deletion","Run Record Deleted Successfully...")
        

#BUTTONS
Button(divs,text="Add Run ",font="arial 0 bold",bg="Light Green",command=Add_Run).grid(row=12,column=5)
Button(divs,text="Delete Run",font="arial  0 bold",bg="Light Green",command=Delete_Run).grid(row=12,column=6)

 

#BUTTON TO GO TO HOME PAGE

def destroy():
    con.close()
    divs.destroy()
    import DATABASE_DETAIL


img_1=PhotoImage(file='.\\home.png')
Button(divs,image=img_1,command=destroy).grid(row=12,column=7)




divs.mainloop()
