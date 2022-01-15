
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []

# Declare the empty dictionary.
candidate_votes = {}

# Declare a varaible for winner candidate and winning count tracacker equal to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # rea the file object with the reader function
    file_reader = csv.reader(election_data)

    # print the header row.
    headers = next(file_reader)
    #print(headers)

    # print each row in the csv file.
    for row in file_reader:
        # print (row)
        # 2. Add to the total vote count. total_votes  = total_votes + 1
        total_votes += 1

        # print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to the lsit of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            # we're setting each candidate's vote count to zero. 
            # once we set it to zero, then we can start tallying the votes to each candidate
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count. 
        # we put this out of the if statement but aligned with the for loop
        # so that it will count is incremented as we iterate through each row
        candidate_votes[candidate_name] +=1

    # Determine the percentage of votes for ach candidate by lopping through the counts
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate the percentage of votes, and formulat in two decimal places
        # "{:.2f}".format
        vote_percentage = float(votes)/float(total_votes) * 100 

        # 4. Print the candidate name and percentage of votes
        #print out each candidate's name, vote count, and percentage of vote to the terminal.
        # vote_percentage :.1f / in one decimal place
        print(f"{candidate_name}: {vote_percentage:.1f} % ({votes:,})\n") 

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set winning_candidate equal to candidate name
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f"-------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------\n"
    )
    print(winning_candidate_summary)



# print the candidate vote dictionary
print(candidate_votes)

# print the candidate list.
print(candidate_options)
    
# 3. print the total votes.
print(total_votes)

# Accumulator, count up all the votes by initialize a variable.
# accoumulator will increment by 1 as we read each row in the for loop




#using the open() function with the "w" mode we will warite data to the file
#outfile = open(file_to_save,"w")
#write some data to the file.
#outfile.write("Hello World")
#close the file
#outfile.close()

# using the with statement oepn the file as a text file.
#with open(file_to_save,"w") as txt_file:
    #write some data to the file
   # txt_file.write("end world")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    # or using txt_file.write("Arapahoe, Denver, Jefferson")

    #\n on next line(return, new line)
    #txt_file.write("\nhi\nbye")