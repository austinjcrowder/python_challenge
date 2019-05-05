# Dependencies
import os
import csv

# Files to load and output (Remember to change these)
pybank_csv_path = os.path.join("Resources/budget_data.csv")
file_to_output = "Resources/budget_analysis.txt"

# setting the variables 
total_months = 0
total_revenue = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_decrease = ['', 999999999]
greatest_increase = ['', 0]

with open(pybank_csv_path, newline="") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")

    for row in reader:

        # Track the total.. i have a friend that helped me fix some issues and he told me to use += and here are two links that explain and this helped me understand it https://stackoverflow.com/questions/823561/what-does-mean-in-python/823878
        total_months += 1

        total_revenue += int(row['Profit/Losses'])

        # revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # greatest increase
        if revenue_change>greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row['Date']

        # greatest decrease
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row['Date']

# average change in revenue
revenue_avg = sum(revenue_change_list)/len(revenue_change_list)

print('Average Change in Revenue: $ ' +str(revenue_avg))
print("total Months: " + str(total_months))
print("total Revenue: $ " + str(total_revenue))
print(greatest_increase)
print(greatest_decrease)

#output my buddy helped explain this to me and i used this source to understand it https://docs.python.org/2/tutorial/inputoutput.html and https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python the w puts it into
with open(file_to_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: %d\n" %total_months)
    file.write("Total Revenue: %d\n" %total_revenue)
    file.write("Average Revenue Change: $%d\n" % revenue_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1])) 
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

# Print the output s
print(file_to_output)

