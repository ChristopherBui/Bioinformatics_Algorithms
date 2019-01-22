# find most frequent k-mer in text such that k-mer is allowed at most d mismatches

from HAMM import hamming_distance
from BA1M import number_to_pattern

def most_freq(string, klen, d):

    # how to express all possible kmers
