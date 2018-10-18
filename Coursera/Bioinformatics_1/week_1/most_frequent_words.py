import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def most_frequent_words(sequence, kmer_len):
    start = 0
    end = kmer_len

    count_dict = {}
    most_freq = []

    for i in range(len(sequence) - kmer_len):

        frame = sequence[start:end]

        if frame not in count_dict:
            count_dict[frame] = 1

        else:
            count_dict[frame] = count_dict[frame] + 1

        start = start + 1
        end = end + 1

    max_value = max(d.values())

    for kmer, count in d.items():
        if count == max_value:
            most_freq.append(kmer)

    return most_freq
