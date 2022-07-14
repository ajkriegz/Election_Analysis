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
#other options:
#file_to_load = os.path.join("resources", "election_results.csv")
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#os.path should work, but the directory is not automatically set to the same file when I run the code in terminal

#Perform analysis

#initialize vote counter at 0
total_votes = 0

#Declare empty lists and dictionaries
candidate_options = []
candidate_votes = {}

#Declare variables for the winning candidate
winning_candidate = "" #empty string value
winning_count = 0
winning_percentage = 0

with open(file_to_load, 'r') as election_data:

    #To do: read and analyze data
    file_reader=csv.reader(election_data)

    #Read and skip the header row in the count
    headers = next(file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        total_votes += 1

        #Add candidate names to the list
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal and candidate results to the terminal
    election_results = (
        f"\nElectionResults\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    txt_file.write(election_results)

#calculate vote percentages and output each candidate's results
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: received {vote_percentage:,.1f}% of the vote.")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:,.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

#Determine winning vote counts and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name   

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:,.1f}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    
    