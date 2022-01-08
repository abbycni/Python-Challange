#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[10]:


# Path to collect data from the Resources folder
Pybank_csv = os.path.join('Resources', 'budget_data.csv')
with open(Pybank_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",")
    
    # read the header row first (skip this part if there is no longer header)
    cvs_header= next(csv_file)
    print(f"Header: {cvs_header}")
    
#  Calculate Print the total number of months     
    all_data = list(csv_reader)
    numberofmonths= len(all_data)
    
print("The total number of months is "+ str(numberofmonths))   

# Calculate and Print the sum of net profit ( sum of Row [1])
total=0
diff=[]
months=[]

for row in all_data:
    total += int(row[1])
    months.append (row[0])
    


    
print("The total net profit is $" + str(total)) 


# Calculate the net change for per month second month- previous month

sumdiff = 0

for row in range(numberofmonths-1):
    diff.append (int(all_data[row+1][1])-int(all_data[row][1]))
    
maxdiff=diff[0]
maxmonth=0

mindiff=diff[0]
minmonth=0

#Calculate the minimum and maximum difference 
for i in range(len(diff)):
    if diff[i] > maxdiff:
        maxdiff = diff[i]
        maxmonth = i
    if diff[i] < mindiff:
        mindiff = diff[i]
        minmonth = i
        
#Calculate the average difference
sumdiff = sum(diff)    
average = sumdiff/(numberofmonths-1)
print("The average difference for months $" + str(average))

print("The greatest increase in profits is " + months[maxmonth+1] + " ($" + str(maxdiff) + ")")
print("The greatest decrease in profits is " + months[minmonth+1] + " ($" + str(mindiff) + ")")



    
    # write data in a file.
file1 = open("myfile2.txt","w")
file1.write("Financial Analysis\n")
file1.writelines(["The total number of months is "+ str(numberofmonths)]) 
file1.write(" \n")
file1.writelines(["The total net profit is $" + str(total)])
file1.write(" \n")
file1.writelines(["The average difference for months $" + str(average)])
file1.write(" \n")   
file1.writelines (["The greatest increase in profits is " + months[maxmonth+1] + " ($" + str(maxdiff) + ")"])
file1.write(" \n") 
file1.writelines  (["The greatest decrease in profits is " + months[minmonth+1] + " ($" + str(mindiff) + ")"])

  

  
file1.close() #to change file access modes




# In[ ]:


9

