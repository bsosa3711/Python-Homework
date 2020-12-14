import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#removing header
    budget_header = next(csvreader)
    total_months = []
    total_pl = []
    changes = []
    
    #appending both columns
    for row in csvreader:
        total_months.append(row[0])
        total_pl.append(int(row[1]))
#added a new row to find the change for each line in row[1]

    for r in range(len(total_pl)-1):
        changes.append(total_pl[r+1]-total_pl[r])

#getting the average(mean) for those changes
    def mean(changes):
        return sum(changes) / len(changes)
#using max and min to find the largest increase and decrease
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

output_file = os.path.join("budget_data_analysis.txt")

with open(output_file, 'w', newline='') as datafile:
    datafile.write("Financial Analysis")
    datafile.write("--------------------")
    datafile.write(f'Total Months: , {dates}')
    datafile.write(f'Total: $, {profit}')
    datafile.write(f'Average Change: $, {r_average}')
    datafile.write(f'Greatest Increase in Profits: Feb-2012 $, {increase}')
    datafile.write(f'Greates Decrease in Profits: Sep-2013 $, {decrease}')