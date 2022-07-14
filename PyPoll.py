# The data we need to retrieve.
#1. Total number of votes cast
#2. complete list of candidates who received votes
#3. percentage of votes each candidate won
#4. total number of votes each candidate won
#5. winner of the election based on popular vote

#add our dependencies

import csv
import os
import random
import numpy

# file_variable = open(filename, mode)
# \resources\election_results.csv

# Assign a variable to load a file from path
# Assign a variable to save the pile to a path

file_to_load = 'C:/Users/ajkri/Documents/bootcamp/analysis_projects/Election_Analysis/resources/election_results.csv'
file_to_save = 'C:/Users/ajkri/Documents/bootcamp/analysis_projects/Election_Analysis/analysis/election_analysis.txt'
#file_to_save = os.path.join("analysis", "election_analysis.txt")

#file_to_load = os.path.join("resources", "election_results.csv")
#os.path should work, but the directory is different when I run the code in terminal

#Perform analysis

with open(file_to_load, 'r') as election_data:

    #To do: read and analyze data here
    file_reader=csv.reader(election_data)

    #Read and print the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file
    for row in file_reader:
        print(row)


#Close the file -- may be redundant with current instructions
#election_results.close()

#Create a filename variable to a direct or indirect path to the file
#Then use the open() function with 'w' mode to write data to the file, open as a text file


with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

