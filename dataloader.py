import sys
import MySQLdb

#this is the line to connect MySQL
db=MySQLdb.connect(host="localhost",user="root", passwd="Chemistry", db="Sales")

#you must create a cursor object. It will let you execute all the queries you need.

cur=db.cursor()

cur.execute("select * from info")

for row in cur.fetchall():
	print row

f=open("data.csv","r")

for line in f:
	line=line.strip('\n').strip('\r')
	entry=line.split(',')
	print entry