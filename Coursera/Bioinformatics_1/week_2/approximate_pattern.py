import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def approximate_pattern(sequence, kmer, distance):
    start = 0
    end = len(kmer)

    # beginning positions of approximate patterns
    approx_positions = []

    for i in range(len(sequence)):
        frame = sequence[start:end]

        if hamming_distance(frame,kmer) <= distance:
            approx_positions.append(i)
        else:
            pass

    n_occurences = len(approx_positions)
    print('There are {} approximate patterns'.format(n_occurences))

    return approx_positions
