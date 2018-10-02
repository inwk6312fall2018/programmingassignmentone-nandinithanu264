myfile = open("running-config.cfg")
wrfile = open("output.txt","w+") # open file in write mode
mylist_intname=[]
for line in myfile:
 line=line.strip()
 line=line.split()
 #print(line)
 #print(len(line))
 if(line[0] == 'security-level'):
  line[1]='10'
  wrfile.write(str(line[1]))
 if(len(line)>=4):#checks for the strings starting with '192' or '172' 
  if(line[2][0:3] == '192' or line[2][0:3] == '172'): #store the string after the first 3 letters
   temp_=line[2][4:]
   del line[2] #append the required prefix o the ip add.
   temp='10.'+temp_ #insert the new peice of string into the final list in the exact position
   line.insert(2,temp)#write output to final
   wrfile.write(str(line))
 wrfile.write(str(line))
 #




