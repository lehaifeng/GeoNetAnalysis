# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:07:00 2018

@author: Yan Li
"""

import pandas as pd
import random
import networkx as nx
import time


t0 = time.time()

data = pd.read_csv(r'F:/new_experiments/last_version/edge_attack/edges_ricci/4all_CNA.csv',sep = ',',header = None)
data.columns = ['source','target','FR', 'OR','BC','DD']
nodes = pd.read_csv(r'F:/new_experiments/last_version/node_attack/4NodeRicci_CNA.csv',sep = ',')
nodes.columns = ['nodeid', 'OR', 'FR', 'Degree', 'Betweenness', 'Algebraic_connectivity']


print ('-------------Create network-------------')
G = nx.Graph()
for i in range(len(data)):
    source = data.get_value(i, 'source')
    target = data.get_value(i, 'target')
    FR = data.get_value(i, 'FR')
    OR = data.get_value(i, 'OR')
    BC = data.get_value(i, 'BC')
    DD = data.get_value(i, 'DD')
    G.add_edge(source, target, FR = FR, OR = OR,BC=BC,DD=DD)


print ('-------------Sort values-------------')
orderbyOricci = nodes.sort_values('OR')
orderbyFricci = nodes.sort_values('FR')
orderbydegree = nodes.sort_values('Degree',ascending = False)
orderbyconnectivity = nodes.sort_values('Algebraic_connectivity')
orderbybetweenness = nodes.sort_values('Betweenness',ascending = False)

G1 = G.copy()
G2 = G.copy()
G3 = G.copy()
G4 = G.copy()
G5 = G.copy()
G6 = G.copy()

n = G.number_of_nodes()
N_rm = int(n)

tot_FLCC = [0] * (N_rm + 1)
giant_FLCC = len(max(nx.connected_components(G1), key = len))
tot_FLCC[0] = giant_FLCC

tot_OLCC = [0] * (N_rm + 1)
giant_OLCC = len(max(nx.connected_components(G), key = len))
tot_OLCC[0] = giant_OLCC

tot_DLCC = [0] * (N_rm + 1)
giant_DLCC = len(max(nx.connected_components(G2), key = len))
tot_DLCC[0] = giant_DLCC

tot_CLCC = [0] * (N_rm + 1)
giant_CLCC = len(max(nx.connected_components(G3), key = len))
tot_CLCC[0] = giant_CLCC

tot_BLCC = [0] * (N_rm + 1)
giant_BLCC = len(max(nx.connected_components(G4), key = len))
tot_BLCC[0] = giant_BLCC

tot_RLCC = [0] * (N_rm + 1)
giant_RLCC = len(max(nx.connected_components(G5), key = len))
tot_RLCC[0] = giant_RLCC


print ('-------------Remove nodes by ascending Oricci order-------------')
for a in range(N_rm):
    node = orderbyOricci.iat[a,0]
    G.remove_node(node)
    if G.number_of_nodes() == 0:
        break
    giant_OLCC = len(max(nx.connected_components(G), key = len))
    tot_OLCC[a+1] = giant_OLCC
    if a % 100 == 0:
        print ('-------------Removed % f nodes-------------'%a)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))

print ('-------------Remove nodes by ascending Fricci order-------------')
for b in range(N_rm):
    node = orderbyFricci.iat[b,0]
    G1.remove_node(node)
    if G1.number_of_nodes() == 0:
        break
    giant_FLCC = len(max(nx.connected_components(G1), key = len))
    tot_FLCC[b+1] = giant_FLCC
    if b % 100 == 0:
        print ('-------------Removed % f nodes-------------'%b)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))

print ('-------------Remove nodes by decending degree order-------------')
for c in range(N_rm):
    node = orderbydegree.iat[c,0]
    G2.remove_node(node)
    if G2.number_of_nodes() == 0:
        break
    giant_DLCC = len(max(nx.connected_components(G2), key = len))
    tot_DLCC[c+1] = giant_DLCC
    if c % 100 == 0:
        print ('-------------Removed % f nodes-------------'%c)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))

print ('-------------Remove nodes by ascending Algebraic_connectivity order-------------')
for d in range(N_rm):
    node = orderbyconnectivity.iat[d,0]
    G3.remove_node(node)
    if G3.number_of_nodes() == 0:
        break
    giant_CLCC = len(max(nx.connected_components(G3), key = len))
    tot_CLCC[d+1] = giant_CLCC
    if d % 100 == 0:
        print ('-------------Removed % f nodes-------------'%d)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))

print ('-------------Remove nodes by ascending Betweenness order-------------')
for e in range(N_rm):
    node = orderbybetweenness.iat[e,0]
    G4.remove_node(node)
    if G4.number_of_nodes() == 0:
        break
    giant_BLCC = len(max(nx.connected_components(G4), key = len))
    tot_BLCC[e+1] = giant_BLCC
    if e % 100 == 0:
        print ('-------------Removed % f nodes-------------'%e)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))


print ('-------------Remove nodes by random order-------------')
all_nodes = list(G5.nodes())
random.shuffle(all_nodes)

#remove all the edges adjacent to this node
for i in range(N_rm):
    node = all_nodes[i]
    G5.remove_node(node)
    if G5.number_of_nodes() == 0:
        break
    giant_RLCC = len(max(nx.connected_components(G5), key = len)) 
    tot_RLCC[i+1] = giant_RLCC
    if i % 100 == 0:
        print ('-------------Removed % f nodes-------------'%i)
        print ('------------- % f seconds spent-------------'%(time.time()-t0))

#
print ('-------------save files-------------')
sheet = pd.DataFrame(tot_OLCC)
sheet[1] = tot_FLCC
sheet[2] = tot_DLCC
sheet[3] = tot_BLCC
sheet[4] = tot_CLCC
sheet[5] = tot_RLCC


t1 = time.time()
print ('-------------end-------------')
print ('time: %f s' % (t1 - t0))
sheet.to_csv(r'F:/new_experiments/last_version/node_attack/LCC_4NodeRicci_CNA.csv',header = None)