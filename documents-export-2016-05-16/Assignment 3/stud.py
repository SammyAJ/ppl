file = open(raw_input("Enter name of the file:\n"))
a = file.read()
data = a.split()
i = 0
count = 0
print "the students scoring above 70\n"
while(i < len(data)):
	if int(data[i]) > 70:
		print data[i] + " " + data[i + 1]
		count = count + 1
	i = i + 2
print "Total number of students scoring above 70:-", 
print count
print "Total number of students with unique marks:-",
i = 0
count = 0
while(i < len(data)):
	if data.count(data[i]) == 1:
		#print data[i] + " " + data[i + 1]
		count = count + 1
	i = i + 2
print count