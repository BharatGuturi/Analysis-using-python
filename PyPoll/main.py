from collections import Counter
import os   #to import the os module
import csv  #to import the csv module
csvpath = os.path.join("Resources", "election_data.csv")       #path to csv
file_to_output = os.path.join("analysis", "PyPoll_results.txt")

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)        #header
    candidate_list = []
    Total_votes = 0
    Candidate_count = 0
    for row in csvreader:
        candidate_list.append(row[2])

    #printing to terminal and output file
    f = open(file_to_output, "w")
    print("Election Results", '\n')
    f.writelines(["Election Results", '\n'])
    print("--------------------", '\n')
    f.writelines(["--------------------", '\n'])
    Total_votes = len(candidate_list)           #Total number of votes
    print("Total Votes : ", Total_votes, '\n')
    f.writelines(["Total Votes : ", str(Total_votes), '\n'])
    print("---------------------", '\n')
    f.writelines(["---------------------", '\n'])

    limit = len(candidate_list)
    Each_candidate = Counter(candidate_list)
    for candidate in Each_candidate:                #Each candidate votes and percentage
        percent_Candidate = round((Each_candidate.get(candidate)*100)/Total_votes,3)
        vote_Number = Each_candidate.get(candidate)
        print(candidate, '\t', percent_Candidate, "%", "(",Each_candidate.get(candidate), ")", '\n')
        f.writelines([str(candidate), '\t', str(percent_Candidate), "%", "(",str(Each_candidate.get(candidate)), ")", '\n'])
    print("---------------------", '\n')
    f.writelines(["---------------------", '\n'])
    #Determining Winner
    key_list = list(Each_candidate.keys())
    val_list = list(Each_candidate.values())
    winner_Candidate = max(Each_candidate.values())
    position = val_list.index(winner_Candidate)
    print("Winner: ", key_list[position], '\n')
    f.writelines(["Winner: ", str(key_list[position]), '\n'])
    print("---------------------")
    f.writelines(["---------------------", '\n'])
    f.close()


    