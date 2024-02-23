import os
import csv

 ################################################################################  



######  complete list of candidates receiving votes
CandidateName = ['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']
CandidateVoteCount = [0, 0, 0]
TotalVotes = 0
TotalProfitLoss = 0
VoteCountCandidate1 = 0
VoteCountCandidate2 = 0
VoteCountCandidate3 = 0
CandidateName1 = 0
CandidateName2 = 0
CandidateName3 = 0
CarryForwardMonthProfit = 0
GreatestMonthlyIncreaseMonth = '' 
GreatestMonthlyDecreaseMonth = '' 
ChangeEntirePeriod = 0
Count = 0
ProfitBeginningPeriod = 0

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

            #if candidate == CandidateName[0]:            
            #    VoteCountCandidate1 = VoteCountCandidate1 + 1 
            #if candidate == CandidateName[1]:            
            #    VoteCountCandidate2 = VoteCountCandidate2 + 1
            #if candidate == CandidateName[2]:
            #    VoteCountCandidate3 = VoteCountCandidate3 + 1 
            for x in range(3):
                if candidate == CandidateName[x]:            
                    CandidateVoteCount[x] += 1 
           # if candidate == CandidateName[1]:            
             #   CandidateVoteCount[1] += 1 
           # if candidate == CandidateName[2]:
          #      CandidateVoteCount[2] += 1 

        if((CandidateVoteCount[0] > CandidateVoteCount[1]) and (CandidateVoteCount[0] > CandidateVoteCount[2])): 
            Winner = CandidateName[0]
        elif((CandidateVoteCount[1] > CandidateVoteCount[0]) and (CandidateVoteCount[1] > CandidateVoteCount[2])): 
            Winner = CandidateName[1]
        else:
            Winner = CandidateName[2]
        
def percent(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
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
#with open(output_path, 'w') as textfile:

#    textfile.write("Election Results" + "\n\n\n\n")

 #   textfile.write("-" * 25 + "\n\n\n\n")

 #   textfile.write("Total Votes: " + str(TotalVotes) + "\n\n\n\n")

  #  textfile.write("-" * 25 + "\n\n\n\n")

   # textfile.write(CandidateName1, ":", + str(VoteCountCandidate1) + "\n\n\n\n")

   # textfile.write("VoteCountCandidate1: " + "\n\n\n\n") python main.py

 #   textfile.write("Greatest Increase in Profits: " + str(VoteCountCandidate1) + " ($" + str(VoteCountCandidate1) + ")" + "\n\n\n\n")

  #  textfile.write("Greatest Decrease in Profits: " + str(VoteCountCandidate1) + " ($" + str(VoteCountCandidate1) + ")"