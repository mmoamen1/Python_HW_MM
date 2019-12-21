import os
import csv
import statistics
os.chdir(os.path.dirname(os.path.abspath(__file__)))
election_data = os.path.join('Resources', 'election_data.csv')
num_of_votes = 0
name_candidates = []
final_candidates = []
percentages = []
frs_votes = 0
scnd_votes = 0
thrd_votes = 0
frth_votes = 0

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    next(csvreader)
    for row in csvreader:
        num_of_votes += 1
        if row[2] not in name_candidates:
            name_candidates.append(row[2])
        if row[2] == name_candidates[0]:
            frs_votes += 1
        elif row[2] == name_candidates[1]:
            scnd_votes += 1
        elif row[2] == name_candidates[2]:
            thrd_votes += 1
        else:
            frth_votes += 1
            
    frst_per = round((frs_votes/num_of_votes) * 100)
    scnd_per = round((scnd_votes/num_of_votes) * 100)
    thrd_per = round((thrd_votes/num_of_votes) * 100)
    frth_per = round((frth_votes/num_of_votes) * 100)
    final_candidates.append(name_candidates[0])
    final_candidates.append(name_candidates[1]) 
    final_candidates.append(name_candidates[2]) 
    final_candidates.append(name_candidates[3])    
    percentages.append(frst_per)
    percentages.append(scnd_per)
    percentages.append(thrd_per)
    percentages.append(frth_per)
    winner_perc = max(percentages)
    index = percentages.index(winner_perc)
    winner = final_candidates[index]
 
    print("Election result")
    print(f"Total Votes: {num_of_votes}")
    print(f"{name_candidates[0]}: {frst_per}% ({frs_votes})")
    print(f"{name_candidates[1]}: {scnd_per}% ({scnd_votes})")
    print(f"{name_candidates[2]}: {thrd_per}% ({thrd_votes})")
    print(f"{name_candidates[3]}: {frth_per}% ({frth_votes})")
    print(f"Winner is {winner}")
    with open('Pypollresult.csv', 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Election result"])
        csvwriter.writerow([f"Total Votes: {num_of_votes}"])
        csvwriter.writerow([f"{name_candidates[0]}: {frst_per}% ({frs_votes})"])
        csvwriter.writerow([f"{name_candidates[1]}: {scnd_per}% ({scnd_votes})"])
        csvwriter.writerow([f"{name_candidates[2]}: {thrd_per}% ({thrd_votes})"])
        csvwriter.writerow([f"{name_candidates[3]}: {frth_per}% ({frth_votes})"])
        csvwriter.writerow([f"Winner is {winner}"])