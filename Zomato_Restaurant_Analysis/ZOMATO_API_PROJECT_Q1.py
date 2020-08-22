 #-*- coding: utf-8 -*-
"""
Created on Thu May 14 14:03:36 2020

@author: prankhur
"""

# encoding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('zomato.csv',engine='python')

df_india = df[df['Country Code']==1]

""" __________________BAR GRAPH_________________________ """

num_delhi_ncr = 0
num_other_cities = 0

NCR= ['Gurgaon','Ghaziabad','Faridabad','New Delhi','Noida']

num_delhi_ncr = len(df_india[df_india['City'].isin(NCR)])
num_other_cities = len(df_india[~df_india['City'].isin(NCR)])

x_val = ["Delhi NCR","Other Cities"]
y_val = [num_delhi_ncr,num_other_cities]

plt.ylabel("Number of Restaurants")
plt.xlabel("City Grooup")
plt.bar(x_val,y_val)
plt.show()

"""________________________________________________________"""

"""____________________Cuisines not in NCR_________________ """

df_ncr = df_india[df_india['City'].isin(NCR)]
df_other_cities = df_india[~df_india['City'].isin(NCR)]

cuisines_ncr = df_ncr['Cuisines']
cuisines_other = df_other_cities['Cuisines']

cuisines_ncr_list=[]
cuisines_other_list=[]

for i in cuisines_ncr:
    x=i.split(',')
    for k in x:
        if(k.strip() not in cuisines_ncr_list):    
            cuisines_ncr_list.append(k.strip())
for i in cuisines_other:
    x=i.split(',')
    for k in x:
        if(k.strip() not in cuisines_other_list):
            cuisines_other_list.append(k.strip())

cuisines_not_in_ncr = [i for i in cuisines_other_list if i not in cuisines_ncr_list]

"""________________________________________________________"""

"""___________________TOP 10 Cuisines______________________"""


cuisine_dict={}
for i in df_india['Cuisines']:
    x=i.split(',')
    for k in x:
        cuisine_dict[k.strip()] = cuisine_dict.get(k.strip(),0) + 1
cuisine_list= [(v,k) for k,v in cuisine_dict.items()]
cuisine_list.sort(reverse=True)

for i in range(10):
    print(cuisine_list[i][1],cuisine_list[i][0])
    
"""__________________________________________________________"""


"""______________________Part1.4_Explanation____________________"""

cuisine_ncr_dict={}
for i in df_ncr['Cuisines']:
    x=i.split(',')
    for k in x:
        cuisine_ncr_dict[k.strip()] = cuisine_ncr_dict.get(k.strip(),0) + 1
cuisine_ncr_list= [(v,k) for k,v in cuisine_ncr_dict.items()]
cuisine_ncr_list.sort(reverse=True)


cuisine_other_dict={}
for i in df_other_cities['Cuisines']:
    x=i.split(',')
    for k in x:
        cuisine_other_dict[k.strip()] = cuisine_other_dict.get(k.strip(),0) + 1
cuisine_other_list= [(v,k) for k,v in cuisine_other_dict.items()]
cuisine_other_list.sort(reverse=True)

    
#graph_NCR
x_axis_NCR = [i[1] for i in cuisine_ncr_list[0:15]]
y_axis_NCR = [i[0] for i in cuisine_ncr_list[0:15]]

x_axis_OTHER = [i[1] for i in cuisine_other_list[0:15]]
y_axis_OTHER = [i[0] for i in cuisine_other_list[0:15]]

plt.rcParams["figure.figsize"] = (17,5)
plt.bar(x_axis_NCR,y_axis_NCR)
plt.title('Cuisines in NCR')
plt.show()

plt.rcParams["figure.figsize"] = (17,5)
plt.bar(x_axis_OTHER,y_axis_OTHER)
plt.title('Cuisines in Other parts of India')
plt.show()


"""_____________________________________________________________"""





