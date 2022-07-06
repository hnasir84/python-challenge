"""
The code has to calculate the follwoing:

  The total number of votes cast
  A complete list of candidates who received votes
  The percentage of votes each candidate won
 The total number of votes each candidate won

  The winner of the election based on popular vote

""" 

# Import os module to read and write files
import os

# import csv module to to be able to deal woth coma sperated value files
import csv

# get to the file path to read election data file
input_file = os.path.join("Resources", "election_data.csv")

# export the analysis report to text file
output_file = os.path.join ("Analysis", "ElectionResults.txt")


# set variables
# This varaiable will hole the total number of votes casted  
Total_Votes = 0
# empty list that hold the candidates
Candidates = []
# a dictionary to hold the vots each candidate received
Candidates_Votes = {}
# assign a variable for winning count
WinningCount = 0 
#assignn a variable to hold the winning candidate
winning_candidate= ""

# read the csv file
with open(input_file) as csvfile :
    # create csv reader
    csvReader = csv.reader(csvfile, delimiter=",") 

    # read the header
    header = next(csvReader)

    #create a loop to calculate the total votes
    for row in csvReader:

        #calculate the increment through the folder
        Total_Votes +=1

        # check if the candidate is not in the list, add candidate to the candidates list
        if row[2] not in Candidates:
            Candidates.append(row[2])

            # add the value to the vote dictionary as well
            Candidates_Votes[row[2]] = 1
        
        else:
            # the candidate exist in the list
            # add a vote to the existing candidate
            Candidates_Votes[row[2]] +=1

    # calculate the number of votes each candidate recived and the percentage
    # uset get function to cound the percentage

votes_output= "" 
for candi in Candidates_Votes:
    # get the vote count and percentage
    votes = Candidates_Votes.get(candi)
    votes_percentage = (float(votes)/float(Total_Votes))*100


    # format the votes output
    votes_output += f"{candi}: {votes_percentage:.2f}%  ({votes})\n "

     # find out the winning candidate
    if votes > WinningCount:
      WinningCount = votes
      winning_candidate = candi

    
    # generate the output
output = (f"Election Results \n\n"
          f"-----------------------------\n\n"
          f" Total Votes: {Total_Votes}\n\n"
          f"-----------------------------\n\n"
          f"{votes_output}\n"
          f"-----------------------------\n\n"
          f" Winner: {winning_candidate}\n\n"
          f"-----------------------------")



print(output)

# print the results and export the data to the text file created
with open(output_file, "w") as textFile:
    # write the output the text file open
    textFile.write(output)


# THe end 

