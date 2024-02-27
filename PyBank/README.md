# Module 3 Challenge

This module comprises two challenges.  This challenge named "PyBank" presents a real-world situation in which a financial dataset called budget_data.csv is provided comprising two columns with “Date” and “Profit/Loss” headers and numerous rows. A quick review of the data reveals that the former has a mmm-yr format and the latter has an integer format where negative numbers are preceded with a minus sign.  

A challenge named "PyPoll" of the Module 3 Challenge in which a real-world situation of helping a small, rural town modernize its vote-counting process is employed may be found under the PyPoll directory.

## PyBank Instructions

As instructed, a Python script has been created (1) to analyze the records to calculate each of the following values and (2) to present the results in a format that was provided:

* The total number of months included in the dataset.

* The net amount of “Profit/Losses” over the entire period.

* The changes of “Profit/Losses” over the entire period, and then the average of those changes.

* The greatest increase in profits (date and amount) over the entire period.

* The greatest decrease in profits (date and amount) over the entire period.

As instructed, the final script (1) presents the results in a format that was provided (2) prints to the terminal, and (3) exports the results to a .txt file. 

## PyBank Solution

The script begins by importing os and csv modules so that the script interacts with the operating system and classes are implements to read and write the tabular data presented in the .csv, respectively. Prior to each row of the data being analyzed, initializations are performed.  With respect to text variables, a list named months is created to define the 12 text variables that appear in the data file.  Then, two text variables are initialized as empty strings and will be used to record the condition in which each of the greatest monthly increase and decrease is identified as the analysis of each row progresses.

Numerous numerical variables are initialized to zero and are subject change as each row is analyzed in a row loop iteration.  These variables are representative of the following:

* A count of months (or tows) rows with each row loop iteration;

* A running cumulation of total profit/loss with each row loop iteration;

* Values representative of the greatest monthly increase/decrease at the time when those conditions are identified with each row loop iteration;

* Value representative of the monthly change between successive row loop iterations; 

* Value representative of the cumulative profit/loss that is carried forward to the next row loop iteration;

* Values representative of the first month profit/loss and a flag to record that condition; and

* Value representative of the accumulative change of the profit/loss at the completion of the row loop iterations. 

After the initialization is completed, the analyan iteration begins in which each row is sequentially analyzed. Firstly, the first and second columns of each row are identified as months and profit/losses, respectively.  

Secondly, the text variable is confirmed that to be one of the 12 months in the months list.  

Thirdly, once confirmed, the count of months is increased by 1, the values of the total profit/losses value and the monthly change are increased or decreased as appropriate, and the flag value is increased by 1.  During the initial row loop iteration, the flag value becomes 1, thereby meeting the condition in which the value of the first month profit/loss is recorded so that it can be used in determining the change to profit/loss over the entire period at the end of the row loop iterations.

Fourthly, a determination of whether the monthly change is an increase (or greater than 0) or a decrease (or less than 0).  If an increase, a determination is made to see if the increase is the greatest monthly increase encountered as the row loop continues its iterations; if so, it is recorded as the greatest monthly increase and subjected to subsequent determinations of greatest monthly increases.  

Similarly, if the monthly change is a decrease, a determination is made to see if the decrease is the greatest is the greatest monthly decease encountered as the row loop continues its iterations; if so, it is recorded as the greatest monthly decrease and subjected to subsequent determinations of greatest monthly decreases.     

Fifthly, after all rows have been analyzed upon the completion of the row loop iterations, the value representative of the accumulative change of the profit/loss is identified as the profit/loss over the entire period and used to determine the change over the entire period (or total months).

Lastly, the results of the analysis are printed to the terminal and exported as a text file.









