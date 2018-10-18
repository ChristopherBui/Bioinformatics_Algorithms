import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def reverse_compliment(sequence):
    # reverse_compliment
    rc = ''

    for i in sequence:
        if i == 'A':
            rc = rc + 'T'
        elif i == 'T':
            rc = rc + 'A'
        elif i == 'G':
            rc = rc + 'C'
        elif i == 'C':
            rc = rc + 'G'
        else:
            print('Unknown Nucleotide in Template')
            break

    rc = rc[::-1]

    return rc
