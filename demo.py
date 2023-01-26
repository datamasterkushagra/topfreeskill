import mysql.connector

mydb=mysql.connector.connect(host = "localhost",user = "root",passwd="")
if mydb.is_connected():
    print("connection success")

mycursor = mydb.cursor()
# sql= "insert into myweb(name, address) values(%s,%s)"
# val=("john","highway 21")

resultt=mycursor.execute("show databases")

# mydb.commit()

# print(mycursor.rowcount,"record inserted.")
print(resultt)
