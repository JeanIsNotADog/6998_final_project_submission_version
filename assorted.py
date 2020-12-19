import pandas as pd
import matplotlib.pyplot as plt
import datetime

# plot histogram
df = pd.read_csv('train/phase2/Election_model_predict_new.csv')
# counts = df.groupby('target').size().to_list()
plt.hist(df['target'])
plt.show()

# find tweets with disagreement scores
df_covid = pd.read_csv('train/phase2/Covid_model_predict_new.csv')
df_election = pd.read_csv('train/phase2/Election_model_predict_new.csv')
df_covid['time'] = df_covid.apply(lambda row: datetime.datetime.strptime(row.time, '%a %b %d %H:%M:%S %z %Y').timestamp(), axis=1)
df_election['time'] = df_election.apply(lambda row: datetime.datetime.strptime(row.time, '%a %b %d %H:%M:%S %z %Y').timestamp(), axis=1)
df_covid = df_covid.sort_values('text')
df_election = df_election.sort_values('text')

cnt = 0
ele_cnt = 0
for i in range(len(df_election)):
    if abs(df_covid.iloc[i]['target'] - df_election.iloc[i]['target']) > 2:
        print(df_covid.iloc[i]['label'], df_covid.iloc[i]['target'], df_election.iloc[i]['target'], df_covid.iloc[i]['text'])
        if df_covid.iloc[i]['label'] == 'election':
            ele_cnt += 1
        cnt += 1
print(cnt, ele_cnt)