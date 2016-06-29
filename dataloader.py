import sys
import MySQLdb

#this is the line to connect MySQL
db=MySQLdb.connect(host="localhost",user="root", passwd="Chemistry", db="Sales")

#you must create a cursor object. It will let you execute all the queries you need.

cur=db.cursor()

f=open("data.csv","r")

for line in f:
	if line.startswith('date'):
			pass
	else:
		line=line.strip('\n').strip('\r')
		entry=line.split(',')
		print entry
		query="INSERT INTO transactions(date,name,cost,paid,balance,status) values ('"+entry[0]+"','"+entry[1]+"','"+entry[2]"','"+entry[3]+"','"+entry[4]+"','"+entry[5]+"')"
		print" "

		cur.execute(query)
		db.commit()