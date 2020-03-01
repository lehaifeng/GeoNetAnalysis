# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 16:51:19 2017

@author: Yan Li
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats


plt.figure(figsize=(8, 6), dpi=300)
node = pd.read_csv(r'F:/new_experiments/last_version/node_attack/LCC_1NodeRicci_SHS.csv',header = None)
plt.xlim(0,1)
plt.ylim(0,1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

x = [ k/len(node[0]) for k in [float(i) for i in node[0]]]
Oricci = [k for k in [float(i) for i in node[7]]]
Fricci = [k for k in [float(i) for i in node[8]]]
Betweenness = [k for k in [float(i) for i in node[9]]]
degree = [k for k in [float(i) for i in node[10]]]
Algebraic_connectivity = [k for k in [float(i) for i in node[11]]]
random = [k for k in [float(i) for i in node[12]]]


plt.plot(x,random,c = 'k',label = "Removed by Random Order")
plt.plot(x,degree,c='r',label="Removed by Descending Degree Order")
plt.plot(x,Betweenness,c = 'r',ls = '--',label="Removed by Descending Betweenness Order")
plt.plot(x,Oricci,c='b',label="Removed by Ascending Ollivier Ricci Curvature Order")
plt.plot(x,Fricci,c='b',ls = '--',label="Removed by Ascending Forman Ricci Curvature Order")
plt.plot(x,Algebraic_connectivity,c='#FF8C00',label="Removed by Ascending Algebraic Connectivity Order")

         
plt.legend(loc='upper right',fontsize=10)
plt.xlabel('Proportion of Removing Nodes ',fontsize=24)
plt.ylabel('Proportion of LCC',fontsize=24)
plt.savefig(r'F:/new_experiments/last_version/node_attack/LCC_1NodeRicci_SHS.png')
