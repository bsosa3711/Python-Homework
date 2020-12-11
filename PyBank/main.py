import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    budget_header = next(csvreader)
    total_months = []
    total_pl = []
    
    profits = 0
    for row in csvreader:
        total_months.append(row[0])
        total_pl.append(int(row[1]))

profit = sum(total_pl)
length_of_the_csv = len(total_months)            

print(length_of_the_csv)
print(profit)


  