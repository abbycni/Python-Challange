The following is Abby Kannappan's ReadMe file for the PyBank homework in Python 3

The assignment was to take a short CSV file with banking data and import it into Python. The next step was to analyse the data and make an approach to reporting financial analaysis on the data. 
The first step was to use the Len function to count the number of months of data in the file. The answer to that was 86.

The next step sum the total net profit over all 86 months. This was done by looping through the file and summing each row. 
Step number 4 to calculate the average per month change over the entire period. This was done using the following formula to calculate the sum of the differneces divided by 85.
#Calculate the average difference
sumdiff = sum(diff)    
average = sumdiff/(numberofmonths-1)
Followed by this we calculated the greatest monthly increase in profit and the greated monthly decreasein profit. This was done using a loop to compare each row and find the minimun and maximum change. 

the results of the data were written to  a text file and are as follow:

The total number of months is 86
The total net profit is $38382578
The average difference for months $-2315.1176470588234
The greatest increase in profits is Feb-2012 ($1926159)
The greatest decrease in profits is Sep-2013 ($-2196167)

