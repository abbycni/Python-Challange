The following is a Readme file for the Python PyPoll Exercise. We were tasked with 
analyzing the data in the source file and perforning some calculations to report out to 
a text file. The first step was to have the system read the file, calculate the total 
number of votes, find the candidates names and determine how many votes each one got.
The last step was to declare a winner. Which in this case was Khan.


1. Readd input CSV file 
2. Calculate the total number of votes using the len function to read the whole file 
    all_data = list(csv_reader)
    total_vote= len(all_data)  
3. Find the unique candidates names 
4. calculate the number of votes per candidate
5. Calculate the percentage vote per candidate 
    percentage_votes[name]= votes[name]/total_vote*100
6. Print all results to screen
    print(key + ":   " +str(percentage_votes[key]) + "%  "+ "("+str(votes[key])+")")
7. print all data formated and write to a text file. 

The result file looks as follows:

Election results
Khan:   63.00001050837531%  (2218231)
Correy:   19.999994319797125%  (704200)
Li:   13.999996023857989%  (492940)
O'Tooley:   2.999999147969569%  (105630)
Winner:  Khan

