import os
import csv

 ################################################################################  

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
TotalMonths = 0
TotalProfit = 0 
GreatestMonthlyIncrease = 0
GreatestMonthlyDecrease = 0
MonthlyChange = 0
CarryForwardMonthProfit = 0
GreatestMonthlyIncreaseMonth = '' 
GreatestMonthlyDecreaseMonth = '' 
ChangeEntirePeriod = 0
Count = 0
ProfitBeginningPeriod = 0

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        month = row[0]
        profit = row[1]

        if row[0][:3] in months:
            TotalMonths = TotalMonths + 1
            TotalProfit = TotalProfit + int(profit)
            Count = Count + 1
            if Count == 1:
                ProfitBeginningPeriod = int(profit)

            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month

            CarryForwardMonthProfit = int(profit)
            
        ProfitEndPeriod = int(profit)
        ChangeEntirePeriod = ProfitEndPeriod - ProfitBeginningPeriod 


print("Financial Analysis" + "\n\n\n\n")
print("-" * 28 + "\n\n\n\n")
print("Total Months: ", TotalMonths, "\n\n\n\n")
print("Total: $", TotalProfit, "\n\n\n\n", sep='')
print("Average Change: $", round(ChangeEntirePeriod / (TotalMonths - 1), 2), "\n\n\n\n", sep='')
print("Greatest Increase in Profits: ", GreatestMonthlyIncreaseMonth," ($", GreatestMonthlyIncrease, ")", "\n\n\n\n", sep='')
print("Greatest Decrease in Profits: ", GreatestMonthlyDecreaseMonth," ($", GreatestMonthlyDecrease, ")", sep='')

###########################################################################

# Specify the file to write to
output_path = os.path.join("analysis","results_temp.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as textfile:

    textfile.write("Financial Analysis" + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("-" * 28 + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Total Months: " + str(TotalMonths) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Total: $" + str(TotalProfit) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Average Change: $" + str(round(ChangeEntirePeriod / (TotalMonths - 1), 2)) + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Greatest Increase in Profits: " + str(GreatestMonthlyIncreaseMonth) + " ($" + str(GreatestMonthlyIncrease) + ")" + "\n\n\n\n")
    #textfile.write("\n\n\n\n")
    textfile.write("Greatest Decrease in Profits: " + str(GreatestMonthlyDecreaseMonth) + " ($" + str(GreatestMonthlyDecrease) + ")")



