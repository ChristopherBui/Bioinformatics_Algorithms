import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pattern_count(sequence, kmer):
    start = 0
    end = len(kmer)

    count = 0

    try:
        for i in range(len(sequence) - len(kmer)):
            frame = sequence[start:end]

            if frame == kmer:
                count = count + 1

            else:
                pass

            start += 1
            end += 1

    except:
        pass

    return count
