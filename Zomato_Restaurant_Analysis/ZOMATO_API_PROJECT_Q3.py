# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:47:45 2020

@author: prankhur
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zomato.csv',engine='python')

x_val = df['Restaurant Name'].value_counts().index
y_val = df['Restaurant Name'].value_counts().values

fix,ax = plt.subplots()
ax.barh(x_val[0:15],y_val[0:15])

for i, v in enumerate(y_val[0:15]):
    ax.text(v + 1, i , str(v), color='black', fontweight='bold')
    
plt.xlabel('Number of Outlets')
    
"""______________________________________end of part 1_______________________________"""

df_copy= df[df['Aggregate rating']>0]
x = df_copy['Aggregate rating']
plt.hist(x,bins=[1.5,2,2.5,3,3.5,4,4.5,5],edgecolor='black')
plt.rcParams["figure.figsize"] = (10,5)
plt.xlabel('Aggregate Rating')
plt.show()

"""_________________________________end of part 2___________________________________ """

df_copy2 = df.copy()
df_copy2.sort_values(by=['Votes'],ascending=False,inplace=True)
df_copy2.reset_index(drop=True,inplace=True)

fx2,ax2=plt.subplots()
ax2.barh(df_copy2['Restaurant Name'][0:11],df_copy2['Votes'][0:11])

for i, v in enumerate(df_copy2['Votes'][0:10]):
    ax2.text(v + 1, i , str(v), color='black', fontweight='bold')

plt.xlabel('Number of Votes')

"""___________________________end of part 3_________________________________________"""

df_USA = df[df['Country Code']==216]
df_USA = df_USA.dropna()

cuisine_US_dict={}
for i in df_USA['Cuisines']:
    x=i.split(',')
    for k in x:
        cuisine_US_dict[k.strip()] = cuisine_US_dict.get(k.strip(),0) + 1
    
cuisine_ncr_list= [(v,k) for k,v in cuisine_US_dict.items()]
cuisine_ncr_list.sort(reverse=True)

labels = [i[1] for i in cuisine_ncr_list]
values = [i[0] for i in cuisine_ncr_list]

fig1, ax1 = plt.subplots()
explode = [i/20 for i in range(1,11)]
ax1.pie(values[0:10],labels=labels[0:10], autopct='%1.1f%%', shadow=True, startangle=90,explode=explode)


"""____________________________________end of part 4___________________________________"""


df_india = df[df['Country Code']==1]
df_city_weighted = df_india[['City','Aggregate rating','Votes']]
df_city_weighted = df_city_weighted[df_city_weighted['Aggregate rating']>0]
df_city_weighted=df_city_weighted.dropna()
df_city_weighted.reset_index(inplace=True,drop=True)

city_dict={}
num_city_dict={}
rating_dict={}

for i in range(6513):
    city_dict[df_city_weighted['City'][i]] = city_dict.get(df_city_weighted['City'][i],0) + df_city_weighted['Votes'][i]
    num_city_dict[df_city_weighted['City'][i]] = num_city_dict.get(df_city_weighted['City'][i],0)+1

    
for i in range(6513):
    rating_dict[df_city_weighted['City'][i]] = rating_dict.get(df_city_weighted['City'][i],0) + df_city_weighted['Aggregate rating'][i]*df_city_weighted['Votes'][i]


for i in rating_dict:
    rating_dict[i]=round(rating_dict[i]/city_dict[i],2)



city_list = [i[0] for i in num_city_dict.items()]
num_list = [i[1] for i in num_city_dict.items()]
weighted_rating_list = [rating_dict[i] for i in city_list]
weighted_rating_str = [str(i) for i in weighted_rating_list]
weighted_rating_plot = [i*100 for i in weighted_rating_list]

plt.rcParams["figure.figsize"] = (12,10)
plt.scatter(num_list,city_list,s=weighted_rating_plot,alpha=0.3)


"""_______________________________________end of part 5___________________________________________"""







