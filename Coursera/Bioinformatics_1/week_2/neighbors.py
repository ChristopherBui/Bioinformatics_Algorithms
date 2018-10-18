import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import hamming_distance

def neighbors(sequence, distance):

    if distance == 0:
        return [sequence]
    if len(sequence)==1:
        return ['A','T','C','G']

    neighbors_set = set()
    suffix = neighbors(sequence[1:], distance)

    for i in suffix:
        if hamming_distance(sequence[1:], i) < distance:
            for j in ['A','T','C','G']:
                neighbors_set.add(j + i)
        else:
            neighbors_set.add(sequence[0] + i)

    return neighbors_set
