import sqlite3

con=sqlite3.Connection("PROJECT")
cur=con.cursor()

cur.execute('create table if not exists operator  (operator_id numeric,operator_name varchar(30),operator_address varchar(30),operator_email varchar(30),operator_phone numeric)')
cur.execute("create table if not exists bus (bus_id numeric,bus_type varchar(10),bus_capacity numeric,bus_fare numeric,bus_operator_id numeric,bus_route_id numeric)")
cur.execute("create table if not exists booking  (passen_name varchar(25),passen_seat numeric,passen_fare numeric,passen_from varchar(25),passen_to varchar(25),passen_date date,passen_phone numeric,passen_gender varchar(20),passen_age numeric,passen_bus varchar(10))")
cur.execute("create table if not exists route_run_seat(route_id numeric,route_bus_id numeric,station_name varchar(25),station_id numeric,run_date varchar(20),route_seat numeric)")






cur.execute("insert into operator (operator_id,operator_name,operator_address,operator_email,operator_phone) values (1,'ryan','guna','ryan@gmail.com',9988776655)")
cur.execute("insert into operator (operator_id,operator_name,operator_address,operator_email,operator_phone) values (2,'kamla','bhopal','kamla@gmail.com',9262855965)")





cur.execute("insert into bus (bus_id,bus_type,bus_operator_id,bus_capacity,bus_fare,bus_route_id) values (1,'4x4 ac',1,100,1500,1)")
cur.execute("insert into bus (bus_id,bus_type,bus_operator_id,bus_capacity,bus_fare,bus_route_id) values (2,'2x2 non ac',1,50,500,2)")
cur.execute("insert into bus (bus_id,bus_type,bus_operator_id,bus_capacity,bus_fare,bus_route_id) values (3,'4x4 ac',2,60,600,1)")
cur.execute("insert into bus (bus_id,bus_type,bus_operator_id,bus_capacity,bus_fare,bus_route_id) values (4,'2x2 non ac',2,30,300,2)")




#BUSES PROVIDED BY OPERAOTOR 1 ON BOTH ROUTE(GUNA TO BHOPAL AND BHOPAL TO GUNA)
cur.execute("insert into route_run_seat values(1,1,'guna',1,'2022/11/30',100)")
cur.execute("insert into route_run_seat values(1,1,'jaypee',2,'2022/11/30',100)")
cur.execute("insert into route_run_seat values(1,1,'byawra',3,'2022/11/30',100)")
cur.execute("insert into route_run_seat values(1,1,'bhopal',4,'2022/11/30',0)")
cur.execute("insert into route_run_seat values(2,2,'bhopal',1,'2022/11/25',50)")
cur.execute("insert into route_run_seat values(2,2,'byawra',2,'2022/11/25',50)")
cur.execute("insert into route_run_seat values(2,2,'jaypeee',3,'2022/11/25',50)")
cur.execute("insert into route_run_seat values(2,2,'guna',4,'2022/11/25',0)")


#BUS PROVIDED BY OPERATOR 2 ON BOTH ROUTE(GUNA TO BHOPAL AND BHOPAL TO GUNA)

cur.execute("insert into route_run_seat values(1,3,'guna',1,'2022/12/01',60)")
cur.execute("insert into route_run_seat values(1,3,'japyee',2,'2022/12/01',60)")
cur.execute("insert into route_run_seat values(1,3,'byawra',3,'2022/12/01',60)")
cur.execute("insert into route_run_seat values(1,3,'bhopal',4,'2022/12/01',0)")
cur.execute("insert into route_run_seat values(2,4,'bhopal',1,'2022/11/25',30)")
cur.execute("insert into route_run_seat values(2,4,'byawra',2,'2022/11/25',30)")
cur.execute("insert into route_run_seat values(2,4,'jaypee',3,'2022/11/25',30)")
cur.execute("insert into route_run_seat values(2,4,'guna',4,'2022/11/25',0)")

con.commit()
con.close()

'''
F='guna'
T='jaypee'
id_1=1
id_2=2
b=1
s=10
if(id_1!=1):
    cur.execute("update route_run_seat set route_seat=route_seat-(?) where station_id=1 and route_bus_id=(?)",(s,b))
    for i in range(id_1+1,id_2):
        cur.execute("update  route_run_seat set route_seat=route_seat-(?) where station_id=(?)",(s,i))
else:    
    for i in range(id_1,id_2):
        cur.execute("update  route_run_seat set route_seat=route_seat-(?) where station_id=(?)",(s,i))

cur.execute("select * from route_run_seat")
catch=cur.fetchall()
print(catch)
'''

'''
cur.execute("delete from booking where passen_phone=9340790169")
cur.execute("select * from booking")
catch=cur.fetchall()
print(catch)
'''


'''
cur.execute("select distinct(run_date) from route_run_seat")
catch=cur.fetchall()
print(catch)
catch_date=catch[0][0]
date='2022/11/30'
if(catch_date==date):
    print("HELLO")
else:
    print(date,catch_date)
'''

'''
cur.execute("select distinct(route_id) from route_run_seat where station_name='guna' or station_name='bhopal'")
#cur.execute("select bus_id from bus,route_run_seat where station_name='guna' and station )
catch=cur.fetchall()
#catch=[(1,),(2,)]
for i in range(len(catch)):
    a=catch[i][0]
    cur.execute("select station_id from route_run_seat where station_name='guna' and route_id=(?)",(a,))
    id_1=cur.fetchall()
    cur.execute("select station_id from route_run_seat where station_name='bhopal' and route_id=(?)",(a,))
    id_2=cur.fetchall()
    if(id_1<id_2):
        cur.execute("select distinct(bus_id) from bus , route_run_seat where (?)=bus_route_id",(a,))
        select_bus=cur.fetchall()
        print(select_bus)
print(catch)
'''
