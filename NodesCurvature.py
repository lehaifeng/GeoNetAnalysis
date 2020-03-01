# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:37:47 2020

@author: Yan Li
"""


import networkx as nx
import pandas as pd
import os
import os.path
import glob

datapath = glob.glob(r'F:/new_experiments/new/Ricci_*.csv')
for csvfile in datapath:
    nowDir = os.path.split(csvfile)[0]
    filename = os.path.split(csvfile)[1]
    new_Dir = os.path.join(nowDir, "node_" + filename)
    data = pd.read_table(csvfile, sep = ',')
    data.columns = ['source', 'target', 'FR', 'OR']
    
    Gd1 = nx.DiGraph()
    for i in range(len(data)):
        source = str(data.get_value(i,'source'))
        target = str(data.get_value(i,'target'))
        FR = str(data.get_value(i,'FR'))
        OR = str(data.get_value(i,'OR'))
        if source != target:
            Gd1.add_edge(source,target,FR=FR,OR=OR)
        
    print ('computing ricci curvature for nodes in directed networks:',filename)

    index = []
    for n in Gd1.nodes():
        FRsum = 0  # sum of the neighbor Ricci curvature
        ORsum = 0
        if Gd1.degree(n) != 0:
            for nbr in Gd1.neighbors(n):
                if 'FR' in Gd1[n][nbr]:
                    FR = float(Gd1[n][nbr]['FR'])
                    FRsum = FRsum + FR
                if 'OR' in Gd1[n][nbr]:
                    OR = float(Gd1[n][nbr]['OR'])
                    ORsum = ORsum + OR
    
            # assign the node Ricci curvature to be the average of node's adjacency edges
            FR = FRsum / Gd1.degree(n)
            OR = ORsum / Gd1.degree(n)
            Gd1.node[n]['FR'] = FR
            Gd1.node[n]['OR'] = OR
            Gd1.node[n]['degree'] = Gd1.degree(n)
            index.append([int(n), FR, OR, Gd1.degree(n)])
    
    name = ['nodeid','FR','OR','degree']
    node_ricci = pd.DataFrame(columns=name,data=index)
    node_ricci.to_csv(new_Dir,index=None)
