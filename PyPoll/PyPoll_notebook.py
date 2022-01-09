#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
import csv


# In[2]:


election_csv = os.path.join( "Resources", "election_data.csv")


# In[3]:


# open the CSV file 
with open(election_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    
    # read the header row first (skip this part if there is no longer header)
    cvs_header= next(csv_file)
   
    
    #read through each row of data after the header
 #   for row in csv_reader:
    # Count the total number of votes per candidate
    
#  Calculate Print the total number of votes   
    all_data = list(csv_reader)
    total_vote= len(all_data)    
    print("The total number of votes is "+ str(total_vote))    

    Candidates=[]
    for row in all_data:
       
       
        if row[2] not in Candidates:
            Candidates.append(row[2])
           
  
votes ={}
for name in Candidates: 
    votes[name]=0
    

for name in Candidates:
   
    for row in all_data:
        if row[2]==name:
            votes[name]=votes[name]+1 


percentage_votes={}
for name in votes:

    percentage_votes[name]= votes[name]/total_vote*100
   
 


# In[5]:




print("Election results")
for key in votes:
  
    print(key + ":   " +str(percentage_votes[key]) + "%  "+ "("+str(votes[key])+")")

winner = ""    
max_vote=0
for name in votes:   
    if votes[name]>max_vote:
        winner=name
        max_vote=votes[name]
        
        
    
    #winner=(votes[name]).max()
    #print(votes[name])

print("Winner:  " +winner)
  

    
    # write data in a file.
file1 = open("myfile.txt","w")
file1.write("Election Results\n")
file1.writelines("The total number of votes is "+ str(total_vote))
file1.write(" \n")
    
  
   
for key in votes:
        file1.writelines([key + ":   " +str(percentage_votes[key]) + "%  "+ "("+str(votes[key])+")\n"])     

file1.writelines("Winner:  " + (winner))    
file1.close() #to change file access modes


# In[ ]:





# In[ ]:




