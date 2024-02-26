# Module 3 Challenge

This module comprises two challenges.  The first challenge is PyBank which presents a real-world situation in which a financial dataset called budget_data.csv is provided comprising two columns with “Date” and “Profit/Loss” headers and numerous rows. A quick review of the data reveals that the former has a mmm-yr format and the latter has an integer format where negative numbers are preceded with a minus sign.  

The second challenge is PyPoll which presents a real-world situation of helping a small, rural town modernize its vote-counting process.  Poll data is provided in a dataset called bedget_data.csv comprising three columns with “Ballot ID,” “County,” and “Candidate” headers and a plethora of rows, where each row represents one vote.  A quick review of the data reveals each row of the Candidate column consists of three candidate names: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.   has three candidates reviews of the Dat and Profit/Loss columns reveal that the former has a mmm-yr format and the latter has an integer format where negative numbers are preceded with a minus sign

## PyBank Instructions

As instructed, a Python script has been created (1) to analyze the records to calculate each of the following values and (2) to present the results in a format that was provided:

* The total number of months included in the dataset.

* The net amount of “Profit/Losses” over the entire period.

* The changes of “Profit/Losses” over the entire period, and then the average of those changes.

* The greatest increase in profits (date and amount) over the entire period.

* The greatest decrease in profits (date and amount) over the entire period.

As instructed, the final script (1) presents the results in a format that was provided (2) prints to the terminal, and (3) exports the results to a .txt file. 

## Solution

The script begins by importing os and csv modules so that the script interacts with the operating system and classes are implements to read and write the tabular data presented in the .csv, respectively.  

### First Loop "i"

Each ticker is represented by a plurality of rows, where each row corresponds to one date.  For each ticker, the first loop i reads each row per day to produce one row per ticker which presents the following information across four columns I-L, inclusive: (1) the ticker symbol, (2) the yearly change, (3) the percentage change, and (4) the total volume of stock.  

Prior to loop i being performed, headers idenfiying these will be added to row 1.  To identify the number of iterations which loop i will perform, the number of rows of the data set is determined using the .Cells(Rows.Count, 1).End(xlUp).  In addition, variables are initialized prior to begin subjected to the loop.  For the  initial loop, the opening price is obtained.

Loop i begins with a conditional "if" statement to determine whether the ticker has reached its last row by comparing with the ticker of the next row.  If the condition has not been met, loop i jumps to its corresponding "Else" statement where variables representative of the ticker count and volume count are increased by 1 and the actual numerical volume, respectively, so that the number of rows occupied by the ticker are known and an accumulated value of the numerical volume is increased until the condition has been met.

If the ticker condition has been met, then the closing price in the row is obtained and subtracted from the opening price from which the yearly change ticker's final and the percentage change between the two can be determined for the ticker.  Given this information, ticker, yearly change, and percentage change may be presented in Columns I-K, respectively, of the top-most available row under the headers, where the yearly change is highlighted with green format for a positive change and red format if the change is negative.  In addition, the volume of the ticker's last row is added to the accumulated value and then presented in column L next to percentage change.  Afterwards, variables representative of volume count, ticker count, and closing price are reset to zero for the next internation of loop i, and the value of the opening price is set for its corresponding value.

Loop i is repeated until the data of the last row has been read and subject to the script of the loop.

It should be noted loop i included a count of the number of tickers so that the number of rows created in columns data presented in Columns I-J, inclusive, would be known for defining the number of iterations that loop j would have to perform.

### Second Loop "j"

Prior to loop j being performed, headers identifying the following are presented in the cells as instructed: (1) Greatest % Increase, (2) Greatest % Decrease, (3) Greatest Total Volume, (4) Ticker, and (5) Value.  In addition, variables are initialized using the row 2 values under Columns I-L, inclusive.

Loop j will perform the number of iterations that was determined in loop i (as discussed above) in which each row will be subjected to three "If" conditional tests to compare values of percentage changes in Column K and total stock volumes of Column L.  As the loop progresses, values of greatest percentage increase, greatest percentage decrease, and greatest total volume will be updated as the condition warrants.  After each ticker in Column I has been subjected to the three "IF" rows, the tickers and corresponding values of greatest percentage increase, greatest percentage decrease, and greatest total volume will be presented in Columns O-Q, inclusive

## PyPoll Instructions

As instructed, a Python script has been created to analyze the records to calculate each of the following: 

* The total number of votes cast.

* A complete list of candidates who received votes.

* The percentage of votes each candidate won.

* The total number of votes each candidate won.

* The winner of the election based on the popular vote.

As instructed, the final script (1) presents the results in a format that was provided (2) prints to the terminal, and (3) exports the results to a .txt file. 





