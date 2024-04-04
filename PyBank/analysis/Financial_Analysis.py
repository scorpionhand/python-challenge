import os
import csv

# First make sure we are in the current script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Change to csv directory
os.chdir("..\\Resources")
csv_path = str(os.getcwd()) + "\\budget_data.csv"

# Array to capture the header
header = []

# # Dictionary for unique entries
# votes_dict = {}

# Array to capture profit/loss data
p_and_l = []
p_and_l_changes = []

# Use to count the number of entries
row_count = 0

# Add up the net ammount
net_ammount = 0

# # Use to get a list of candidates
# candidate = {}

# Open the csv file from the path defined earlier
with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    # Advance past the header row
    header = next(csvreader)

    for row in csvreader:
        p_and_l.append (int(row[1]))
        row_count += 1

        net_ammount = net_ammount + int(row[1])

        if row_count > 1:
            p_and_l_changes.append(int(row[1]) - p_and_l[row_count-2])
         
#         votes_dict['ID'] = row[0]
#         votes_dict['County'] = row[1]
#         votes_dict['Candidate'] = row[2]

#         if votes_dict['Candidate'] in candidate:
#             candidate[votes_dict['Candidate']] += 1
#         else:
#             candidate[votes_dict['Candidate']] = 1

# vote_percentages = []
# # Store vote percentages for later
# for vote_percentage in candidate:
#     vote_percentages.append (candidate[vote_percentage] / row_count)


# print("Election Results \n\n")
# print("-------------------------\n\n")
# print(f"Total Votes: {row_count}\n\n")
# print("-------------------------\n\n")

# # Prep to output percentages and winner
# # Store the winner's name
# winner = ""

# # Used to compare for the most votes
# largest_count = 0

# # loop iteration
# i=0

# # Calculate percentages, find winner and output results
# for vote_percent in vote_percentages:
#     # use to get the name from the candidate dictionary
#     cand_name = list(candidate)[i]
    
#     # output vote percent and vote count
#     print(f"{vote_percent:.3%} ({candidate[cand_name]})\n\n")
    
#     if candidate[cand_name] > largest_count:
#         # store the winner's name
#         winner = cand_name
#         largest_count = candidate[cand_name]
#     i += 1

# print("-------------------------\n\n")
# print(f"Winner: {winner}\n\n")
print("-------------------------\n\n")


