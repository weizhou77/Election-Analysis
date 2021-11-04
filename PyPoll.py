# the data we need to retrieve
# 1. the total number of votes cast
# 2. a complete list of candidates who received votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

    #import csv
# Assign a variable for the file to load and the path
    #file_to_load = '/Users/weizhou/Desktop/Data Analytic Boot Camp/Module 3 Python/Election-Analysis/Resources/election_results.csv'

#file_variable = open(filename,mode) 
#mode: "r":open file to read
#"w": open a file to write to it, overwrite an existing file and create a file if one does not already exists
#"x": opena file for exclusive creation. if file not exist, will not create one
#"a": open a file to append data to an exising file. if not exist, will create one and add to the folder
#"+": open a file for reading and writing

#Open the election results and read the file
    #election_data = open(file_to_load,'r')
#To do: perform analysis

# close the file. it's important to disconnect the file to the program
    #election_data.close()

#Open the election results and read the file
    #with open(file_to_load) as election_data:
    
#To do: perform analysis
    #print(election_data)

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("/Users/weizhou/Desktop/Data Analytic Boot Camp/Module 3 Python/Election-Analysis/Resources", "election_results.csv")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options, a list
candidate_options = []

# 1. declare the empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Print the file object.
     #print(election_data)

    # print the header row
    headers = next(file_reader)
    #print(headers)

    #print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidates does not match any existing candidate, then add he/her to the candidate options
        if candidate_name not in candidate_options :
            # Add it to the list of candidates
            candidate_options.append(candidate_name)


            # Begin tracking that candidates's vote count.
            candidate_votes[candidate_name] = 0

        # add a vote to that candidate's count
        candidate_votes[candidate_name] +=1
# 3. Print total votes 
print(total_votes)

# Print Candidate options
print(candidate_options)

# print the candiate vote dictionary
print(candidate_votes)


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name


# Print the winning_candidate_summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner : { winning_candidate} \n"
    f"Winning Vote Count: { winning_count:,} \n"
    f"Winning Percentage : {winning_percentage:.1f}% \n"
    f"-------------------------\n")

print(winning_candidate_summary)







# ----------------------------Create and Write txt file-------------------------------------------------------------------------------------------------
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/weizhou/Desktop/Data Analytic Boot Camp/Module 3 Python/Election-Analysis/analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
        #txt_file.write("Hello World")
    # write three counties to the file
        #txt_file.write("Arapahoe, ")
        #txt_file.write("Denver, ")
        #txt_file.write("Jefferson")
    #write three counties to the file
        #txt_file.write("Arapahoe, Denver, Jefferson")
    # write three counties to the file with \n 
    txt_file.write("Arapahoe\nDenver\nJefferson")
    # Exercise
    txt_file.write("\nCounties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")

# using the with statement open the files as a text file.
    #outfile = open(file_to_save,"w")
# wtite some data to the file.
    #outfile.write("Hello World")









