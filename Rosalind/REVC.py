def reverse_complement(string):
    ''' We read dna in 3' to 5' direction. Thus, the reverse complement of dna,
    keeping the same direction of reading, is read in 5' to 3' direction with its bases
    being those complementary to those in dna. '''

    # this function will return the reverse complement
    rc = ''

    for i in string:
        if i == 'A':
            rc = 'T' + rc
        elif i == 'C':
            rc = 'G' + rc
        elif i == 'G':
            rc = 'C' + rc
        elif i == 'T':
            rc = 'A' + rc

    return rc

print(reverse_complement('AAAACCCGGT'))
