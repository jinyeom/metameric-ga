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
    def __init__(self, size):
        self.size = size            # number of design variables
        self.dv = npr.rand(size)    # randomly initialized design variables

    # calculate dissimilarity with other metavariable.
    def dissimilarity(self, m1):
        assert (self.size == m1.size), "invalid argument metavariable"
        return

# Variable-length Genome
class Genome(object):
    def __init__(self, mv_size, length):
        self.length = length
        self.genome = [Metavariable(mv_size) for x in range(length)]       
 
    def mutate(self):
        return
    
    def sm_recombination(self):
        return

# Metameric Genetic Algorithm
class MGA(object):
    def __init__(self):
        assert (type(p[0]) is int and p[0] > 0), \
            "invalid number of generations"
        assert (type(p[1]) is int and p[1] > 0), \
            "invalid size of population"
        assert (type(p[2]) is int and p[2] > 0), \
            "invalid size of metavariable"
        assert (type(p[3]) is int and p[3] > 0), \
            "invalid minimum length of genome"
        assert (type(p[4]) is int and param[4] > param[3]), \
            "invalid minimum and maximum lengths of genome"
        assert (type(p[5]) is float and 0.0 <= p[5] and p[5] < 1.0), \
            "invalid crossover rate"
        assert (type(p[6]) is float and 0.0 <= p[6] and p[6] < 1.0), \
            "invalid mutation rate"


        self.population = [Genome(METAVAR_SIZE, npr.randint(GENOME_LEN_MIN, GENOME_LEN_MAX)) for x in range(POPULATION_SIZE)]


if __name__ == '__main__':

    mga = MGA()
