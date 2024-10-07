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




        
                                                     #WINDOW CONFIGURE
divs=Tk()
h,w=divs.winfo_screenheight(),divs.winfo_screenwidth()
divs.geometry('%dx%d'%(w,h))
divs.title("BOOKING")


img_1=PhotoImage(file='.\\Bus_for_project.png')
Label(divs,image=img_1).grid(row=0,column=0,padx=w//2.5,columnspan=11)


Label(divs,text="Online Bus Booking System",font="Arial 30 bold",fg="red",bg="Light Blue",relief="ridge").grid(row=1,column=0,columnspan=11)#IN BOOKING GUI


Label(divs,text=" ").grid(row=2,column=0)# TO CREATE SPACE BETWEEN ROWS
Label(divs,text=" ").grid(row=3,column=0)# TO CREATE SPACE BETWEEN ROWS
Label(text="Enter Journey Details",font="Arial 20 bold",fg="Green",bg="Light Green",relief="ridge").grid(row=4,column=0,columnspan=11)



Label(divs,text=" ").grid(row=5,column=0)# TO CREATE SPACE BETWEEN ROWS
Label(divs,text="From : ",font="Arial 15 bold").grid(row=6,column=0)#IN BOOKING GUI
From=Entry(divs,font="Arial 15 bold",width=15)#DESTINATION POINT
From.grid(row=6,column=1)
Label(divs,text="Example: ayodhya",font="Arial 10 bold",fg="gray64").grid(row=7,column=1)


Label(divs,text="To : ",font="Arial 15 bold").grid(row=6,column=2)#JOURNEY STARTING POINT
To=Entry(divs,font="Arial 15 bold",width=15)
To.grid(row=6,column=3)
Label(divs,text="Example: guna",font="Arial 10 bold",fg="gray64").grid(row=7,column=3)



Label(divs,text="Journey Date : ",font="Arial 15 bold").grid(row=6,column=4)#JOURNEY DATE
Date=Entry(divs,font="Arial 15 bold",width=15)
Date.grid(row=6,column=5)
Label(divs,text="Example: YYYY/MM/DD",font="Arial 10 bold",fg="gray64").grid(row=7,column=5)



             
#SHOWING BUS ACCORDING TO SEARCH
def show_bus():
    T=To.get()
    F=From.get()
    D=Date.get()
    if(len(T)==0 or len(F)==0 or len(D)==0):
        showerror('INCOMPLETE','YOU HAVE NOT FILLED ALL FIELDS')
    else:
        if(T==F):
            showerror("SAME ENTRY","Starting and Ending station are same....")
            
        cur.execute("select distinct(route_id) from route_run_seat where station_name=(?)",(T,))
        T_check=cur.fetchall()
        cur.execute("select distinct(route_id) from route_run_seat where station_name=(?)",(F,))
        F_check=cur.fetchall()
        if(len(T_check)==0 or len(F_check)==0):
            showerror("BUS FINDING ERROR","The bus in this route does not exits.....")#ASSUMING IF THERE IS AN ROUTE THERE SHOULD BE AN BUS
            return 1


        
                                                            #DATABASE_USE_IN_BOOKING


        
        cur.execute("select distinct(route_id) from route_run_seat where station_name=(?) or station_name=(?)",(F,T))
        route_id=cur.fetchall()
        for i in range(len(route_id)):
            a=route_id[i][0]
            cur.execute("select distinct(station_id) from route_run_seat where station_name=(?) and route_id=(?)",(F,a))
            id_1=cur.fetchall()
            cur.execute("select distinct(station_id) from route_run_seat where station_name=(?) and route_id=(?)",(T,a))
            id_2=cur.fetchall()
            if(id_1[0][0]<id_2[0][0]):
                id_1_1=id_1[0][0]
                id_2_2=id_2[0][0]
                cur.execute("select distinct(bus_id) from bus , route_run_seat where (?)=bus_route_id",(a,))
                select_bus_id=cur.fetchall()
        count=0
        bus=0
        Label(divs,text=" ").grid(row=10,column=0)
        bus_select=IntVar()
        bus_select.set(0)
        for i in range(len(select_bus_id)): #ASSUMING ONE ROUTE CAN HAVE MULTIPLE BUSES BUT ONE BUS CANNOT BE ON MULTIPLE ROUTES AND AT ONE DATE THERE IS ONLY ONE BUS AT PERTICULAR ROUTE 
            b=select_bus_id[i][0]
            cur.execute("select distinct(run_date) from route_run_seat where route_bus_id=(?)",(b,))
            select_date=cur.fetchall()
            if(select_date[0][0]==D):
                bus+=1
                Radiobutton(divs,text='BUS'+' '+str(bus),variable=bus_select,value=b,font='Arial 12',bg='light green',indicator=0).grid(row=9+count,column=0)
                
                cur.execute("select operator_name from operator,bus where bus_id=(?) and bus_operator_id=operator_id",(b,))
                detail_operator=cur.fetchall()
                Label(divs,text=detail_operator[0][0],font="Arial 12 bold",fg='tomato').grid(row=9+count,column=1)
                
                cur.execute("select bus_type from bus where bus_id=(?)",(b,))
                detail_type=cur.fetchall()
                Label(divs,text=detail_type[0][0],font="Arial 12 bold",fg='tomato').grid(row=9+count,column=2)
                
                cur.execute("select route_seat from route_run_seat where route_bus_id=(?) and station_name=(?)",(b,F))
                detail_seat=cur.fetchall()
                cur.execute("select bus_capacity from bus where bus_id=(?)",(b,))
                detail_capacity=cur.fetchall()
                Label(divs,text=str(detail_seat[0][0])+'/'+str(detail_capacity[0][0]),font="Arial 12 bold",fg='tomato').grid(row=9+count,column=3)

                cur.execute("select bus_fare from bus where bus_id=(?)",(b,))
                detail_fare=cur.fetchall()
                Label(divs,text=detail_fare[0][0],font="Arial 12 bold",fg='tomato').grid(row=9+count,column=4)


#------------------------------------------------------------------------------------------------------------------------------------------------------------

                #DETAILS OF PASSENGER
                def Book():
                    seat=0
                    value=bus_select.get()
                    #CONDITION TO CHECK IF BUS IS SELECTED OR NOT
                    if(value==0):
                        showerror("NOT SELECTED","Select bus to book.......")
                        return(1)                    
                    Label(divs,text=" ").grid(row=12,column=0)
                    Label(divs,text="Fill The Passenger Details TO Book The Bus Ticket",font="Arial 20 bold",fg="red",bg="Light Blue",relief="ridge").grid(row=13,column=0,columnspan=11)

                    Label(text=" ").grid(row=14,column=0)
                    Label(divs,text="Name : ",font="Arial 15 bold").grid(row=15,column=0)
                    Name=Entry(divs,font="Arial 15 bold",width=15)
                    Name.grid(row=15 ,column=1)

                    Label(divs,text="Gender : ",font="Arial 15 bold").grid(row=15,column=2)
                    gender=StringVar()
                    gender.set("GENDER")
                    Option=["Male","Female","Transgender"]
                    g=OptionMenu(divs,gender,*Option)
                    g.config(font="Arial 11 bold")
                    g.grid(row=15,column=3)

                    Label(divs,text="No.of seats : ",font="Arial 15 bold").grid(row=15,column=4)
                    seats=Entry(divs,font="Arial 15 bold",width=8)
                    seats.grid(row=15 ,column=5)
                    
                    Label(divs,text="Mobile Number : ",font="Arial 15 bold").grid(row=15,column=6)
                    num=Entry(divs,font="Arial 15 bold",width=15)
                    num.grid(row=15 ,column=7)
            
                    Label(divs,text="Age : ",font="Arial 15 bold").grid(row=15,column=8)
                    age=Entry(divs,font="Arial 15 bold",width=5)
                    age.grid(row=15 ,column=9)

                    

#--------------------------------------------------------------------------------------------------------------------------------------------------------            
                                                                #TICKET INSERTION
                    #SEAT CONFIRMATION
                    def seat():
                        na=Name.get()
                        g=gender.get()
                        nu=num.get()
                        s=seats.get()
                        a=age.get()
                        total_fare=(detail_fare[0][0])*(int(s))
                        cur.execute("select operator_name from bus , operator where bus_id=(?) and operator_id=bus_operator_id",(value,))
                        operator_detail=cur.fetchall()  
                        if(len(na)==0 or len(g)==0 or len(s)==0 or len(nu)==0 or len(a)==0):
                            showerror('INCOMPLETE','YOU HAVE NOT FILLED ALL FIELDS')
                        else:
                            QUE=askyesno('FARE CONFIRM',("Total Amount To Be Paid is Rs. ",total_fare))
                                    
                            if(QUE):
                                cur.execute("insert into booking (passen_bus,passen_age,passen_gender,passen_name,passen_seat,passen_fare,passen_from,passen_to,passen_date,passen_phone) values(?,?,?,?,?,?,?,?,?,?)",(operator_detail[0][0],a,g,na,s,total_fare,F,T,D,nu))
                                if(id_1_1!=1):
                                    cur.execute("update route_run_seat set route_seat=route_seat-(?) where station_id=1 and route_bus_id=(?)",(s,value))
                                    a=id_1_1
 
                                    c=id_2_2
 
                                    for i in range(a+1,c):
                                        cur.execute("update  route_run_seat set route_seat=route_seat-(?) where station_id=(?) and route_bus_id=(?)",(s,i,value))
                                else:
                                    a=id_1_1

                                    c=id_2_2
 
                                    for i in range(a,c):
                                        cur.execute("update route_run_seat set route_seat=route_seat-(?) where station_id=(?) and route_bus_id=(?)",(s,i,value))


                                con.commit()
                                con.close()
                                divs.destroy()
                                import TICKET                                
                                '''CONNECT TO TICKET GUI'''
                            else:
                                return(1)

                                
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                    #BUTTON FOR BOOK
                    Label(text=" ").grid(row=16,column=0)
                    Button(divs,text="Book Seat",command=seat,font="Arial 15 bold",bg="Light Green").grid(row=17,column=6)

                
#------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                if(detail_seat!=0):
                    Button(divs,text="Proceed to Book ",command=Book,font="Arial 12 bold",bg="Light Green").grid(row=9+count,column=6)
                    
                count+=2
        if(count==0):
            showerror("NO BUS FOUND","There is no bus running for this route at this date......")
            return(1)
        #Label(divs,text=select_bus).grid(row=9,column=0)
                 
        Label(divs,text="Select Bus ",font="Arial 15 bold",fg="Green").grid(row=8,column=0)
        Label(divs,text="Operator ",font="Arial 15 bold",fg="Green").grid(row=8,column=1)
        Label(divs,text="Bus type ",font="Arial 15 bold",fg="Green").grid(row=8,column=2)
        Label(divs,text="Available/Capacity ",font="Arial 15 bold",fg="Green").grid(row=8,column=3)
        Label(divs,text="Fare ",font="Arial 15 bold",fg="Green").grid(row=8,column=4)
        

                        
        
            

#BUTTIONS
Button(divs,text="Show Bus",font="Arial 15 bold",bg="Light Green",command=show_bus).grid(row=6,column=6)#BUTTON TO SHOW THE BUS DETAILS AND CONNECT TO DATABASE
Label(divs,text=" ").grid(row=7,column=0)#TO CREATE SPACE BETWEEN ROWS

def destroy():
    divs.destroy()
    import HOME

img_2=PhotoImage(file='.\\home.png')
Button(divs,image=img_2,command=destroy).grid(row=6,column=7)# TO GIVE HOME BUTTON THAT CONNECT TO HOME GUI


#ROW 9 TO 12 IS FOR INFORMATIONA AND SPACE



for i in range(8,12):
    Label(text=" ").grid(row=6,column=i)


divs.mainloop()


