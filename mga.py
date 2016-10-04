# METAMERIC GENETIC ALGORITHM (MGA)
# 
# MODULE:     mga.py
# AUTHOR:     Jinseok Yeom
# VERSION:    0.1
# SINCE:      10/03/2016
#

import numpy as np
import numpy.random as npr

# Metavariable
class Metavar(object):
    def __init__(self, size):
        self.size = size
        self.dv = npr.rand(size)

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
    def __init__(self, **kwargs):
        # process parameters
        keywords = [
            "num_generation",       # number of generations
            "population_size",      # size of genome population
            "metavar_size",         # number of design variables in metavariable
            "genome_len_min",       # minimum number of metavariables in a genome
            "genome_len_max",       # maximum number if metavariables in a genome
            "recombination_rate",   # recombination rate
            "mutation_rate",        # mutation rate
        ]
        param = [kwargs.get(kw) for kw in keywords]

        assert (type(param[0]) is int and param[0] > 0), "invalid number of generations"
        assert (type(param[1]) is int and param[1] > 0), "invalid size of population"
        assert (type(param[2]) is int and param[2] > 0), "invalid size of metavariable"
        assert (type(param[3]) is int and param[3] > 0), "invalid minimum length of genome"
        assert (type(param[4]) is int and param[4] > param[3]), "invalid minimum and maximum lengths of genome"
        assert (type(param[5]) is float and 0.0 <= xover_rate and xover_rate < 1.0), "invalid crossover rate"
        assert (type(param[6]) is float and 0.0 <= mut_rate and mut_rate < 1.0), "invalid mutation rate"

        self.parameters = param
        self.population = [Genome(mv_size, npr.randint(l_min, l_max)) for x in range(p_size)]

if __name__ == '__main__':
    # MGA constants
    NUM_GENERATION      = 100
    POPULATION_SIZE     = 100
    METAVAR_SIZE        = 5
    GENOME_LEN_MIN      = 3
    GENOME_LEN_MAX      = 5
    RECOMB_RATE         = 0.1
    MUTATION_RATE       = 0.1


