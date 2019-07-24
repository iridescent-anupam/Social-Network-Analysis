
# coding: utf-8

# In[60]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

#demo graph
G0 = nx.Graph()
G0.add_edges_from([(0, 'A'),
                   (0, 2),
                   (0, 3),
                   (0, 5),
                   (1, 3),
                   (1, 6),
                   (3, 4),
                   (4, 5),
                   (4, 7),
                   (5, 8),
                   (8, 9)])



nx.draw_networkx(G0)

# density
dens = nx.density(G0)
print("Density =", dens)

#path length

asp = nx.average_shortest_path_length(G0)
print("Average Distance Between Pair of Nodes = ", asp)

#diameter

dia = nx.diameter(G0)
print("Diameter = ", dia)

#eccentricity

ecc = nx.eccentricity(G0)
print("Eccentricity =", ecc)

#radius a.k.a mininmum eccentricity

rad = nx.radius(G0)
print("Radius =", rad)

#Center of graph

cent = nx.center(G0)
print("Center =", cent)

#Degree Centrality

deg_cent = nx.degree_centrality(G0)
print("Degree Centrality =", deg_cent)

#closeness centrality

close_cent = nx.closeness_centrality(G0)
print("Closeness Centrality =", close_cent)


#betweenness centrality

bet_cent = nx.betweenness_centrality(G0)
print("Betweenness Centrality =", bet_cent)

#eigen vector centrality

eigen_cent = nx.eigenvector_centrality(G0)
print("Eigen Vector Cent =", eigen_cent)

#local clustering coefficent

loc_cc = nx.clustering(G0)
print("Local Clustering Cofficients= ", loc_cc)

#global clustering coefficent

gl_cc = nx.transitivity(G0)
print("Global Clustering Coefficient= ", gl_cc)

#average clustering coefficient

a_cc = nx.average_clustering(G0)
print("Average CLustering Coefficient= ", a_cc)

#degree assortativity coefficient

d_ac = nx.degree_assortativity_coefficient(G0)
print("Degree Assortativity Coefficient= ", d_ac)




# In[61]:


#Basic Graph 1

G1 = nx.Graph()
G1.add_edges_from([(0, 1),
                   (0, 2),
                   (0, 3),
                   (0, 4),
                   (0, 5)])

nx.draw_networkx(G1)
# density
dens = nx.density(G1)
print("Density =", dens)

#path length

asp = nx.average_shortest_path_length(G1)
print("Average Distance Between Pair of Nodes = ", asp)

#diameter

dia = nx.diameter(G1)
print("Diameter = ", dia)

#eccentricity

ecc = nx.eccentricity(G1)
print("Eccentricity =", ecc)

#radius a.k.a mininmum eccentricity

rad = nx.radius(G1)
print("Radius =", rad)

#Center of graph

cent = nx.center(G1)
print("Center =", cent)

#Degree Centrality

deg_cent = nx.degree_centrality(G1)
print("Degree Centrality =", deg_cent)

#closeness centrality

close_cent = nx.closeness_centrality(G1)
print("Closeness Centrality =", close_cent)


#betweenness centrality

bet_cent = nx.betweenness_centrality(G1)
print("Betweenness Centrality =", bet_cent)

#eigen vector centrality

eigen_cent = nx.eigenvector_centrality(G1)
print("Eigen Vector Cent =", eigen_cent)

#local clustering coefficent

loc_cc = nx.clustering(G1)
print("Local Clustering Cofficients= ", loc_cc)

#global clustering coefficent

gl_cc = nx.transitivity(G1)
print("Global Clustering Coefficient= ", gl_cc)

#average clustering coefficient

a_cc = nx.average_clustering(G1)
print("Average CLustering Coefficient= ", a_cc)

#degree assortativity coefficient

d_ac = nx.degree_assortativity_coefficient(G1)
print("Degree Assortativity Coefficient= ", d_ac)



# In[62]:


#Basic Graph 2

G2 = nx.Graph()
G2.add_edges_from([('A', 1),
                   ('A', 2),
                   ('A', 3),
                   ('A', 4),
                   ('A','B'),
                   ('B', 5),
                   ('B', 6),
                   ('B', 7),
                   (5, 8),
                   (6, 9),
                   (8, 9),
                   (9, 10),
                   (10, 11)])

nx.draw_networkx(G2)
# density
dens = nx.density(G2)
print("Density =", dens)

#path length

asp = nx.average_shortest_path_length(G2)
print("Average Distance Between Pair of Nodes = ", asp)

#diameter

dia = nx.diameter(G2)
print("Diameter = ", dia)

#eccentricity

ecc = nx.eccentricity(G2)
print("Eccentricity =", ecc)

#radius a.k.a mininmum eccentricity

rad = nx.radius(G2)
print("Radius =", rad)

#Center of graph

cent = nx.center(G2)
print("Center =", cent)

#Degree Centrality

deg_cent = nx.degree_centrality(G2)
print("Degree Centrality =", deg_cent)

#closeness centrality

close_cent = nx.closeness_centrality(G2)
print("Closeness Centrality =", close_cent)


#betweenness centrality

bet_cent = nx.betweenness_centrality(G2)
print("Betweenness Centrality =", bet_cent)

#eigen vector centrality

eigen_cent = nx.eigenvector_centrality(G2)
print("Eigen Vector Cent =", eigen_cent)

#local clustering coefficent

loc_cc = nx.clustering(G2)
print("Local Clustering Cofficients= ", loc_cc)

#global clustering coefficent

gl_cc = nx.transitivity(G2)
print("Global Clustering Coefficient= ", gl_cc)

#average clustering coefficient

a_cc = nx.average_clustering(G2)
print("Average CLustering Coefficient= ", a_cc)

#degree assortativity coefficient

d_ac = nx.degree_assortativity_coefficient(G2)
print("Degree Assortativity Coefficient= ", d_ac)


# In[63]:


#Basic Graph 3

G3 = nx.Graph()
G3.add_edges_from([('A', 1),
                   ('A', 2),
                   ('A', 3),
                   ('A', 4),
                   ('B', 5),
                   ('B', 6),
                   ('B', 7),
                   (5, 8),
                   (6, 9),
                   (8, 9),
                   (9, 10),
                   (10, 11),
                   ('C', 'B'),
                   ('C', 'A')])

nx.draw_networkx(G3)
# density
dens = nx.density(G3)
print("Density =", dens)

#path length

asp = nx.average_shortest_path_length(G3)
print("Average Distance Between Pair of Nodes = ", asp)

#diameter

dia = nx.diameter(G3)
print("Diameter = ", dia)

#eccentricity

ecc = nx.eccentricity(G3)
print("Eccentricity =", ecc)

#radius a.k.a mininmum eccentricity

rad = nx.radius(G3)
print("Radius =", rad)

#Center of graph

cent = nx.center(G3)
print("Center =", cent)

#Degree Centrality

deg_cent = nx.degree_centrality(G3)
print("Degree Centrality =", deg_cent)

#closeness centrality

close_cent = nx.closeness_centrality(G3)
print("Closeness Centrality =", close_cent)


#betweenness centrality

bet_cent = nx.betweenness_centrality(G3)
print("Betweenness Centrality =", bet_cent)

#eigen vector centrality

eigen_cent = nx.eigenvector_centrality(G3)
print("Eigen Vector Cent =", eigen_cent)

#local clustering coefficent

loc_cc = nx.clustering(G3)
print("Local Clustering Cofficients= ", loc_cc)

#global clustering coefficent

gl_cc = nx.transitivity(G3)
print("Global Clustering Coefficient= ", gl_cc)

#average clustering coefficient

a_cc = nx.average_clustering(G3)
print("Average CLustering Coefficient= ", a_cc)

#degree assortativity coefficient

d_ac = nx.degree_assortativity_coefficient(G3)
print("Degree Assortativity Coefficient= ", d_ac)


# In[64]:


#Basic Graph 4

G4 = nx.Graph()
G4.add_edges_from([(1, 2),
                   (3, 2),
                   (1, 3),
                   (1, 4),
                   (4, 3),
                   (4, 5),
                   (5, 6),
                   (6, 7),
                   (7, 8),
                   (7, 9),
                   (7, 10),
                   (6, 11),
                   (11, 12),
                   (11, 16),
                   (12, 13),
                   (12, 15),
                   (13, 14),
                   (14, 15),
                   (15, 16)])

nx.draw_networkx(G4)
# density
dens = nx.density(G4)
print("Density =", dens)

#path length

asp = nx.average_shortest_path_length(G4)
print("Average Distance Between Pair of Nodes = ", asp)

#diameter

dia = nx.diameter(G4)
print("Diameter = ", dia)

#eccentricity

ecc = nx.eccentricity(G4)
print("Eccentricity =", ecc)

#radius a.k.a mininmum eccentricity

rad = nx.radius(G4)
print("Radius =", rad)

#Center of graph

cent = nx.center(G4)
print("Center =", cent)

#Degree Centrality

deg_cent = nx.degree_centrality(G4)
print("Degree Centrality =", deg_cent)

#closeness centrality

close_cent = nx.closeness_centrality(G4)
print("Closeness Centrality =", close_cent)


#betweenness centrality

bet_cent = nx.betweenness_centrality(G4)
print("Betweenness Centrality =", bet_cent)

#eigen vector centrality
#since it didn't converge within 100 iterations hence using the alternate documentation and 
#setting max_iter 1000

eigen_cent = nx.eigenvector_centrality(G4, max_iter=1000, tol=1e-06, nstart=None, weight=None)
print("Eigen Vector Cent =", eigen_cent)

#local clustering coefficent

loc_cc = nx.clustering(G4)
print("Local Clustering Cofficients= ", loc_cc)

#global clustering coefficent

gl_cc = nx.transitivity(G4)
print("Global Clustering Coefficient= ", gl_cc)

#average clustering coefficient

a_cc = nx.average_clustering(G4)
print("Average CLustering Coefficient= ", a_cc)

#degree assortativity coefficient

d_ac = nx.degree_assortativity_coefficient(G4)
print("Degree Assortativity Coefficient= ", d_ac)

