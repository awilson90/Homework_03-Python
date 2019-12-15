import os
import csv

output_file = "pyPollResult.txt"

candidates = []
unique = []            
percentages = []                                   ## election_data.csv saved in same folder as code to make the following lines to work 
vote = []

with open('election_data.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar='|')

    row = 0
    for i in reader:                                ## i is the dummy variable used to represent row number
                                                    ## Skip the header row.
        if row >= 1:
            candidates.append(i[2])

        row = row + 1

    total_votes = len(candidates)                    ### get total number of entries

    for j in set(candidates):               ###define lists and indexes
      unique.append(j)
      w = candidates.count(j)
      vote.append(w)
      v = round((w/total_votes)*100, 2)
      percentages.append(v)
        
        
line1 = '  Election Results'        ##summary
line2 = '  -------------------------'
line3 = '  Total Votes: %d' %(total_votes)
line4 = '  -------------------------'
output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
print(output)

for x in range(len(unique)):
    print(unique[x] + ": " + str(percentages[x]) +"% (" + str(vote[x])+ ")")        ##print percentages with concatenated values



with open(output_file,'w') as outputfile:
        outputfile.write(output)         
