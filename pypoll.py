import os
import csv
pypoll = os.path.join("Resources","election_data.csv")

voters = []
candidate = []
unique_candidate = []
voter_list=[]
percentage=[]
vote=0

with open(pypoll, "r") as csvfile:

   csvreader = csv.reader(csvfile, delimiter=',')
   next(csvreader)

   for row in csvreader:
       candidate.append(row[2])
       voters.append(row[0])
       if row[2] not in unique_candidate:
           unique_candidate.append(row[2])

   for y in range(len(unique_candidate)):
       vote = 0
       for x in range(len(candidate)):
           if unique_candidate[y] == candidate[x]:
               vote = vote + 1
       voter_list.append(vote)
       percentage.append(round(vlist[y]/len(candidate)*100,2))

   for y in range(len(unique_candidate)):
       print(unique_candidate [y], vlist[y])


   print("Election Results")
   print("Total Votes:" + str(len(candidate)))
   for y in range(len(unique_candidate)):
       print((unique_candidate[y])+":"+"  "+ str(vlist[y])+"  " + str(percentage[y])+'\n')