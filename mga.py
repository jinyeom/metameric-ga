# METAMERIC GENETIC ALGORITHM (MGA)
#
# AUTHOR:     JINSEOK YEOM
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
        return (abs()) / float(size)

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

