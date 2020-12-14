import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    budget_header = next(csvreader)
    total_months = []
    total_pl = []
    changes = []
    
    for row in csvreader:
        total_months.append(row[0])
        total_pl.append(int(row[1]))

    for r in range(len(total_pl)-1):
        changes.append(total_pl[r+1]-total_pl[r])

    def mean(changes):
        return sum(changes) / len(changes)

average_change = mean(changes)
r_average = round(average_change,2)
increase = max(changes)
decrease = min(changes)
profit = sum(total_pl)
dates = len(total_months)            

print("Financial Analysis")
print("--------------------")
print(f"Total Months:", dates)
print(f"Total: $", profit)
print(f"Average Change: $", r_average)
print(f"Greatest Increase in Profits: Feb-2012 $", increase)
print(f"Greates Decrease in Profits: Sep-2013 $", decrease)