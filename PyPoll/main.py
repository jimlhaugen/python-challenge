
                ### Import os and csv modules
import os
import csv

                ### Initialize string list of the name of each of the three candidates
                ### Initialize numerical list for accumulating vote count for each candidate
                ### Initialize variable for keeping count of total votes
                ### Indices 0-2 correspond to vote counts of candidates Stockham, DeGette, and Doane, respectively 
CandidateName = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
CandidateVoteCount = [0, 0, 0]
NumberofVotes = 0

                ### Defines input path for budget_data.csv 
csvpath = os.path.join("Resources", "election_data_sub.csv")

                ### Open .csv file in READ mode, file object csvfile is converted to a csv.reader object named csvreader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

                ### Skip the header row
    header = next(csvreader)
    
                ### Reads each row of csvreader after the header originally presented in the .csv file 
                ### For each row in csvreader, column 3 (or index 2 of candidates numerical list) equals candidates names
                ### For each row in csvreader, columns 1 and 2 (or indices 0 and 1) are not necessary for the analysis
    for row in csvreader:
        candidate = row[2]

                ### Ensures the data represents the name of one of the three canddiates
                ### Begins loop for each row having a good candidate name   
        if row[2] in CandidateName:

                ### Performs three iterations to determines the candidate's name 
                ### Numerical value of index corresponding to candidate is incremented by one 
            NumberofVotes = NumberofVotes + 1
            for x in range(3):
                if candidate == CandidateName[x]:            
                    CandidateVoteCount[x] += 1

                ### Determines the winner as the candidate having greatest vote count
        if((CandidateVoteCount[0] > CandidateVoteCount[1]) and (CandidateVoteCount[0] > CandidateVoteCount[2])): 
            Winner = CandidateName[0]
        elif((CandidateVoteCount[1] > CandidateVoteCount[0]) and (CandidateVoteCount[1] > CandidateVoteCount[2])): 
            Winner = CandidateName[1]
        else:
            Winner = CandidateName[2]



                ### Defines percentage formatting function to three decimal points 
def percent(num1, num2): 
    percentage = "{:.3%}".format(num1 / num2)
    return percentage

                ### Prints to terminal in instructed format  
print("Election Results" + "\n\n\n\n")
print("-" * 25 + "\n\n\n\n")
print("Total Votes:", NumberofVotes, "\n\n\n\n")
print("-" * 25 + "\n\n\n\n")

                ### Prints identical format for each candidate 
for y in range(3):
    print(CandidateName[y], ": ", percent(CandidateVoteCount[y], NumberofVotes), " (", CandidateVoteCount[y], ")", "\n\n\n\n", sep='')
    
print("-" * 25 + "\n\n\n\n")
print("Winner: " + Winner + "\n\n\n\n")
print("-" * 25)

                ### Defines export path
output_path = os.path.join("analysis", "results.txt")

                ### Open .txt file in WRITE mode
with open(output_path, 'w') as textfile:

                ### Exports to .txt in instructed format
    textfile.write("Election Results" + "\n\n\n\n")
    textfile.write("-" * 25 + "\n\n\n\n")
    textfile.write("Total Votes: " + str(NumberofVotes) + "\n\n\n\n")
    textfile.write("-" * 25 + "\n\n\n\n")
    for z in range(3):
        textfile.write(CandidateName[z] + ": " + percent(CandidateVoteCount[z], NumberofVotes) + " (" + str(CandidateVoteCount[z]) + ")" + "\n\n\n\n" ) # + sep=''
    textfile.write("-" * 25 + "\n\n\n\n")
    textfile.write("Winner: " + Winner + "\n\n\n\n")
    textfile.write("-" * 25)