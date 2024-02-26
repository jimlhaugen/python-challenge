
            ### Import os and csv modules
import os
import csv

            ### Initialize strings list string of months
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

            ### Initialize strings variables for recording months of greatest increase/decreases 
GreatestMonthlyIncreaseMonth = '' # records month of greatest monthly increase upon its condition
GreatestMonthlyDecreaseMonth = '' # records month of greatest monthly increase upon its condition

            ### Initialize numerical numerical variables subjected to loops
TotalMonths = 0                     # keeps count of months by counting each rows with each loop interation
TotalProfitLoss = 0                 # keeps running cumulation of total profit/loss with each interation
GreatestMonthlyIncrease = 0         # records greatest monthly increase upon its condition
GreatestMonthlyDecrease = 0         # records greatest monthly decerease upon its condition
MonthlyChange = 0                   # records monthly change between successive interations of loop
CarryFwdMonthProfitLoss = 0         # carries forward cumulative profit/loss to the next iterantion of loop  
ProfitLosssBeginningPeriod = 0      # records the first month profit/loss data
Count = 0                           # used to identify first month for recording ProfitLossBeginningPeriod
ChangeEntirePeriod = 0              # records the accumulative change of profit/loss data for all rows 

            ### Set path for file
csvpath = os.path.join("Resources", "budget_data - Copy.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        month = row[0]
        profit = row[1]

        if row[0][:3] in months:                                
            TotalMonths = TotalMonths + 1
            TotalProfitLoss = TotalProfitLoss + int(profit)
            Count = Count + 1
            MonthlyChange = int(profit) - CarryFwdMonthProfitLoss 

            if Count == 1:
                ProfitLosssBeginningPeriod = int(profit)

            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month

            CarryFwdMonthProfitLoss = int(profit)
            
    ProfitEndPeriod = CarryFwdMonthProfitLoss   # using different varaible to distinguish functionalities                
    ChangeEntirePeriod = ProfitEndPeriod - ProfitLosssBeginningPeriod 


print("Financial Analysis" + "\n\n\n\n")
print("-" * 28 + "\n\n\n\n")
print("Total Months: ", TotalMonths, "\n\n\n\n")
print("Total: $", TotalProfitLoss, "\n\n\n\n", sep='')
print("Average Change: $", round(ChangeEntirePeriod / (TotalMonths - 1), 2), "\n\n\n\n", sep='')
print("Greatest Increase in Profits: ", GreatestMonthlyIncreaseMonth," ($", GreatestMonthlyIncrease, ")", "\n\n\n\n", sep='')
print("Greatest Decrease in Profits: ", GreatestMonthlyDecreaseMonth," ($", GreatestMonthlyDecrease, ")", sep='')

###########################################################################

# Specify the file to write to
output_path = os.path.join("analysis","results_temp2.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    textfile.write("Financial Analysis" + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("-" * 28 + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Total Months: " + str(TotalMonths) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Total: $" + str(TotalProfitLoss) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Average Change: $" + str(round(ChangeEntirePeriod / (TotalMonths - 1), 2)) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Greatest Increase in Profits: " + str(GreatestMonthlyIncreaseMonth) + " ($" + str(GreatestMonthlyIncrease) + ")" + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Greatest Decrease in Profits: " + str(GreatestMonthlyDecreaseMonth) + " ($" + str(GreatestMonthlyDecrease) + ")")



