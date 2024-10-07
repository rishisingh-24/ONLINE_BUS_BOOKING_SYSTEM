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
divs.title("ADD BUS")
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
Label(divs,text="Add Bus Details",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=14)

#DETAILS
Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text=" ").grid(row=6,column=0)

Label(divs,text="Bus id : ",font="Arial 15 bold").grid(row=7,column=0)
B_ID=Entry(divs,font="Arial 14 bold",width=7)
B_ID.grid(row=7,column=1)

Label(divs,text="Bus Type : ",font="Arial 15 bold").grid(row=7,column=2)




#ADDING OPTIONS
bus_type=StringVar()
bus_type.set("Bus Type")
Option=['AC 2X2','AC 3X2','NON AC 2X2','NON AC 3X2','AC-SLEPPER 2X1','NON-AC SLEPPER 2X1']
o=OptionMenu(divs,bus_type,*Option)
o.config(font="Arial 12 bold")
o["menu"].config(bg="sky blue")
o.grid(row=7,column=3)

Label(divs,text="Capacity : ",font="Arial 15 bold").grid(row=7,column=4)
capa=Entry(divs,font="Arial 14 bold",width=10)
capa.grid(row=7,column=5)

Label(divs,text="Fare Rs : ",font="Arial 15 bold").grid(row=7,column=6)
fare=Entry(divs,font="Arial 14 bold",width=10)
fare.grid(row=7,column=7)

Label(divs,text="Operator id : ",font="Arial 15 bold").grid(row=7,column=8)
O_ID=Entry(divs,font="Arial 14  bold",width=6)
O_ID.grid(row=7,column=9)

Label(divs,text="Route id : ",font="Arial 15 bold").grid(row=7,column=10)
R_ID=Entry(divs,font="Arial 14  bold",width=6)
R_ID.grid(row=7,column=11)



#WHEN ADD BUS IS CLICKED
def Addbus():
    b=B_ID.get()
    ty=bus_type.get()
    r=R_ID.get()
    oid=O_ID.get()
    f=fare.get()
    c=capa.get()
    if(len(b)==0 or len(oid)==0 or len(r)==0 or len(f)==0 or len(ty)==0 or len(c)==0):
        showerror("INCOMPLETE","You have not filled all fields")

    else:
        cur.execute("select * from bus")
        bus_catch=cur.fetchall()
        for i in range(len(bus_catch)):
            if(int(b)==bus_catch[i][0]):
                showerror("DUPLICATE DATA","Data Already Exists.....")
                return 1

        
        cur.execute("insert into bus (bus_id,bus_type,bus_operator_id,bus_capacity,bus_fare,bus_route_id) values (?,?,?,?,?,?)",(b,ty,oid,c,f,r))
        cur.execute("select * from bus where bus_id=(?)",(b,))
        catch=cur.fetchall()
        Label(divs,text=str(catch[0][0])+', '+str(catch[0][1])+', '+str(catch[0][3])+', '+str(catch[0][4])+', '+str(catch[0][2])+', '+str(catch[0][5]),font="Arial 12 bold",fg='gray64').grid(row=9,column=0,columnspan=13)
        showinfo ("Bus Entry","Bus Added Successfully...")

        con.commit()



    Label(divs,text=" ").grid(row=10,column=0)
    Label(divs,text=" ").grid(row=11,column=0)
    
#WHEN EDIT BUS IS CLICKED
def Editbus():
    b=B_ID.get()
    ty=bus_type.get()
    r=R_ID.get()
    oid=O_ID.get()
    f=fare.get()
    c=capa.get()

    if(len(b)==0 or len(oid)==0 or len(r)==0 or len(f)==0 or len(ty)==0 or len(c)==0):
        showerror("INCOMPLETE","You have not filled all fields")
    else:
        cur.execute("select * from bus")
        bus=cur.fetchall()
        for i in range(len(bus)):
            if(int(b)!=bus[i][0]):
                showerror("NOT EXISTS","Data Does Not Exists.....")
                return 1
            else:
                cur.execute("update bus set bus_id=(?),bus_type=(?),bus_operator_id=(?),bus_capacity=(?),bus_fare=(?),bus_route_id=(?) where bus_id=(?)",(b,ty,oid,c,f,r,b))
                cur.execute("select * from bus where bus_id=(?)",b)
                catch=cur.fetchall()
                Label(divs,text=str(catch[0][0])+','+str(catch[0][1])+', '+str(catch[0][3])+', '+str(catch[0][4])+', '+str(catch[0][2])+', '+str(catch[0][5]),font="Arial 12 bold",fg='gray64').grid(row=9,column=0,columnspan=13)
                showinfo ("Bus Entry Update ","Bus  Updated Successfully...")
                return 1

        con.commit()
        


    Label(divs,text=" ").grid(row=10,column=0)
    Label(divs,text=" ").grid(row=11,column=0)
        
#TO CREATE SPACE BETWEEN ROWS
Label(divs,text=" ").grid(row=8,column=0)

#BUTTONS

Button(divs,text="Add Bus ",font="arial 0 bold",bg="Light Green",command=Addbus).grid(row=12,column=6)
Button(divs,text="Edit Bus",font="arial  0 bold",bg="Light Green",command=Editbus).grid(row=12,column=7)

#BUTTON TO GO TO HOME PAGE
def destroy():
    con.close()
    divs.destroy()
    import DATABASE_DETAIL


img_1=PhotoImage(file='.\\home.png')
Button(divs,image=img_1,command=destroy).grid(row=12,column=8)




divs.mainloop()
