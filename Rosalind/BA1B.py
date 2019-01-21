def most_frequent_kmer(string, klen):
    counts = {}
    most_freq = []

    start = 0
    end = klen

    while end <= len(string):
        kmer = string[start:end]

        if kmer not in counts:
            counts[kmer] = 1
        else:
            counts[kmer] += 1

        start += 1
        end += 1

    max_count = max(counts.values())

    for k, count in counts.items():
        if count == max_count:
            most_freq.append(k)
        else:
            pass

    return most_freq
