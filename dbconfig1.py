import pymysql

#Connection Object
mydb1 = pymysql.connect(host="localhost",port=3306,user="root",database="movie")

#Cursor object
mycursor = mydb1.cursor()