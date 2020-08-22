# -*- coding: utf-8 -*-
"""
Created on Fri May 15 16:16:07 2020

@author: prankhur
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zomato.csv',engine='python')

df_india = df[df['Country Code']==1]
df_india.reset_index(drop=True,inplace=True)


"""___________________________________Number of Votes___________________________________________"""

df_india_votes_review = df_india[['Restaurant ID','Restaurant Name','Votes','Aggregate rating']].copy()
df_india_votes_review = df_india_votes_review[(df_india_votes_review['Votes']>0)]
df_india_votes_review = df_india_votes_review[(df_india_votes_review['Aggregate rating']>0)]
df_india_votes_review.reset_index(drop=True,inplace=True)

df_india_votes_review['Rating_Bucket'] = ""
df_india_votes_review['Votes_Bucket'] = ""


for i in range(6513):
    
    if(df_india_votes_review['Votes'][i] < 500):
        df_india_votes_review['Votes_Bucket'][i] = "0-500"
    elif(df_india_votes_review['Votes'][i] < 1000):
        df_india_votes_review['Votes_Bucket'][i] = "500 - 1000"
    elif(df_india_votes_review['Votes'][i] < 2000):
        df_india_votes_review['Votes_Bucket'][i] = "1000 - 2000"
    elif(df_india_votes_review['Votes'][i] < 3000):
        df_india_votes_review['Votes_Bucket'][i] = "2000 - 3000"
    elif(df_india_votes_review['Votes'][i] > 4000):
        df_india_votes_review['Votes_Bucket'][i] = "3000 - 4000"
    else:
        df_india_votes_review['Votes_Bucket'][i] = "4000 and above"
    
    if(df_india_votes_review['Aggregate rating'][i] > 4.5):
        df_india_votes_review['Rating_Bucket'][i] = "4.5 - 5.0"
    elif(df_india_votes_review['Aggregate rating'][i] > 4.0):
        df_india_votes_review['Rating_Bucket'][i] = "4.0 - 4.5"
    elif(df_india_votes_review['Aggregate rating'][i] > 3.5):
        df_india_votes_review['Rating_Bucket'][i] = "3.5 - 4.0"
    elif(df_india_votes_review['Aggregate rating'][i] > 3.0):
        df_india_votes_review['Rating_Bucket'][i] = "3.0 - 3.5"
    elif(df_india_votes_review['Aggregate rating'][i] > 2.5):
        df_india_votes_review['Rating_Bucket'][i] = "2.5 - 3.0"
    else:
        df_india_votes_review['Rating_Bucket'][i] = "Below 2.5"
        
        
df_india_votes_review_cost1 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="0-500"]
df_india_votes_review_cost2 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="500 - 1000"]
df_india_votes_review_cost3 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="1000 - 2000"]
df_india_votes_review_cost4 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="2000 - 3000"]
df_india_votes_review_cost5 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="3000 - 4000"]
df_india_votes_review_cost6 = df_india_votes_review[df_india_votes_review['Votes_Bucket']=="4000 and above"]


labels1 = df_india_votes_review_cost1['Rating_Bucket'].value_counts().index
sizes1 = df_india_votes_review_cost1['Rating_Bucket'].value_counts().values

labels2 = df_india_votes_review_cost2['Rating_Bucket'].value_counts().index
sizes2 = df_india_votes_review_cost2['Rating_Bucket'].value_counts().values

labels3 = df_india_votes_review_cost3['Rating_Bucket'].value_counts().index
sizes3 = df_india_votes_review_cost3['Rating_Bucket'].value_counts().values

labels4 = df_india_votes_review_cost4['Rating_Bucket'].value_counts().index
sizes4 = df_india_votes_review_cost4['Rating_Bucket'].value_counts().values

labels5 = df_india_votes_review_cost5['Rating_Bucket'].value_counts().index
sizes5 = df_india_votes_review_cost5['Rating_Bucket'].value_counts().values

labels6 = df_india_votes_review_cost6['Rating_Bucket'].value_counts().index
sizes6 = df_india_votes_review_cost6['Rating_Bucket'].value_counts().values

fig1, ax1 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax1.pie(sizes1,labels=labels1, autopct='%1.1f%%', shadow=True, startangle=150)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('0 - 500',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig2, ax2 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax2.pie(sizes2,labels=labels2, autopct='%1.1f%%', shadow=True, startangle=150)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('500 - 1000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig3, ax3 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax3.pie(sizes3,labels=labels3, autopct='%1.1f%%', shadow=True, startangle=150)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('1000 - 2000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig4, ax4 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax4.pie(sizes4,labels=labels4, autopct='%1.1f%%', shadow=True, startangle=150)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('2000 - 3000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig5, ax5 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax5.pie(sizes5,labels=labels5, autopct='%1.1f%%', shadow=True, startangle=150)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('3000 - 4000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig6, ax6 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 12.0
ax6.pie(sizes6,labels=labels6, autopct='%1.1f%%', shadow=True, startangle=150)
ax6.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('4000 and above',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()



"""_________________________________________________________________________________________"""
"""___________________________________No of Cuisines___________________________________________"""

df_india_cuisine_review = df_india[['Restaurant ID','Restaurant Name','Cuisines','Aggregate rating']].copy()
df_india_cuisine_review = df_india_cuisine_review[(df_india_cuisine_review['Aggregate rating']>0)]
df_india_cuisine_review.reset_index(drop=True,inplace=True)

df_india_cuisine_review['No_Cuisines'] = 0

for i in range(6513):
    x = df_india_cuisine_review['Cuisines'][i].split(',')
    df_india_cuisine_review['No_Cuisines'][i]=len(x)
df_india_cuisine_review.drop(['Cuisines'],axis=1,inplace=True)

df_india_cuisine_review['Rating_Bucket'] = ""
df_india_cuisine_review['Cuisine_Bucket'] = ""

for i in range(6513):
    
    if(df_india_cuisine_review['No_Cuisines'][i] < 4):
        df_india_cuisine_review['Cuisine_Bucket'][i] = "1 - 3"
    elif(df_india_cuisine_review['No_Cuisines'][i] <7):
        df_india_cuisine_review['Cuisine_Bucket'][i] = "4 - 6"
    else:
        df_india_cuisine_review['Cuisine_Bucket'][i] = "7 - 8"
    
    if(df_india_cuisine_review['Aggregate rating'][i] > 4.5):
        df_india_cuisine_review['Rating_Bucket'][i] = "4.5 - 5.0"
    elif(df_india_cuisine_review['Aggregate rating'][i] > 4.0):
        df_india_cuisine_review['Rating_Bucket'][i] = "4.0 - 4.5"
    elif(df_india_cuisine_review['Aggregate rating'][i] > 3.5):
        df_india_cuisine_review['Rating_Bucket'][i] = "3.5 - 4.0"
    elif(df_india_cuisine_review['Aggregate rating'][i] > 3.0):
        df_india_cuisine_review['Rating_Bucket'][i] = "3.0 - 3.5"
    elif(df_india_cuisine_review['Aggregate rating'][i] > 2.5):
        df_india_cuisine_review['Rating_Bucket'][i] = "2.5 - 3.0"
    else:
        df_india_cuisine_review['Rating_Bucket'][i] = "Below 2.5"


df_india_cuisine_review1 = df_india_cuisine_review[df_india_cuisine_review['Cuisine_Bucket']=="1 - 3"]
df_india_cuisine_review2 = df_india_cuisine_review[df_india_cuisine_review['Cuisine_Bucket']=="4 - 6"]
df_india_cuisine_review3 = df_india_cuisine_review[df_india_cuisine_review['Cuisine_Bucket']=="7 - 8"]



labels1 = df_india_cuisine_review1['Rating_Bucket'].value_counts().index
sizes1 = df_india_cuisine_review1['Rating_Bucket'].value_counts().values

labels2 = df_india_cuisine_review2['Rating_Bucket'].value_counts().index
sizes2 = df_india_cuisine_review2['Rating_Bucket'].value_counts().values

labels3 = df_india_cuisine_review3['Rating_Bucket'].value_counts().index
sizes3 = df_india_cuisine_review3['Rating_Bucket'].value_counts().values



fig1, ax1 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax1.pie(sizes1,labels=labels1, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('1 - 3',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig2, ax2 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax2.pie(sizes2,labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('4 - 6',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig3, ax3 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax3.pie(sizes3,labels=labels3, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('7 - 8',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

"""__________________________________________________________________________________________"""
"""___________________________________Average Cost___________________________________________"""

df_india_cost_review = df_india[['Restaurant ID','Restaurant Name','Average Cost for two','Aggregate rating']].copy()


df_india_cost_review['Rating_Bucket'] = ""
df_india_cost_review['Price_Bucket'] = ""

for i in range(8652):
    
    if(df_india_cost_review['Average Cost for two'][i] > 5000):
        df_india_cost_review['Price_Bucket'][i] = "above 5000"
    elif(df_india_cost_review['Average Cost for two'][i] > 4000):
        df_india_cost_review['Price_Bucket'][i] = "4000 - 5000"
    elif(df_india_cost_review['Average Cost for two'][i] > 3000):
        df_india_cost_review['Price_Bucket'][i] = "3000 - 4000"
    elif(df_india_cost_review['Average Cost for two'][i] > 2000):
        df_india_cost_review['Price_Bucket'][i] = "2000 - 3000"
    elif(df_india_cost_review['Average Cost for two'][i] > 1000):
        df_india_cost_review['Price_Bucket'][i] = "1000 - 2000"
    else:
        df_india_cost_review['Price_Bucket'][i] = "1000 and less"
    
    if(df_india_cost_review['Aggregate rating'][i] > 4.5):
        df_india_cost_review['Rating_Bucket'][i] = "4.5 - 5.0"
    elif(df_india_cost_review['Aggregate rating'][i] > 4.0):
        df_india_cost_review['Rating_Bucket'][i] = "4.0 - 4.5"
    elif(df_india_cost_review['Aggregate rating'][i] > 3.5):
        df_india_cost_review['Rating_Bucket'][i] = "3.5 - 4.0"
    elif(df_india_cost_review['Aggregate rating'][i] > 3.0):
        df_india_cost_review['Rating_Bucket'][i] = "3.0 - 3.5"
    elif(df_india_cost_review['Aggregate rating'][i] > 2.5):
        df_india_cost_review['Rating_Bucket'][i] = "2.5 - 3.0"
    else:
        df_india_cost_review['Rating_Bucket'][i] = "Below 2.5"
        
df_india_cost_review = df_india_cost_review[df_india_cost_review['Aggregate rating']>0]
df_india_cost_review = df_india_cost_review[df_india_cost_review['Average Cost for two']>0]


df_india_cost_review_cost1 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="above 5000"]
df_india_cost_review_cost2 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="4000 - 5000"]
df_india_cost_review_cost3 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="3000 - 4000"]
df_india_cost_review_cost4 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="2000 - 3000"]
df_india_cost_review_cost5 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="1000 - 2000"]
df_india_cost_review_cost6 = df_india_cost_review[df_india_cost_review['Price_Bucket']=="1000 and less"]


labels1 = df_india_cost_review_cost1['Rating_Bucket'].value_counts().index
sizes1 = df_india_cost_review_cost1['Rating_Bucket'].value_counts().values

labels2 = df_india_cost_review_cost2['Rating_Bucket'].value_counts().index
sizes2 = df_india_cost_review_cost2['Rating_Bucket'].value_counts().values

labels3 = df_india_cost_review_cost3['Rating_Bucket'].value_counts().index
sizes3 = df_india_cost_review_cost3['Rating_Bucket'].value_counts().values

labels4 = df_india_cost_review_cost4['Rating_Bucket'].value_counts().index
sizes4 = df_india_cost_review_cost4['Rating_Bucket'].value_counts().values

labels5 = df_india_cost_review_cost5['Rating_Bucket'].value_counts().index
sizes5 = df_india_cost_review_cost5['Rating_Bucket'].value_counts().values

labels6 = df_india_cost_review_cost6['Rating_Bucket'].value_counts().index
sizes6 = df_india_cost_review_cost6['Rating_Bucket'].value_counts().values

fig1, ax1 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax1.pie(sizes1,labels=labels1, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('above 5000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig2, ax2 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax2.pie(sizes2,labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('4000 - 5000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig3, ax3 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax3.pie(sizes3,labels=labels3, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('3000 - 4000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig4, ax4 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax4.pie(sizes4,labels=labels4, autopct='%1.1f%%', shadow=True, startangle=90)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('2000 - 3000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig5, ax5 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax5.pie(sizes5,labels=labels5, autopct='%1.1f%%', shadow=True, startangle=90)
ax5.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('1000 - 2000',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

fig6, ax6 = plt.subplots()
plt.rcParams["figure.figsize"] = (15,15)
plt.rcParams["font.size"] = 20.0
ax6.pie(sizes6,labels=labels6, autopct='%1.1f%%', shadow=True, startangle=90)
ax6.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('1000 and below',loc='right',fontdict={'size':20,'weight':'bold'})
plt.show()

"""_____________________________________________________________________________________"""

"""__________________________Specific Cuisines__________________________________________"""


df_india_cuisine_rating = df_india[['Restaurant ID','Restaurant Name','Cuisines','Aggregate rating']].copy()
df_india_cuisine_rating = df_india_cuisine_rating[df_india_cuisine_rating['Aggregate rating']>0]

df_india_cuisine_rating.reset_index(drop=True,inplace=True)

cuisine_num_dict={}
cuisine_rating_dict={}

for i in range(6513):
    x=df_india_cuisine_rating['Cuisines'][i].split(',')
    for k in x:
        cuisine_num_dict[k.strip()] = cuisine_num_dict.get(k.strip(),0) + 1
        cuisine_rating_dict[k.strip()] = cuisine_rating_dict.get(k.strip(),0) + df_india_cuisine_rating['Aggregate rating'][i]
        
for i in cuisine_num_dict:
    if(cuisine_num_dict[i]<50):
        del cuisine_rating_dict[i]

for i in cuisine_rating_dict:
    cuisine_rating_dict[i] = cuisine_rating_dict[i]/cuisine_num_dict[i]
    
cuisine_rating_list = [(v,k) for (k,v) in cuisine_rating_dict.items()]
cuisine_rating_list.sort(reverse=True)

x_val = [i[1] for i in cuisine_rating_list[0:30]]
y_val = [i[0] for i in cuisine_rating_list[0:30]]

plt.rcParams["figure.figsize"] = (12,10)
plt.barh(x_val,y_val)
plt.show()


"""___________________________________________________________________________________"""


"""_________________________________Locality Weighted_________________________________"""

df_locality_weighted = df_india[['Locality','Aggregate rating','Votes']]
df_locality_weighted = df_locality_weighted[df_locality_weighted['Aggregate rating']>0]

df_locality_weighted.reset_index(inplace=True,drop=True)

localities_dict={}
rating_dict={}

for i in range(6513):
    localities_dict[df_locality_weighted['Locality'][i]] = localities_dict.get(df_locality_weighted['Locality'][i],0) + df_locality_weighted['Votes'][i]

    
for i in range(6513):
    rating_dict[df_locality_weighted['Locality'][i]] = rating_dict.get(df_locality_weighted['Locality'][i],0) + df_locality_weighted['Aggregate rating'][i]*df_locality_weighted['Votes'][i]


for i in rating_dict:
    rating_dict[i]=rating_dict[i]/localities_dict[i]

sorted_weighted = [(v,k) for (k,v) in rating_dict.items()]
sorted_weighted.sort(reverse=True)

for i in sorted_weighted[0:10]:
    print(i[1])
"""__________________________________________________________________________________"""











































