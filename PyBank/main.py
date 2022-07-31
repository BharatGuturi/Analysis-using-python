import os   #to import the os module
import csv  #to import the csv module


csvpath = os.path.join("Resources", "budget_data.csv")       #path to csv
file_to_output = os.path.join("analysis", "PyBank_results.txt")

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)        #header
    sum = 0
    sum2 = 0
    month = []
    month_count = 0
    changesinpl = []
    res_changesinpl = []
    avg_changes = 0
    month_year = []
    for row in csvreader:
        month.append(row[0].split("-")[0]) 
        sum = sum + int(row[1])         #net total amount of profit or loss over entire period
        changesinpl.append(row[1])
        month_year.append(row[0])
    limit = len(month)
    #print(limit)
    for indx, counter in enumerate(month):
        if indx == limit - 1:
            break
        elif month[indx] != month[indx + 1]:
            month_count = month_count + 1
            res_changesinpl.append(int(changesinpl[indx+1]) - int(changesinpl[indx]))       #The changes in "Profit/Losses" over the entire period
    #print(sum)                          #print the net total amount of profit or loss over the entire period
    #print(month_count + 1)              #print the total number of months
    #print(res_changesinpl)              #print changes in "Profit/Losses" over the entire period
    for value in res_changesinpl:
        sum2 = sum2 + value
    avg_changes = sum2/len(res_changesinpl)
    #print(avg_changes)                  #print average changes over entire period
    
    maxchange_pl = max(res_changesinpl)                     #determining the maximum change in profit/ loss
    #print(maxchange_pl)
    max_index = res_changesinpl.index(maxchange_pl)         #index of maximum change in profit/loss
    #print(max_index)
    max_month = month_year[max_index + 1]                   #determining the month which has maximum profit
    #print(max_month)
    
    minchange_pl = min(res_changesinpl)                     #determining the minimum value of change in profit/ loss
    #print(minchange_pl)
    min_index = res_changesinpl.index(minchange_pl)         #index of minimum value of change in profit/loss
    #print(min_index)
    min_month = month_year[min_index + 1]                   #determining the month which has minimum value of change
    #print(min_month)

    #printing to terminal
    print("Financial Analysis", '\n')
    print("*******************************", '\n')
    print("Total Months: ", int(len(month)), '\n')
    print("Total: ", "$",sum, '\n')
    print("Average Change: ", "$",round(avg_changes,2), '\n')
    print("Greatest Increase in Profits: "+ max_month + "($", maxchange_pl, ")", '\n')
    print("Greatest Decrease in Profits: "+ min_month + "($", minchange_pl, ")", '\n')

    #printing to output text file
    f = open(file_to_output, "w")
    f.writelines(["Financial Analysis", '\n'])
    f.writelines(["*******************************"])
    f.writelines(["Total Months: ", str(int(len(month))), '\n'])
    f.writelines(["Total: ", "$",str(sum),'\n'])  
    f.writelines(["Average Change: ", "$",str(round(avg_changes,2)), '\n'])
    f.writelines(["Greatest Increase in Profits: "+ str(max_month) + "($", str(maxchange_pl), ")", '\n'])
    f.writelines(["Greatest Decrease in Profits: "+ str(min_month) + "($", str(minchange_pl), ")", '\n'])
    f.close()

   
  
 