def dna_to_rna(string):
    # note that this function does not return the rna complement for a dna sting
    # this just transforms all 'T' in the dna to 'U'

    rna = ''

    for i in range(len(string)):
        if string[i] == 'T':
            rna = rna + 'U'
        else:
            rna = rna + string[i]

    return rna
