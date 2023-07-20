import pandas as pd

df = pd.read_csv(r'python-challenge\PyPoll\Resources\election_data.csv')


#Number of Votes 
print('Number of Votes:', len(df)-1)
n_votes = len(df)-1

#list of candidates who received votes
candidate_list  = [""]