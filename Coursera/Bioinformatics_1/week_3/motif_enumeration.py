import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def hamming_distance_(str1, str2):
    distance = 0

    for i,j in zip(str1,str2):
        if i != j:
            distance = distance + 1

    return distance


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


def motif_enumeration_(dna, klen, distance):

    patterns = set()

    for string in dna:
        for i in range(len(string)-klen+1):
            frame = string[i:i+klen]
            frame_neighbors = neighbors_(frame, distance)

            for neighbor in frame_neighbors:

                in_all_strings = True

                for string_ in dna:

                    in_string_ = False

                    for j in range(len(string_)-klen+1):
                        frame_ = string_[j:j+klen]

                        if hamming_distance_(neighbor, frame_) <= distance:
                            in_string_ = True

                    if in_string_ == False:
                        in_all_strings = False

                if in_all_strings == True:
                    patterns.add(neighbor)

    return patterns


if __name__ == '__main__':
    for i in motif_enumeration_(dna,klen,distance):
        print(i)
