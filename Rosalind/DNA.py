def count_nucleotides(string):
    counter = {'A':0, 'C':0, 'G':0, 'T':0}

    for base in string:
        if base == 'A':
            counter['A'] += 1
        elif base == 'C':
            counter['C'] += 1
        elif base == 'G':
            counter['G'] += 1
        elif base == 'T':
            counter['T'] += 1
        else:
            return 'Unknown Base Detected'

    counts = list(counter.values())

    # convert counts list elements from int to str type
    counts = [str(i) for i in counts]

    return ' '.join(counts)
