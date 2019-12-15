import os
import csv

output_file = "pyBankResult.txt"
                                                ## budget_data.csv saved in same folder as code to make the following lines to work 
dates = []
transactions = [] 
change = []

with open('budget_data.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar='|')

    row = 0
    for i in reader:                                ## i is the dummy variable used to represent row number
                                                    ## Skip the header row.
        if row >= 1:
            dates.append(i[0])                      ## append adds the row i
            transactions.append(i[1])

        row = row + 1

    months = len(dates)                             ## Print number of transaction in List for part 1

    transactions = [int(i) for i in transactions]   ## using list comprehension to perform conversion from str to int
    totals = sum(transactions)                      ##sum elements in list for part 2

    change = [y-x for x, y in zip(transactions[:-1], transactions[1:])]     ###subtract consecutive rows                                                ##Next, for change subtract last period from current period. Get the average from that list

    def Average(lst):                       ###define function to calculate average for any list
        return sum(lst) / len(lst) 
  
    average = Average(change)               ###use function for average change

    Greatest_Increase = max(change)         # Determine greatest increase and date
    Greatest_Increase_Date = str(dates[change.index(max(change))])
        
    Greatest_Decrease = min(change)         # Determine greatest decrease and date
    Greatest_Decrease_Date = str(dates[change.index(min(change))])

line0 = '                    '
line1 = '  Financial Analysis'
line2 = '  -------------------------'
line3 = '  Total Months: %d' %(months)
line4 = '  Total:$ %d' %(totals)
line5 = '  Average Change: ' '${:,.2f}'.format(average)
line6 = '  Greatest Increase in Profits:' + Greatest_Increase_Date + ' $'+ str(Greatest_Increase)
line7 = '  Greatest Decrease in Profits:' + Greatest_Decrease_Date + ' $'+ str(Greatest_Decrease)
output = line0 + '\n' + line1 + '\n' + line2 + '\n' + line3 + '\n' + line4 + '\n' + line5 + '\n' + line6 +'\n' + line7
print(output)

with open(output_file,'w') as outputfile:
        outputfile.write(output)         
