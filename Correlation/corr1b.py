diameters = []
densities = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.DiGraph()

for i in range(7):
    for j in range(0, 7):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)







G = nx.DiGraph()

for i in range(70):
    for j in range(0, 70):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)





G = nx.DiGraph()

for i in range(100):
    for j in range(0, 100):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(700):
    for j in range(0, 700):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)




G = nx.DiGraph()

for i in range(1000):
    for j in range(0, 1000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(7000):
    for j in range(0, 7000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)


G = nx.DiGraph()

for i in range(10000):
    for j in range(0, 10000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(50000):
    for j in range(0, 50000):
        weights = [0.1, 0.9]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



from scipy.stats.stats import pearsonr
print (pearsonr(diameters, densities))

# for second set of probabilities

diameters = []
densities = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.DiGraph()

for i in range(7):
    for j in range(0, 7):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)







G = nx.DiGraph()

for i in range(70):
    for j in range(0, 70):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)





G = nx.DiGraph()

for i in range(100):
    for j in range(0, 100):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(700):
    for j in range(0, 700):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)




G = nx.DiGraph()

for i in range(1000):
    for j in range(0, 1000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(7000):
    for j in range(0, 7000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)


G = nx.DiGraph()

for i in range(10000):
    for j in range(0, 10000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(50000):
    for j in range(0, 50000):
        weights = [0.25, 0.75]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



from scipy.stats.stats import pearsonr
print (pearsonr(diameters, densities))



# for third set of probabilities

diameters = []
densities = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.DiGraph()

for i in range(7):
    for j in range(0, 7):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)







G = nx.DiGraph()

for i in range(70):
    for j in range(0, 70):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)





G = nx.DiGraph()

for i in range(100):
    for j in range(0, 100):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(700):
    for j in range(0, 700):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)




G = nx.DiGraph()

for i in range(1000):
    for j in range(0, 1000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(7000):
    for j in range(0, 7000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)


G = nx.DiGraph()

for i in range(10000):
    for j in range(0, 10000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(50000):
    for j in range(0, 50000):
        weights = [0.35, 0.65]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



from scipy.stats.stats import pearsonr
print (pearsonr(diameters, densities))



# for fourth set of probabilities

diameters = []
densities = []

import matplotlib.pyplot as plt
import networkx as nx
import random
from random import *

G = nx.DiGraph()

for i in range(7):
    for j in range(0, 7):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)







G = nx.DiGraph()

for i in range(70):
    for j in range(0, 70):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)





G = nx.DiGraph()

for i in range(100):
    for j in range(0, 100):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(700):
    for j in range(0, 700):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)




G = nx.DiGraph()

for i in range(1000):
    for j in range(0, 1000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(7000):
    for j in range(0, 7000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)


G = nx.DiGraph()

for i in range(10000):
    for j in range(0, 10000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



G = nx.DiGraph()

for i in range(50000):
    for j in range(0, 50000):
        weights = [0.4, 0.6]
        population = [1, 0]
        prob = choices(population, weights)
        #print(prob)
        if prob==[1]:
            if i!=j:
                G.add_edge(i, j)

Gc = max(nx.strongly_connected_component_subgraphs(G), key=len)
dia = nx.diameter(Gc)
dens = nx.density(G)

diameters.append(dia)
densities.append(dens)



from scipy.stats.stats import pearsonr
print (pearsonr(diameters, densities))












