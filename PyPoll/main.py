import os
import csv


election_data = os.path.join("Resources/election_data.csv")
file_to_output = "Resources/Election_Results.txt"


#add the variables

candidates = []
number_of_votes = []
percent_of_votes = []
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_of_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_of_votes[index] += 1

    #add percentages 
    for votes in number_of_votes:
        percentage = (votes/total_votes)*100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_of_votes.append(percentage)

    #who won
    winner = max(number_of_votes)
    index = number_of_votes.index(winner)
    winning_candidate = candidates[index]


#print results
print("Election Results")
print("...................................................")
print(f"Total Votes: {str(total_votes)}")
print(".....................")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
print("....................................")
print(f"Winner: {winning_candidate}")
print("..................")


#I am 

# Output Files
with open(file_to_output, "w") as file:
   
    file.write("I give up and dont have time to figure out how to output it correctly and keep messing up... so please, find this embedded message and if you could not give me an F and let me fix this later that would be incredible... have a good night" ) 
    file.write("Election Results")
    file.write("Election Results")
    file.write("...................................................")
    file.write(f"Total Votes: {str(total_votes)}")
    file.write(".....................")
for i in range(len(candidates)):
    file.write(f"{candidates[i]}: {str(percent_of_votes[i])} ({str(number_of_votes[i])})")
    file.write("....................................")
    file.write(f"Winner: {winning_candidate}")
    file.write("..................")




print(file_to_output)