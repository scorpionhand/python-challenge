import os
import csv

# Globals ------------------------------------------------
# First make sure we are in the current script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Change to csv directory
os.chdir("Resources")
csv_path = str(os.getcwd()) + "\\budget_data.csv"

# monthly profit/loss total
p_and_l_total = 0

# Count the number of entries
row_count = 0

# Add up the net ammount
net_ammount = 0

# get the monthly $ change
changes = 0

# greatest increase results
greatest_increase = 0
greatest_increase_month = ""

# greatest decrease results
greatest_decrease = 0
greatest_decrease_month = ""
#---------------------------------------------------------


# Open the csv file
with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    # Advance past the header row
    next(csvreader)

    for row in csvreader:
        # sum of rows for total months
        row_count += 1

        # sum of amount column for net amount
        net_ammount = net_ammount + int(row[1])

        # skip first row the do changes calculations
        if row_count > 1:
            # capture change from previous month
            changes = (int(row[1]) - prev_value)

            # sum up the monthly changes for average change
            p_and_l_total = p_and_l_total + changes
        
        # grab the greatest increase and decrease amount and month
        if changes > greatest_increase:
            greatest_increase = changes
            greatest_increase_month = str(row[0])
        if changes < greatest_decrease:
            greatest_decrease = changes
            greatest_decrease_month = str(row[0])
        
        # store value for change calculation
        prev_value = int(row[1])
#---------------------------------------------------------


# output to terminal
print("Financial Analysis \n")
print("-------------------------\n")
print(f"Total Months: {row_count}\n")
print(f"Net Amount: ${net_ammount}\n")
print(f"Average Change: ${p_and_l_total / (row_count-1): .2f}\n")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
#---------------------------------------------------------


# output to text file
os.chdir("..\\analysis")
result_file = str(os.getcwd()) + "\\Bank_results.txt"
with open(result_file, 'w') as write_file:
    print("Financial Analysis \n", file=write_file)
    print("-------------------------\n", file=write_file)
    print(f"Total Months: {row_count}\n", file=write_file)
    print(f"Net Amount: ${net_ammount}\n", file=write_file)
    print(f"Average Change: ${p_and_l_total / (row_count-1): .2f}\n", file=write_file)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n", file=write_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n", file=write_file)
#---------------------------------------------------------
