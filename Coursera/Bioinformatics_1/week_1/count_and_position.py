import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def count_and_position(sequence, pattern):
    start = 0
    end = len(pattern)

    count = 0
    position = []

    for i in range(len(sequence) - len(pattern)):
        frame = sequence[start:end]

        if frame == kmer:
            count = count + 1
            position.append(i)

        else:
            pass

    print('There are {} matches'.fomrat(count))
    return count, position
