import sys

f=open("Data.csv","r")
runningbalance=0
linecounter=0

for line in f:
	if linecounter !=0:
		line=line.strip("\r").strip("\n")
		entry=line.split(",")
		runningbalance += int(entry[4])
	linecounter +=1
print runningbalance
f.close