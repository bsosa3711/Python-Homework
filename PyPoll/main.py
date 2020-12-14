import os
import csv


csvpath = os.path.join("Resources", "election_data.csv")

candidate = {}
vote_percentage = {}
votes = 0

with open(csvpath, ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        votes += 1
        if row[2] in candidate:
            candidate[row[2]]["Votes"] += 1
        else:
            candidate[row[2]] = {}
            candidate[row[2]]["Votes"] = 1


for k, v in candidate.items():
    percent = (v["Votes"] / votes)
    p_100 = percent * 100
    total_vp = round(p_100, 2)
    candidate[k]["Percent"] = total_vp 
      
   

print("Election Results")
print("------------------")
print(f'Total Votes: {votes}')
print("------------------")


for k, v in candidate.items(): 
    final_results = f'{k}: {v["Percent"]}% ({v["Votes"]})'
    print(final_results) 
    
for k, v in candidate.items():       
    winning_candidate = "Khan"

print("-------------------")
print(f'Winner: {winning_candidate}')