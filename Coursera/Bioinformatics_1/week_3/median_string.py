import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def number_to_pattern(number, klen):

    digits_list = []
    sequence = ''

    for i in range(klen):
        remainder = number%4
        number = int(number/4)

        digits_list.append(remainder)

    # reverse to have ith index correspond to ith digit
    digits_list = digits_list[::-1]

    for i in digits_list:
        if i == 0:
            sequence = sequence + 'A'
        elif i == 1:
            sequence = sequence + 'C'
        elif i == 2:
            sequence = sequence + 'G'
        elif i == 3:
            sequence = sequence + 'T'
        else:
            print('unknown nucleotide')
            break

    return sequence


def hamming_distance_(str1, str2):
    distance = 0

    for i,j in zip(str1,str2):
        if i != j:
            distance = distance + 1

    return distance


# find the kmer (out of 4**klen possible kmers) that minimizes
# Sum(hamming_distance(kmer, string)) for every string in dna

def median_string(dna, klen):
    # dna is a list of strings

    kmer_scores = {k:v for k,v in zip(list(range(4**klen)),[0]*(4**klen))}
    median = set()

    for kmer in range(4**klen):
        each_strings_score = [0]*len(dna[0])

        for string in range(len(dna)):
            temp_string_score = klen

            for i in range(len(dna[string]) - klen + 1):
                frame = dna[string][i:i + klen]
                distance = hamming_distance_(number_to_pattern(kmer, klen), frame)

                if distance < temp_string_score:
                    temp_string_score = distance

            each_strings_score[string] = temp_string_score

        sum_strings_score = sum(each_strings_score)
        kmer_scores[kmer] = sum_strings_score

    minimum = min(kmer_scores.values())

    for k,v in kmer_scores.items():
        if v == minimum:
            median.add(number_to_pattern(k, klen))

    return median
