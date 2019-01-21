def pattern_to_number(pattern):

    # reverse pattern so that the ith element corresponds to the ith digits place
    pattern = pattern[::-1]

    num = 0

    for i in range(len(pattern)):
        if pattern[i] == 'A':
            num = num + 0*(4**i)
        elif pattern[i] == 'C':
            num = num + 1*(4**i)
        elif pattern[i] == 'G':
            num = num + 2*(4**i)
        elif pattern[i] == 'T':
            num = num + 3*(4**i)
        else:
            print('unknown nucleotide')
            return None

    return num
