# The data we need to retrieve


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1

        print(total_votes)

        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] +=1

print(candidate_votes)

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    print(f"{candidate_name}: recieved {vote_percentage:.2f}% of the vote.")

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n------------\nArapahoe\nDenver\nJefferson")
    


#1. the total number of votes cast
#2. a comlpere lsit of candidates who recieved votes
#3. the percentage of votes each candiddate won
#4. the total number of votes each candidate won
#5. the winner of the election based on popular vote


