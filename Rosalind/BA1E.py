# find all kmers in string that appears at least t times within a reading frame of L bp
def find_clumps(string, klen, L, t):
    clumps = set()

    for i in range(len(string) - L + 1):
        frame = string[i:i+L]
        counts = {}

        for j in range(L - klen + 1):
            kmer_in_frame = frame[j:j + klen]

            if kmer_in_frame not in counts:
                counts[kmer_in_frame] = 0

            counts[kmer_in_frame] += 1

        for kmers in counts:
            if counts[kmers] >= t:
                clumps.add(kmers)

    return clumps
