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
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row)
    
    # Print the file object.
     #print(election_data)

# print the header row
    headers = next(file_reader)
    print(headers)


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

#close the file
    #outfile.close()

# Read the file object with the reader function
#import csv
#file_reader = csv.reader(election_data)

# Print each row in the csv file.

#for row in file_reader:
    #print(row)








