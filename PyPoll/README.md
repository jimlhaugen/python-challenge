# Module 3 Challenge

This module comprises two challenges.  This challenge named "PyPoll" presents a real-world situation of helping a small, rural town modernize its vote-counting process.  Poll data is provided in a dataset called bedget_data.csv comprising three columns with “Ballot ID,” “County,” and “Candidate” headers and a plethora of rows, where each row represents one vote.  A quick review of the data reveals each row of the Candidate column consists of three candidate names: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.  

A challenge named "PyBank" of the Module 3 Challenge in which a real-world situation in which a financial dataset is employed may be found under the PyPoll directory.

## PyPoll Instructions

As instructed, a Python script has been created to analyze the records to calculate each of the following: 

* The total number of votes cast.

* A complete list of candidates who received votes.

* The percentage of votes each candidate won.

* The total number of votes each candidate won.

* The winner of the election based on the popular vote.

As instructed, the final script (1) presents the results in a format that was provided (2) prints to the terminal, and (3) exports the results to a .txt file. 

Based on these instructions, Ballot ID and County columns are not necessary and will not be included in the analysis.

## PyPoll Solution

The script begins by importing os and csv modules so that the script interacts with the operating system and classes are implements to read and write the tabular data presented in the .csv, respectively. Prior to each row of the data being analyzed, initializations are performed.  Unlike the script in PyBank, the initializations are minimal.

Two lists are employed: one list is initialized with the names of the three candidates, and the other list is initialized with zero values but subject to being incremented by one as each vote is counted; this list keeps the running count of votes of its corresponding candidate.  These initializations are minimal because one value of vote corresponds to one candidate, which allows the ability to the same list index for both lists.  Candidate Stockham and his corresponding number of votes will share an index 0 in both lists.  Similarly, candidates DeGette and Doane and their respective number of votes will share indices 1 and 2, respectively.  

Only one non-list variable representative of the total number of votes is needed.  It is initialized to zero and will be employed to count the number of votes (or row) with each row loop iteration and used to determine the percentages of votes each candidate receives at the complete of the iterations. 

After the initialization is completed, an iteration begins the analysis in which each row is sequentially analyzed. Firstly, the third column of each row is identified as a candidate.
Secondly, the candidate is confirmed to be one of the three in the candidates list.  Once confirmed, the count of votes is increased by 1.  

Thirdly, a for loop consisting of three iterations is presented in which the name of the candidate receiving the vote in the row is determined, and one value in the vote count list corresponding to the candidate is incremented by 1.  

Fourthly, after all rows have been analyzed upon the completion of the row loop iterations, the winning candidate can be determined by comparing the number of votes received by each candidate to determine which candidate has the greatest number of votes.

