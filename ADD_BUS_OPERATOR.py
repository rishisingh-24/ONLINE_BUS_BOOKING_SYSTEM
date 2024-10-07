try:
    from tkinter import *
    from tkinter.messagebox import *
except:
    from Tkinter import *
    from TKinter.messagebox import *


                                                # CREATING DATABASE
import sqlite3

con=sqlite3.Connection("PROJECT")
cur=con.cursor()



    

                                                #WINDOWS CONFIGURE
divs=Tk()
divs.title("ADD OPERATOR")
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()#SET GUI TO SCREEN SIZE
divs.geometry('%dx%d'%(w,h))


#ADD BUS IMAGE
img=PhotoImage(file='.\\Bus_for_project.png')
Label(divs,image=img).grid(row=0,column=0,columnspan=13,padx=w//2.5)


#ONLINE BUS BOOKING SYSTEM
Label(divs,text="Online Bus Booking System",relief="ridge",font="Arial 30 bold",fg="Red",bg="Light Blue").grid(row=1,column=0,columnspan=13)


#CREATE SPACE
Label(divs,text=" ").grid(row=2,column=0)
Label(divs,text=" ").grid(row=3,column=0)
Label(divs,text="Add new details to database",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=13)

#DETAILS
Label(divs,text=" ").grid(row=5,column=0)
Label(divs,text=" ").grid(row=6,column=0)

Label(divs,text="Operator id : ",font="Arial 15 bold").grid(row=7,column=0)
O_ID=Entry(divs,font="Arial 15 bold",width=5)
O_ID.grid(row=7,column=1)

Label(divs,text="Name : ",font="Arial 15 bold").grid(row=7,column=2)
name=Entry(divs,font="Arial 15 bold",width=14)
name.grid(row=7,column=3)

Label(divs,text="Address : ",font="Arial 15 bold").grid(row=7,column=4)
addr=Entry(divs,font="Arial 15 bold",width=14)
addr.grid(row=7,column=5)

Label(divs,text="Phone : ",font="Arial 15 bold").grid(row=7,column=6)
phone=Entry(divs,font="Arial 15 bold",width=13)
phone.grid(row=7,column=7)

Label(divs,text="Email : ",font="Arial 15 bold").grid(row=7,column=8)
email=Entry(divs,font="Arial 15  bold")
email.grid(row=7,column=9)



#WHEN ADD BUTTON CLICKED
def add():
    o=O_ID.get()
    na=name.get()
    a=addr.get()
    p=phone.get()
    e=email.get()
    if(len(o)==0 or len(na)==0 or len(a)==0 or len(p)==0 or len(e)==0):
        showerror("INCOMPLETE","You have not filled all fields")
    else:
        Label(divs,text=" ").grid(row=9,column=0)
        Label(divs,text=" ").grid(row=10,column=0)

        cur.execute("select * from operator")
        operator=cur.fetchall()
        for i in range(len(operator)):
            if(int(o)==operator[i][0] or na==operator[i][1] or e==operator[i][3] or int(p)==operator[i][4]):
                showerror("DUPLICATE DATA","Data Already Exists.....")
                return 1
        
        cur.execute("insert into operator (operator_id,operator_name,operator_address,operator_email,operator_phone) values (?,?,?,?,?)",(o,na,a,e,p))
        cur.execute("select * from operator where operator_id=(?)",o)
        catch=cur.fetchall()
        Label(divs,text=catch[0],font="Arial 12 bold",fg='gray64').grid(row=11,column=0,columnspan=13)
        showinfo ("Operator Entry","Operator Added Successfully...")

        con.commit()


#WHEN EDIT BUTTON CLICKED        
def edit():
    o=(O_ID.get())
    na=name.get()
    a=addr.get()
    p=phone.get()
    e=email.get()
    if(len((o))==0 or len(na)==0 or len(a)==0 or len(p)==0 or len(e)==0):
        showerror("INCOMPLETE","You have not filled all fields")
    else:
        Label(divs,text=" ").grid(row=9,column=0)
        Label(divs,text=" ").grid(row=10,column=0)
        cur.execute("select * from operator")
        operator=cur.fetchall()
        for i in range(len(operator)):
            if(int(o)!=operator[i][0]):
                showerror("NOT EXISTS","Data Does Not Exists.....")
                return 1
            else:
                cur.execute("update operator set operator_id=(?),operator_name=(?),operator_address=(?),operator_email=(?),operator_phone=(?) where operator_id=(?)",(o,na,a,e,p,o))
                cur.execute("select * from operator where operator_id=(?)",b)
                catch=cur.fetchall()
                Label(divs,text=catch[0],font="Arial 12 bold",fg='gray64').grid(row=11,column=0,columnspan=13)
                return 1
        showinfo ("Operator Entry Uodate ","Operator Updated Successfully...")

        con.commit()
        
#BUTTONS

Button(divs,text="Add",font="arial 15 bold",bg="Light Green",command=add).grid(row=7,column=10)
Button(divs,text="Edit",font="arial 15 bold",bg="Light Green",command=edit).grid(row=7,column=11)




#BUTTON TO GO TO HOME PAGE
def destroy():
    con.close()
    divs.destroy()
    import HOME
    
Label(divs,text=" ").grid(row=8,column=0)
img_1=PhotoImage(file='.\\home.png')
Button(divs,image=img_1,command=destroy).grid(row=12,column=11)
