myfile = open("running-config.cfg")
mylist_access_list=[]
mylist_manage_list=[]
for line in myfile:
 line=line.strip()
 line=line.split()
 #check for list with the required keywords and store seperately in 2 lists
 if(line[0] == 'access-list' and line[1] == 'fw-management_access_in'):
  mylist_access_list.append(line)
 if(line[0] == 'access-list' and line[1] == 'global_access'):
  mylist_manage_list.append(line)
print('GIVEN THE GLOBAL ACCESS LIST \n\n')
print(mylist_access_list) # list # 1
print('GIVEN THE FW-MANAGEMENT ACCESS LIST \n\n')
print(mylist_manage_list) # list # 2
 #
