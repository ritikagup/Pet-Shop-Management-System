import pymysql as ps
mydb = ps.connect(host = "localhost", user="root", passwd="Ritika2003")
mydb

mycur = mydb.cursor()
mycur.execute("use mydb")

mycur.execute("create table PET if not exists(id int primary key, type varchar(10) not null, breed varchar(20), colour varchar(20), \
               age decimal(5,2), height decimal(5,2), price decimal(8,2), gender varchar(1), avail varchar(1) default 'Y' ) ")

mycur.execute("describe pet")

for i in mycur:
    print(i)
