import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")


 ################################################################################  

print("\n\n\n")
#print(len(row))

print("\n\n\n")
print("Election Results")
print("\n\n\n")
print("-" * 28)
print("\n\n\n")
print("Total Votes")
print("\n\n\n")
print("-" * 28)

#################################################################################

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(months[0:11]) #   prints -Jan but not -Dec

print(months[11])   #   prints -Dec

TotalMonth = 0
TotalProfit = 0
total = 0
GreatestMonthlyIncrease = 0
GreatestMonthlyDecrease = 0
MonthlyChange = 0
CarryForwardMonthProfit = 0
GreatestMonthlyIncreaseMonth = '' 
GreatestMonthlyDecreaseMonth = '' 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        month = row[0]
        trimmed_month = month[:3]
        profit = row[1]
        print("\n\n")
        print('trimmed_month = ',trimmed_month, 'profit = ',profit)




        if trimmed_month == 'Jan':
            print("Is this month January?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)




        elif trimmed_month == 'Feb':
            print("Is this month February?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'Mar':
            print("Is this month March?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)






        elif trimmed_month == 'Apr':
            print("Is this month April?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'May':
            print("Is this month May?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'Jun':
            print("Is this month June?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)






        elif trimmed_month == 'Jul':
            print("Is this month July?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'Aug':
            print("Is this month August?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'Sep':
            print("Is this month September?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)







        elif trimmed_month == 'Oct':
            print("Is this month October?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)


 
 
        elif trimmed_month == 'Nov':
            print("Is this month November?", month, "profit is ", profit)
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)




 
 
        elif trimmed_month == 'Dec':
            print("Is this month December?", month, "profit is ", profit)        
            TotalMonth = TotalMonth + 1
            TotalProfit = TotalProfit + int(profit)
            print(TotalMonth, TotalProfit)
            print("Before Monthly Change is ", MonthlyChange)
            MonthlyChange = int(profit) - CarryForwardMonthProfit 
            print("Monthly Change is: ", MonthlyChange)
            if MonthlyChange > 0:
                if MonthlyChange > GreatestMonthlyIncrease:
                    GreatestMonthlyIncrease = MonthlyChange
                    GreatestMonthlyIncreaseMonth = month
            if MonthlyChange < 0:
                if MonthlyChange < GreatestMonthlyDecrease:
                    GreatestMonthlyDecrease = MonthlyChange
                    GreatestMonthlyDecreaseMonth = month
            print("Greatest Profit Increase: ", GreatestMonthlyIncreaseMonth, GreatestMonthlyIncrease)
            print("Greatest Profit Decrease: ", GreatestMonthlyDecreaseMonth, GreatestMonthlyDecrease)
            CarryForwardMonthProfit = int(profit)






        else:
            print("There is no valid month provided in this csv row of data.")                                                                                                                         
        
        
        #if month == "Dec-10":
        #    print("month = Dec-10")
        #if line[0] == 'Mar-10': # or 'Feb-10': #'Jan' or 'Feb' or 'Jan' or'Mar' or'Apr' or'May'or'Jun'or'Jul'or'Aug'or'Sep'or'Oct'or'Nov'or'Dec':    
        #    print(line[0])
        #    total = total+1
        #    print(line[1])
        #    print(total)
        #    print(months)
        #else:
        #    print("go forward")

print("\n\n\n")
print("Total Months: ", TotalMonth)
print("Total: $", TotalProfit, sep='')
print("Average Change: ", )
print("Greatest Increase in Profits: ", GreatestMonthlyIncreaseMonth," ($", GreatestMonthlyIncrease, ")", sep='')
print("Greatest Decrease in Profits: ", GreatestMonthlyDecreaseMonth," ($", GreatestMonthlyDecrease, ")", sep='')
###########################################################################



























#################################################################################
# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    # I added lineterminator = '\n' to put a spacer between first row and id row
    csvwriter = csv.writer(csvfile, delimiter=',', lineterminator = '\n')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

   # csvwriter.whiterow()

    # Write the id row
    csvwriter.writerow(['Haugen1', 'James1', 'none of your business'])



