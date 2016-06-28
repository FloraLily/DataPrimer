import sys

print sys.argv[1]

personname=sys.argv[1]

print "Hello " + personname

timetable = int(sys.argv[2])

for i in range(1,11):
	print str(timetable)+ " x " + str(i) + " = " + str(timetable*i)


