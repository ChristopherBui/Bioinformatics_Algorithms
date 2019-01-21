# find most frequent k-mer in text such that k-mer is allowed at most d mismatches

from HAMM import hamming_distance

def most_frequent_kmer(string, klen, d):

    kmer_counts = {}
    most_frequent = []

    start = 0
    end = klen

    while end <= len(string):
        kmer = string[start:end]

        if hamming_distance(kmer,

    return most_frequent
