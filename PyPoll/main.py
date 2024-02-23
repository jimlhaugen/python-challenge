import os
import csv

 ################################################################################  



######  complete list of candidates receiving votes
CandidateName = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
CandidateVoteCount = [0, 0, 0]
TotalVotes = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        vote = row[0]
        county = row[1]
        candidate = row[2]

        if row[2] in CandidateName:
            TotalVotes = TotalVotes + 1
            for x in range(3):
                if candidate == CandidateName[x]:            
                    CandidateVoteCount[x] += 1

        if((CandidateVoteCount[0] > CandidateVoteCount[1]) and (CandidateVoteCount[0] > CandidateVoteCount[2])): 
            Winner = CandidateName[0]
        elif((CandidateVoteCount[1] > CandidateVoteCount[0]) and (CandidateVoteCount[1] > CandidateVoteCount[2])): 
            Winner = CandidateName[1]
        else:
            Winner = CandidateName[2]
        
def percent(num1, num2):
    percentage = "{:.3%}".format(num1 / num2)
    return percentage
  
print("Election Results" + "\n\n\n\n")
print("-" * 25 + "\n\n\n\n")
print("Total Votes:", TotalVotes, "\n\n\n\n")
print("-" * 25 + "\n\n\n\n")

for y in range(3):
    print(CandidateName[y], ": ", percent(CandidateVoteCount[y], TotalVotes), " (", CandidateVoteCount[y], ")", "\n\n\n\n", sep='')
    
print("-" * 25 + "\n\n\n\n")
print("Winner: " + Winner + "\n\n\n\n")
print("-" * 25)

###########################################################################

# Specify the file to write to
output_path = os.path.join("output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    textfile.write("Election Results" + "\n\n\n\n")
    textfile.write("-" * 25 + "\n\n\n\n")
    textfile.write("Total Votes:" + str(TotalVotes) + "\n\n\n\n")
    textfile.write("-" * 25 + "\n\n\n\n")

    for z in range(3):
        textfile.write(CandidateName[z] + ": " + percent(CandidateVoteCount[z], TotalVotes) + " (" + str(CandidateVoteCount[z]) + ")" + "\n\n\n\n" ) # + sep=''

    textfile.write("-" * 25 + "\n\n\n\n")
    textfile.write("Winner: " + Winner + "\n\n\n\n")
    textfile.write("-" * 25)