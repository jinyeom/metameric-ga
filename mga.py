# METAMERIC GENETIC ALGORITHM (MGA)
#
#   AUTHOR:     JINSEOK YEOM
#   VERSION:    0.1
#   SINCE:      10/03/2016
#

import numpy as np
import numpy.random as npr

class Metavariable:
   
    # initialize random design variables with given size.  
    def __init__(self, size):
        self.size = size
        self.dv = npr.rand(size)

    # calculate dissimilarity with other metavariable.
    def dissimilarity(self, m1):
        assert (self.size == m1.size), "Unmatching sizes of metavariables"

class Genome:

    # initialize 
    def __init__(self, length):
        self.length = length
        
    def mutate(self):
        return
    
    def sm_recombination(self):
        return

class MGA:

