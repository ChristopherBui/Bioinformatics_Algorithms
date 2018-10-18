import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def pattern_to_number(pattern):

    klen = len(pattern)
    num = 0

    # reverse pattern so that i corresponds to the ith digits place
    pattern = pattern[::-1]

    for i in range(klen):
        if pattern[i] == 'A':
            num = num + 0*(4**i)
        elif pattern[i] == 'C':
            num = num + 1*(4**i)
        elif pattern[i] == 'G':
            num = num + 2*(4**i)
        elif pattern[i] == 'T':
            num = num + 3*(4**i)
        else:
            print('unknown nucleotide')
            break

    return num
