"""
Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
""" 

# import os to find the file path
import os

# import csv to read the file
import csv

# find the file source
PyBank = os.path.join("Resources", "budget_data.csv")

#specify the file to write to
Report = os.path.join("Resources", "Analysis_Report.txt")

# variables
#Assign a variable called total_month to hold the total number of months with initial value to 0
total_month = 0
#Assign a variable  called net_total to hold the total of " profit/loss" over the entire period with initial value of zero
net_total = 0
# Assign a a list called changes to to hold the value of changes
monthly_changes = [] 
# Assign an empty listc called months to hold the month
months = []

# read the csv file
with open(PyBank) as Budgetfile:
    # create csv reader
    csvReader = csv.reader(Budgetfile, delimiter= ",")

    #Read the header row
    header = next(csvReader)

    # move to first row
    first_row = next(csvReader)


    # increment to count the number of months
    total_month +=1 

     #calculate the net total
    net_total += float(first_row[1])

    # establish the previous revenue
    Previous_rev = float(first_row[1])


    for row in csvReader:
        # increment to count the number of months
        total_month +=1 

        #calculate the net total
        net_total += float(row[1])

        # calculate the net change
        net_change = float(row[1]) - Previous_rev

        # add the to the list of net chang
        monthly_changes.append(net_change)

        # add the first month that a change will take place
        months.append(row[0])

        #update the previous revenue
        Previous_rev = float(row[1])


# calculate the average change per month
AverageChangePerMonth = sum(monthly_changes)/len(monthly_changes)

Greatest_Increase = ["",0] # to hold the month and value of greatest increase
Greatest_Decrease = ["",0] # to hold the month and value of greatest decrease

 # create a loop to find the greatest increase and greatest decreae
for H in range(len(monthly_changes)): 
    # find the greatest month and greatest value
    if (monthly_changes[H]) > Greatest_Increase[1]:
       Greatest_Increase[1] = monthly_changes[H]
       #update the  month
       Greatest_Increase[0]= months[H]

    # find the greatest decrease and month
    if (monthly_changes[H]) < Greatest_Decrease[1]:
       Greatest_Decrease[1] = monthly_changes[H]
       #update the  month
       Greatest_Decrease[0]= months[H]



#generate the output
output = (f"Financial Analyis \n"
          f"----------------------------------\n\n"
          f" Total Months:  {total_month}\n\n"
          f" Total: ${net_total:.0f}\n\n"
          f" Average Change: ${AverageChangePerMonth:.2f}\n\n"
          f" Greatest Increase in Profits: {Greatest_Increase[0]} (${ Greatest_Increase[1]:.0f})\n\n"
          f" Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]:.0f}) ")



#print the output
print(output)

# Export the analysis report 

# open the file using write mode and specify the variable to hold the contents
with open(Report, "w") as textfile:
    #write the file
    textfile.write(output)

# The end