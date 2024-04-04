import os
import csv

# Globals ------------------------------------------------        
# First make sure we are in the current script directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Change to csv directory
os.chdir("Resources")
csv_path = str(os.getcwd()) + "\\election_data.csv"

# List to capture the header
header = []

# Dictionary for unique entries
votes_dict = {}

# List to capture voting data
votes = []

# Use to count the number of votes or csv entries
row_count = 0

# Use to get a list of candidates
candidate = {}

# Store the winner's name
winner = ""
#---------------------------------------------------------        


# function to calculate the election results
def output_results():
   
    # results saved in return_str
    return_str = ""

    vote_percentages = []
    # Store vote percentages for later
    for vote_percentage in candidate:
        vote_percentages.append (candidate[vote_percentage] / row_count)

    return_str = return_str + "Election Results \n"
    return_str = return_str + "-------------------------\n"
    return_str = return_str + "Total Votes: " + str(row_count) + "\n"
    return_str = return_str + "-------------------------\n"

    # Used to compare for the most votes
    largest_count = 0

    # Calculate percentages, find winner and output results
    i=0 # loop iteration
    for vote_percent in vote_percentages:
        # use to get the name from the candidate dictionary
        cand_name = list(candidate)[i]
        
        # output vote percent and vote count
        tst = candidate[cand_name]
        return_str = return_str + cand_name + ": " + str(format(vote_percent, ".3%")) + " (" + str(candidate[cand_name]) + ") \n"
        
        if candidate[cand_name] > largest_count:
            # store the winner's name
            winner = cand_name
            largest_count = candidate[cand_name]
        i += 1

    return_str = return_str + "-------------------------\n"
    return_str = return_str + "Winner: " + winner + "\n"
    return_str = return_str + "-------------------------\n"

    return return_str
#---------------------------------------------------------        


# Open the csv file from the path
with open(csv_path) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    # Grab the first row as a header row
    header = next(csvreader)

    for row in csvreader:
        row_count += 1
         
        votes_dict['ID'] = row[0]
        votes_dict['County'] = row[1]
        votes_dict['Candidate'] = row[2]

        if votes_dict['Candidate'] in candidate:
            candidate[votes_dict['Candidate']] += 1
        else:
            candidate[votes_dict['Candidate']] = 1
#---------------------------------------------------------        

# results to terminal
print(output_results())
#---------------------------------------------------------        


# results to a text file
os.chdir("..\\analysis")
result_file = str(os.getcwd()) + "\\poll_results.txt"
with open(result_file, 'w') as write_file:
    v = output_results()
    write_file.writelines(output_results())
#---------------------------------------------------------        
