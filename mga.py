# METAMERIC GENETIC ALGORITHM (MGA)
#
# MODULE:     mga.py
# AUTHOR:     Jinseok Yeom
# VERSION:    0.1
# SINCE:      10/03/2016
#

import numpy as np
import numpy.random as npr

# MGA parameters
NUM_GENERATION      = 100   # number of generations
POPULATION_SIZE     = 100   # size of genome population
METAVAR_SIZE        = 5     # number of design variables in a metavariable
GENOME_LEN_MIN      = 3     # minimum number of metavariables in a genome
GENOME_LEN_MAX      = 5     # maximum number of metavariables in a genome
RECOMBINATION_RATE  = 0.1   # recombination rate
MUTATION_RATE       = 0.1   # mutation rate

# Metavariable
class Metavar(object):
    def __init__(self, mv_id):
        self.mv_id = mv_id                  # metavariable ID
        self.dv = npr.rand(METAVAR_SIZE)    # design variables

    # calculate dissimilarity with other metavariable.
    def dissimilarity(self, m1):
        return

# Variable-length Genome
class Genome(object):
    def __init__(self, g_id):
        length = npr.randint(GENOME_LEN_MIN, GENOME_LEN_MAX)

        self.g_id = g_id                                    # genome ID
        self.length = length                                # genome length
        self.genotype = [Metavar(i) for i in range(length)] # genotype

    # design variable mutation 
    def dv_mutate(self):
        
        # to be implemented

        return

    # metavariable insertion
    def metavar_insert(self):
        
        # to be implemented
    
        return

    # metavariable deletion
    def metavar_delete(self):
        
        # to be implemented
        
        return 

    # similar-metavariable recombination
    def sm_recombine(self, g1):
        
        # to be implemented 
    
        return

# Metameric Genetic Algorithm
class MGA(object):
    def __init__(self):
        self.best_genome = []
        self.population = [Genome(i) for i in range(POPULATION_SIZE)]

    # NSGA-II based selection
    def select(self):
        
        # to be implemented

        return

if __name__ == '__main__':
    mga = MGA()
