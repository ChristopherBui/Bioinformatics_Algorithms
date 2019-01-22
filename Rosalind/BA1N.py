from BA1G import hamming_distance

# return all neighbors of string with at most d mismatches
def neighbors(string, d):
    if d == 0:
        return string
    if len(string) == 1:
        return ['A','T','C','G']

    neighbors_set = set()

    suffix = neighbors(string[1:],d)

    for i in suffix:
        if hamming_distance(string[1:], i) < d:
            for j in ['A','T','C','G']:
                neighbors_set.add(j + i)
        else:
            neighbors_set.add(string[0] + i)

    return neighbors_set
