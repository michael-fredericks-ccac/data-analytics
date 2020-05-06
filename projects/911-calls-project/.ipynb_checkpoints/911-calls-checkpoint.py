import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

#create sqlite3 db
conn = sqlite3.connect('911-calls.db')
cur = conn.cursor()

#read in 911.csv as a dataframe
data = pd.read_csv('911.csv')

#import csv to sqlite3:
data.to_sql('data', conn, if_exists='replace')

#select title and timeStamp columns from SQL database
sql = ('SELECT title, timeStamp FROM data')
df = pd.read_sql_query(sql, conn)

#close db conn
cur.close()
conn.close()

#create new column of string that include only first word of strings in the title column
df['reason'] = df['title'].apply(lambda x: x.split(':')[0])

#change timeStamp column from string to datetime type
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#create new columns for hour, month, and day of the week
df['hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['month'] = df['timeStamp'].apply(lambda x: x.month)
df['dayofweek'] = df['timeStamp'].apply(lambda x: x.dayofweek)

#remap day of the week columns from numbers 0-6 to weekday abbreviations ('Sun' - 'Sat')
dmap = {0: 'Sun',
        1: 'Mon',
        2: 'Tue',
        3: 'Wed',
        4: 'Thu',
        5: 'Fri',
        6: 'Sat',
       }
df['dayofweek'] = df['dayofweek'].map(dmap)

#create violinplot for distributions of calls for every hour by reason
plt.figure(figsize=(12,8))
sns.set_style('whitegrid')
sns.violinplot(x='hour', y='reason', data=df)
#save fig as 'hourbyreason_vp.png'
plt.savefig('hourbyreason_vp.png')

#now look at distplot for each reason
g = sns.FacetGrid(data=df, col='reason', height=6, aspect=1)
g.map(sns.distplot, 'hour', kde=False)
plt.savefig('hourbyreason_dp.png')

#create boxplots for each reason, looking at the distribution of calls per hour by day of the week
for i in df['reason'].unique():
    plt.figure(figsize=(12,8))
    plt.title(i)
    fn = (i + '_bp.png').lower()
    sns.boxplot(x='hour', y='dayofweek', data=df[df['reason'] == i])
    plt.savefig(fn)
    
#lastly create a heatmap to show the number of calls by month and reason
bymonth = df.groupby(['month', 'reason']).count()['title'].unstack()
plt.figure(figsize=(10,12))
sns.heatmap(bymonth)
plt.savefig('monthbyreason_hm.png')
