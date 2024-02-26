
                ### Import os and csv modules
import os
import csv

                ### Initialize strings list of months
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

                ### Initialize strings variables for recording months of greatest increase/decreases 
GreatestMonthlyIncreaseMonth = '' # records month of greatest monthly increase upon its condition
GreatestMonthlyDecreaseMonth = '' # records month of greatest monthly increase upon its condition

                ### Initialize numerical variables subjected to loops
TotalMonths = 0                     # keeps count of months by counting each rows with each loop interation
TotalProfitLoss = 0                 # keeps running cumulation of total profit/loss with each interation
GreatestMonthlyIncrease = 0         # records greatest monthly increase upon its condition
GreatestMonthlyDecrease = 0         # records greatest monthly decrease upon its condition
MonthlyChange = 0                   # records monthly change between successive interations of loop
CarryFwdMonthProfitLoss = 0         # carries forward cumulative profit/loss to the next iterantion of loop  
ProfitLosssBeginningPeriod = 0      # records the first month profit/loss data
Count = 0                           # used to identify first month for recording ProfitLossBeginningPeriod
ChangeEntirePeriod = 0              # records the accumulative change of profit/loss data for all rows 

                ### Defines input path for budget_data.csv 
csvpath = os.path.join("Resources", "budget_data.csv")

                ### Open .csv file in READ mode, file object csvfile is converted to a csv.reader object named csvreaderith open(csvpath) as csvfile:
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

                ### Skip the header rwo
    header = next(csvreader)

                ### Reads each row of csvreader after the header originally presented in the .csv file 
                ### For each row in csvreader, column 1 (or index 0 of list months) equals month
                ### For each row in csvreader, column 2 (or index 1 of list months) equals profit (i.e., profit/loss)        
    for row in csvreader:
        month = row[0]
        profit = row[1]

                ### Ensures the first three characters of string matches one of the 12 month abbreviations in list months
                ### Begins loop for each row having a good month abbreviation   
        if row[0][:3] in months:   

                ### Performs the following for each row
            TotalMonths = TotalMonths + 1
            TotalProfitLoss = TotalProfitLoss + int(profit)
            Count = Count + 1

            MonthlyChange = int(profit) - CarryFwdMonthProfitLoss 

                ### Sets a condition for defining the begining profit/loss value
                ### Used for determining the change over the entire period
            if Count == 1:
                ProfitLosssBeginningPeriod = int(profit)

                ### Sets a condition which records month (i.e., mmm-yr) having the greatest monthly increase 
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month

                ### Sets a condition which records month (i.e., mmm-yr) having the greatest monthly decrease 
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month

                ### Records current profit/loss and used above
            CarryFwdMonthProfitLoss = int(profit)
  
        ProfitEndPeriod = CarryFwdMonthProfitLoss   # using different variable to distinguish functionalities                

                ### Determines accumulative change of profit/loss data for all rows 
        ChangeEntirePeriod = ProfitEndPeriod - ProfitLosssBeginningPeriod 

                ### Prints to terminal in instructed format
print("Financial Analysis" + "\n\n\n\n")
print("-" * 28 + "\n\n\n\n")
print("Total Months: ", TotalMonths, "\n\n\n\n")
print("Total: $", TotalProfitLoss, "\n\n\n\n", sep='')      # sep'' ensures no empty space in print
print("Average Change: $", round(ChangeEntirePeriod / (TotalMonths - 1), 2), "\n\n\n\n", sep='')
print("Greatest Increase in Profits: ", GreatestMonthlyIncreaseMonth," ($", GreatestMonthlyIncrease, ")", "\n\n\n\n", sep='')
print("Greatest Decrease in Profits: ", GreatestMonthlyDecreaseMonth," ($", GreatestMonthlyDecrease, ")", sep='')

                ### Defines export path
output_path = os.path.join("analysis","results.txt")

                ### Open .txt file in WRITE mode
with open(output_path, 'w') as textfile:

                ### Exports to .txt in instructed format
    textfile.write("Financial Analysis" + "\n\n\n\n")
    textfile.write("-" * 28 + "\n\n\n\n")
    textfile.write("Total Months: " + str(TotalMonths) + "\n\n\n\n")
    textfile.write("Total: $" + str(TotalProfitLoss) + "\n\n\n\n")
    textfile.write("Average Change: $" + str(round(ChangeEntirePeriod / (TotalMonths - 1), 2)) + "\n\n\n\n")
    textfile.write("Greatest Increase in Profits: " + str(GreatestMonthlyIncreaseMonth) + " ($" + str(GreatestMonthlyIncrease) + ")" + "\n\n\n\n")
    textfile.write("Greatest Decrease in Profits: " + str(GreatestMonthlyDecreaseMonth) + " ($" + str(GreatestMonthlyDecrease) + ")")