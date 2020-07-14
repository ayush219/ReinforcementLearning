# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 04:06:19 2019

@author: Ayush
"""

#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Dataset
dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

#Implement Reinforcement 
import math
N=10000
d=10
ads_selected=[]
number_of_selections=[0]*d
sum_of_rewards=[0]*d
total_rewards=0
for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        if(number_of_selections[i]>0):            
            avg_reward=sum_of_rewards[i]/number_of_selections[i]
            delta_i=math.sqrt(3/2* math.log(n+1)/number_of_selections[i])
            upper_bound= avg_reward+delta_i
        else:
            upper_bound=100000
        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i
    ads_selected.append(ad)
    number_of_selections[ad]=number_of_selections[ad]+1
    reward=dataset.values[n,ad]
    sum_of_rewards[ad]=sum_of_rewards[ad]+reward
    total_rewards=total_rewards+reward

        
#Visualise
plt.hist(ads_selected)
plt.show()
