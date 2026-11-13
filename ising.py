# this script contains the basic parts of the Ising model 

# Good practices at coding : 
#   - Naming the variables with easily-identifying names. 
#   - Be organised and try to write the code by pieces. (define functions that compute things that appear often :) ).
#   - Adding comments/doc_strings makes correction way easier and shows knowledge.
#   - If your code takes too much time please notify it on the script. Try to modularize it and make use of vectorized functions.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # why 42? Ask the students if they know about The Hitchhiker's Guide to the Galaxy

def initial_random_state(n):
    '''Generates a random lattice of spins of size (lenght) n'''
    lattice = 2 * np.random.randint(0, 2, size = (n, n)) - 1 
    # faster than np.random.choice([-1, 1], size = (n,n))
    return lattice

# Second part: functions that will be useful for our code 

def first_neighbours(lattice, i, j):
    '''Returns the index position of the first neighbours in a spin lattice
    with periodical conditions. We could implement the open lattice condition
    easily but not for this year'''
    n = lattice.shape[0]  # square lattice n x n
    return [
        ((i - 1) % n, j),  # lower
        ((i + 1) % n, j),  # upper
        (i, (j - 1) % n),  # left
        (i, (j + 1) % n),  # right
    ]

def energy(lattice):
    '''Computes the energy of a given lattice in our reduced units'''
    n = lattice.shape[0]  # square lattice n x n
    E = 0
    for i in range(n):
        for j in range(n): 
            E += lattice[i, j] *  sum(lattice[indexes] for indexes in first_neighbours(lattice, i, j))
    return -E/2 # the 1/2 comes from the fact that we are counting the configurations twice in the loops 

def magnetization(lattice):
    '''Computes the magnetization of a lattice''' 
    return np.sum(lattice)/lattice.size # np.mean(lattice) also works out 

def metropolis_algorithm(lattice, T_red, n_iter):
    '''Performs the Metropolis algorithm at reduced temperature T_red, n_iter times'''
    n = lattice.shape[0]
    for iter in range(n_iter):
        i = np.random.randint(n) # row index
        j = np.random.randint(n) # column index

        # Computing dE
        dE = 2 * lattice[i, j] * sum(lattice[indexes] for indexes in first_neighbours(lattice, i, j)) # where does this eqn come from? 

        # Accept the change 
        if dE <= 0:
            lattice[i, j] *= -1
        else:
            p = np.exp(-dE / T_red) # probability of transition between states
            R = np.random.uniform()
            if R < p:
                lattice[i, j] *= -1 
    return lattice