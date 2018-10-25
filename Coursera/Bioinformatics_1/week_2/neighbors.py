import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from hamming_distance import hamming_distance_

def neighbors_(sequence, distance):

    if distance == 0:
        return [sequence]
    if len(sequence)==1:
        return ['A','T','C','G']

    neighbors_set = set()
    suffix = neighbors_(sequence[1:], distance)

    for i in suffix:
        if hamming_distance_(sequence[1:], i) < distance:
            for j in ['A','T','C','G']:
                neighbors_set.add(j + i)
        else:
            neighbors_set.add(sequence[0] + i)

    return neighbors_set
