import random
import networkx as nx
import pandas as pd
import time
import os
import os.path
import glob

#五种删边方式，依次是FR里奇曲率，OR里奇曲率，介数中心性，节点度*节点度，随机。


t0 = time.time()
for csvfile in glob.iglob(os.path.join('.', '*.csv')):
    nowDir = os.path.split(csvfile)[0]
    filename = os.path.split(csvfile)[1]
    new_Dir = os.path.join(nowDir, "LCC_" + filename)
    data = pd.read_table(csvfile, sep = ',')
    data.columns = ['source','target','Fricci', 'Oricci','score','multiply_degree']
    
    Oricci_largest_components = []
    Fricci_largest_components = []
    score_largest_components = []
    DD_largest_components = []
    random_largest_components = []
    
    G = nx.Graph()
    for i in range(len(data)):
        source = data.get_value(i, 'source')
        target = data.get_value(i, 'target')
        Fricci = data.get_value(i, 'Fricci')
        Oricci = data.get_value(i, 'Oricci')
        DD = data.get_value(i, 'multiply_degree')
        score = data.get_value(i, 'score')
        G.add_edge(source, target, Oricci = Oricci, Fricci = Fricci,DD = DD,score = score)

    G1 = G.copy()
    G2 = G.copy()
    G3 = G.copy()
    G4 = G.copy()
    
    orderbyOricci = data.sort_values('Oricci')
    orderbyFricci = data.sort_values('Fricci')
    orderbyscore = data.sort_values('score',ascending = False)
    orderbyDD = data.sort_values('multiply_degree',ascending = False)
    
    print ('---------remove edges by ascending Ollivier ricci curvature----------')
    count_a = 0
    for k in orderbyOricci.index:
        Oricci_source = orderbyOricci.get_value(k, 'source')
        Oricci_target = orderbyOricci.get_value(k, 'target')
        G.remove_edge(Oricci_source, Oricci_target)
        Oricci_largest_components.append(len(max(nx.connected_components(G), key = len)))
        count_a += 1
        if count_a % 1000 == 0:
            print ('-------------Removed % f edges-------------'%count_a)
            print ('------------- % f seconds spent-------------'%(time.time()-t0))
    print ('remove edges % f'%count_a)
    
    
    print ('---------remove edges by ascending Forman ricci curvature----------')
    count_b = 0
    for x in orderbyFricci.index:
        Fricci_source = orderbyFricci.get_value(x, 'source')
        Fricci_target = orderbyFricci.get_value(x, 'target')
        G1.remove_edge(Fricci_source, Fricci_target)
        Fricci_largest_components.append(len(max(nx.connected_components(G1), key = len)))
        count_b += 1
        if count_b % 1000 == 0:
            print ('-------------Removed % f edges-------------'%count_b)
            print ('------------- % f seconds spent-------------'%(time.time()-t0))
    print ('remove edges % f'%count_b)
    
    
    print ('---------remove edges by descending betweenness centrality----------')
    count_c = 0
    for m in orderbyscore.index:
        score_source = orderbyscore.get_value(m, 'source')
        score_target = orderbyscore.get_value(m, 'target')
        G2.remove_edge(score_source, score_target)
        score_largest_components.append(len(max(nx.connected_components(G2), key = len)))
        count_c += 1
        if count_c % 1000 == 0:
            print ('-------------Removed % f edges-------------'%count_c)
            print ('------------- % f seconds spent-------------'%(time.time()-t0))
    print ('remove edges % f'%count_c)
    
    print ('---------remove edges by descending Degree*Degree----------')
    count_d = 0
    for x in orderbyDD.index:
        Wscore_source = orderbyDD.get_value(x, 'source')
        Wscore_target = orderbyDD.get_value(x, 'target')
        G3.remove_edge(Wscore_source, Wscore_target)
        DD_largest_components.append(len(max(nx.connected_components(G3), key = len)))
        count_d += 1
        if count_d % 1000 == 0:
            print ('-------------Removed % f edges-------------'%count_d)
            print ('------------- % f seconds spent-------------'%(time.time()-t0))
    print ('remove edges % f'%count_d)
    
    
    print ('----------remove edges by random----------')
    temp_index = [p for p in range(len(G4.edges()))]
    index = random.sample(temp_index, len(G4.edges()))
    a = list(G4.edges())
    for q in index:
        random_source = a[q][0]
        random_target = a[q][1]
        G4.remove_edge(random_source, random_target)
        random_largest_components.append(len(max(nx.connected_components(G4), key = len)))
        if q % 1000 == 0:
            print ('-------------Removed % f edges-------------'%q)
            print ('------------- % f seconds spent-------------'%(time.time()-t0))
    
    print ('----------save files----------')
    sheet = pd.DataFrame(Oricci_largest_components)
    sheet[1] = Fricci_largest_components
    sheet[2] = score_largest_components
    sheet[3] = DD_largest_components
    sheet[4] = random_largest_components
    
    t1 = time.time()
    print ('----------end----------')
    print ('time: %f s' % (t1 - t0))
    sheet.to_csv(new_Dir,header = None)
