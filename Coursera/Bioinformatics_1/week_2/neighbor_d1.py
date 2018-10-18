import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def neighbor_d1(sequence):
    bases = {'A','T','C','G'}
    neighbors_set = set()

    # change the first nucleotide
    for new_nuc in bases:
        neighbor = sequence.replace(sequence[0], new_nuc)
        neighbors_set.add(neighbor)

    for i in range(1,len(sequence)):
        temp_set = {'A','T','C','G'}
        temp_set.remove(sequence[i])

        for new_nuc in temp_set:
            neighbor = sequence.replace(sequence[i], new_nuc)
            neighbors_set.add(neighbor)

    return neighbors_set
