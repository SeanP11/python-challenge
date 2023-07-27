import os
budgetdata = os.path.join("Resources", "budgetdata.csv")
with open(budgetdata) as csvfile:
    print(csvfile)

#number of months
print('Number of Months:', len(df)-1)

n_months = len(df)-1

#sum of profit/losses
Profit_losses = sum(df['Profit/Losses'])

print ('Total:', Profit_losses)

#greatest increase/decrease in profit
data=(df['Profit/Losses'])
highest_point = max(data)
lowest_point = min(data)
print('Greatest Increase in Profit', highest_point)
print('Greatest Decrease in Profit', lowest_point)


#Average Changes 
Avgdata=(df['Profit/Losses'])
Avgdata = pd.DataFrame.mean(data)
Avgdata= round(Avgdata, 2)
print('Average Changes', Avgdata)

