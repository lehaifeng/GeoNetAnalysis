# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 16:51:19 2017

@author: Yan Li
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats 

#####直方图
filelist = ['1Ricci_SHS','2Ricci_USAA','3Ricci_SHT','4Ricci_CNA','5Ricci_SHM','6Ricci_OF',
            '7Ricci_USAP','8Ricci_ATC','9Ricci_EUR','10Ricci_CR','11Ricci_CUSA',
            '12Ricci_BA','13Ricci_ER','14Ricci_WS']
colorlist = ['#40E0D0','#9932CC','#F08080','#FF4500','#FF00FF','#6495ED','#ADFF2F','#FFFF00','#32CD32','#A52A2A','#696969','#BA55D3','#DB7093','#9370DB']
data = pd.read_csv(r'F:/new_experiments/last_version/nodes/13Ricci_ER.csv', sep = ',')
data.columns = ['nodeid', 'OR', 'FR', 'Degree']
fig = plt.figure(figsize=(10, 2), dpi=300)
plt.hist(data['OR'],bins=100,normed=True,color=colorlist[12])
plt.xlim(-1.5, 1)
plt.xticks([])
plt.yticks(fontsize=24)
plt.savefig(r'F:/new_experiments/last_version/OR/13Ricci_ER.png') 

#####折线图
plt.figure(figsize=(8, 6), dpi=300)
ricci = pd.read_csv(r'F:/new_experiments/last_version/edge_attack/edges_ricci/LCC_3all_SHT.csv',sep = ',',header = None)
plt.xlim(0,1)
plt.ylim(0,1)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

x = [ k/len(ricci[0]) for k in [float(i) for i in ricci[0]]]
Oricci = [k for k in [float(i) for i in ricci[6]]]
Fricci = [k for k in [i for i in ricci[7]]]
score = [k for k in [float(i) for i in ricci[8]]]
DD = [k for k in [float(i) for i in ricci[9]]]
random = [k for k in [float(i) for i in ricci[10]]]

plt.plot(x,Oricci,c='b',label="Removed by Ascending Ollivier Ricci Curvature Order")
plt.plot(x,Fricci,c = 'b',ls = '--',label="Removed by Ascending Forman Ricci Curvature Order")
plt.plot(x,score,c = 'r',label="Removed by Decending Betweenness Centrality Order")
plt.plot(x,DD,c = 'r',ls = '--',label="Removed by Decending Degree*Degree Order")
plt.plot(x,random,c = 'k',label="Removed by Random Order")


plt.legend(loc='upper right',fontsize=10)
plt.xlabel('Proportion of Removing Edges ',fontsize=24)
plt.ylabel('Proportion of LCC',fontsize=24)

plt.savefig(r'F:/new_experiments/last_version/edge_attack/edges_ricci/3LCC_SHT.png')

#####联合分布散点图

#tips = pd.read_csv(r'G:\paper\experiment\Forman\directed_weighted\score_ricci_airports.edge',header = None)
#data = tips[[2,3]]
#data.columns = ['Ricci Curvature','Betweenness Centrality']
#plt.figure(figsize=(8, 5), dpi=300)
#plt.xticks(fontsize=13.2)
#plt.yticks(fontsize=13.2)
#plt.xlabel(fontsize=18)
#plt.ylabel(fontsize=18)

#sns.set_context("talk", font_scale=1.3)
#g = sns.jointplot(x = "Ricci Curvature", y = "Betweenness Centrality", data=data.dropna(), kind="reg",size=8)
#g = g.annotate(stats.pearsonr,fontsize=16)
#g.savefig(r'G:\paper\experiment\Forman\directed_weighted\airports.png')
#plt.show()

