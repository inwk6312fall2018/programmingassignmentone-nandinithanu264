
#open file

myfile = open("running-config.cfg")

#Variable to load values

mylist_intname=[]

#Running through file 

for line in myfile:
    #strip whitespace 
    line = line.strip()
    line = line.split()
if(line[0] == "interface"):
    mylist_intname.append(line[1])

print(mylist_intname)
