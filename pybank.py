import os
import csv
bank = os.path.join("Resources","budget_data.csv")

months = []
profit_loss = []


with open(bank, "r") as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')
  next(csvreader)

  for row in csvreader:
      months.append(row[0])
      profit_loss.append(int(row[1]))

      total_month = len(months)
      print(total_month)

      net_profitloss = sum(profit_loss)
      print(net_profitloss)
      
      avg_rev = round(net_profitloss/total_month, 2)
      max_profit = profit_loss[0]
      min_profit = profit_loss[0]


for x in range (len(profit_loss)):
  if profit_lossl[x]> max_profit:
       max_profit=profit_loss[x]
       max_profit_month=all_months[x]

  elif profit_loss[x]<min_profit:
       min_profit=profit_loss[x]
       min_profit_month=all_months[x]


print ("Financial Analysis")
print("Total No of Months:" + str(total_month))
print("Net Profit and Loss:" + str(net_profitloss))
print("Average Change in P/L:" + str(avg_rev))
print ("Maximum Profit:" + str(max_profit)+" " + "Month:" + " " +str(max_profit_month))
print ("Minimum Profit:" + str(min_profit) + " " +"Month:"+" "+ str(min_profit_month))


output_path = os.path.join("budget.txt")
with open(output_path, 'w') as txt:
  txt.writelines('Financial Analysis\n')
  txt.writelines("Total No of Months:" + str(total_month) + '\n')
  txt.writelines("Net Profit and Loss:" + str(net_profitloss) + '\n')
  txt.writelines("Average Change in P/L:" + str(avg_rev) + '\n')
  txt.writelines("Maximum Profit:" + str(max_profit)+" " + "Month:" + " " +str(max_profit_month)+ '\n')
  txt.writelines("Minimum Profit:" + str(min_profit) + " " +"Month:"+" "+ str(min_profit_month))
Message Input