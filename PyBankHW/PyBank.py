import os
import csv
import statistics
num_months = 0
bud_list = []
avg_value = []
month_list = []
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data = os.path.join('Resources', 'budget.csv')
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        num_months += 1
        bud_list.append(int(row[1])) 
        month_list.append(row[0])
        tot_num = sum((bud_list)) 
    for i in range(0,85):
        avg_value.append((bud_list[i+1])-(bud_list[i]))
        max_num = max(avg_value)
        min_num = min(avg_value)
        mean_num = statistics.mean(avg_value)
    for i in avg_value:   
        if max_num == i:
            max_value = i
        elif min_num == i:
            min_value = i
    max_index = (avg_value.index(max_value))
    max_month = (month_list[max_index + 1])
    min_index = (avg_value.index(min_value))
    min_month = (month_list[min_index + 1])
    print(f"The total number of months: {num_months}")
    print(f"The total value: ${tot_num}")
    print(f"Greatest increase: {max_month} ${max_value}")
    print(f"Greatest decrease: {min_month} ${min_value}")
    print(f"The average change: ${mean_num}")
    with open('output.csv', 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([f"The total number of months: {num_months}"])
        csvwriter.writerow([f"Greatest increase: {max_month} ${max_value}"])
        csvwriter.writerow([f"Greatest decrease: {min_month} ${min_value}"])
        csvwriter.writerow([f"The total value: ${tot_num}"])
        csvwriter.writerow([f"The average change: ${mean_num}"])


    
    
            



#print(max_value)
#print(max_month)
#print(min_value)
#print(min_month)
#print(tot_num)
#print(mean_num)


    
        
       
     