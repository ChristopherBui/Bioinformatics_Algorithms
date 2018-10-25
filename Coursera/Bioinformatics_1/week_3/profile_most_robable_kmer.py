import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from functools import reduce



def profile_most_probable_kmer(motif_string, profile, klen):

    multiply = lambda x,y: x*y
    kmer_proba = {}
    final_kmers = set()

    for i in range(len(motif_string) - klen + 1):
        proba = []
        frame = motif_string[i:i+klen]

        for n in range(len(frame)):
            if frame[n] == 'A':
                proba.append(profile[n][0])
            elif frame[n] == 'C':
                proba.append(profile[n][1])
            elif frame[n] == 'G':
                proba.append(profile[n][2])
            elif frame[n] == 'T':
                proba.append(profile[n][3])

        frame_proba = reduce(multiply, proba)
        kmer_proba[frame] = frame_proba

    max_proba = max(kmer_proba.values())

    for k,v in kmer_proba.items():
        if v == max_proba:
            final_kmers.add(k)

    return final_kmers
