alcc = []
gcc = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.Graph()

for i in range(7):
    for j in range(i+1, 7):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

G = nx.Graph()

for i in range(70):
    for j in range(i+1, 70):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(100):
    for j in range(i+1, 100):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(700):
    for j in range(i+1, 700):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(1000):
    for j in range(i+1, 1000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(7000):
    for j in range(i+1, 7000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(10000):
    for j in range(i+1, 10000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(50000):
    for j in range(i+1, 50000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

print("alcc =", alcc)
print("gcc =", gcc)

from scipy.stats.stats import pearsonr
print (pearsonr(alcc, gcc))


# Different values of probability

alcc = []
gcc = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.Graph()

for i in range(7):
    for j in range(i+1, 7):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

G = nx.Graph()

for i in range(70):
    for j in range(i+1, 70):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(100):
    for j in range(i+1, 100):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(700):
    for j in range(i+1, 700):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(1000):
    for j in range(i+1, 1000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(7000):
    for j in range(i+1, 7000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(10000):
    for j in range(i+1, 10000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(50000):
    for j in range(i+1, 50000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

print("alcc =", alcc)
print("gcc =", gcc)

from scipy.stats.stats import pearsonr
print (pearsonr(alcc, gcc))



# for different probabilities

alcc = []
gcc = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.Graph()

for i in range(7):
    for j in range(i+1, 7):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

G = nx.Graph()

for i in range(70):
    for j in range(i+1, 70):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(100):
    for j in range(i+1, 100):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(700):
    for j in range(i+1, 700):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(1000):
    for j in range(i+1, 1000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(7000):
    for j in range(i+1, 7000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(10000):
    for j in range(i+1, 10000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(50000):
    for j in range(i+1, 50000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

print("alcc =", alcc)
print("gcc =", gcc)

from scipy.stats.stats import pearsonr
print (pearsonr(alcc, gcc))


# differnt probabilities

alcc = []
gcc = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.Graph()

for i in range(7):
    for j in range(i+1, 7):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

G = nx.Graph()

for i in range(70):
    for j in range(i+1, 70):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(100):
    for j in range(i+1, 100):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(700):
    for j in range(i+1, 700):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(1000):
    for j in range(i+1, 1000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(7000):
    for j in range(i+1, 7000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)



G = nx.Graph()

for i in range(10000):
    for j in range(i+1, 10000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)


G = nx.Graph()

for i in range(50000):
    for j in range(i+1, 50000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            G.add_edge(i, j)

Gc = max(nx.connected_component_subgraphs(G), key=len)
dia = nx.average_clustering(Gc)
dens = nx.transitivity(G)

alcc.append(dia)
gcc.append(dens)

print("alcc =", alcc)
print("gcc =", gcc)

from scipy.stats.stats import pearsonr
print (pearsonr(alcc, gcc))












