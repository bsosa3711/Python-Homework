import os
import csv


csvpath = os.path.join("Resources", "election_data.csv")
#creating dictionaries
candidate = {}
vote_percentage = {}
votes = 0

with open(csvpath, ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#removing column headers
    header = next(csvreader)
#for loop to count each row as a vote
    for row in csvreader:
        votes += 1
#if the candidate that is already created is there, add one to the vote total
        if row[2] in candidate:
            candidate[row[2]]["Votes"] += 1
#if not, create a new candidate and count that row as a vote for new candidate. The for loop will repeat for each line.
        else:
            candidate[row[2]] = {}
            candidate[row[2]]["Votes"] = 1

#creates index for the amount of votes for each candidate. Equations to get the correct percentage.
for k, v in candidate.items():
    percent = (v["Votes"] / votes)
    p_100 = percent * 100
    total_vp = round(p_100, 2)
    candidate[k]["Percent"] = total_vp 
      
   

print("Election Results")
print("------------------")
print(f'Total Votes: {votes}')
print("------------------")

#final results show all of the votes and percentage for each candidate.
for k, v in candidate.items(): 
    final_results = f'{k}: {v["Percent"]}% ({v["Votes"]})'
    print(final_results) 
    
for k, v in candidate.items():       
    winning_candidate = "Khan"

print("-------------------")
print(f'Winner: {winning_candidate}')

output_file = os.path.join("election_data_analysis.txt")

with open(output_file, 'w', newline='') as datafile:
    datafile.write("Election Results")
    datafile.write("------------------")
    datafile.write(f'Total Votes: {votes}')
    datafile.write("------------------")
    datafile.write(f'{final_results}')
    datafile.write(f"-------------------")
    datafile.write(f'Winner: {winning_candidate}')