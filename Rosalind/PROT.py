# create codon-amino acid dictionary
codon_aa_table = {'UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S',
'UCC':'S','UCA':'S','UCG':'S','UAU':'Y','UAC':'Y','UAA':'STOP','UAG':'STOP',
'UGU':'C','UGC':'C','UGA':'STOP','UGG':'W','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
'CCU':'P','CCC':'P','CCA':'P','CCG':'P','CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
'CGU':'R','CGC':'R','CGA':'R','CGG':'R','AUU':'I','AUC':'I','AUA':'I','AUG':'M',
'ACU':'T','ACC':'T','ACA':'T','ACG':'T','AAU':'N','AAC':'N','AAA':'K','AAG':'K',
'AGU':'S','AGC':'S','AGA':'R','AGG':'R','GUU':'V','GUC':'V','GUA':'V','GUG':'V',
'GCU':'A','GCC':'A','GCA':'A','GCG':'A','GAU':'D','GAC':'D','GAA':'E','GAG':'E',
'GGU':'G','GGC':'G','GGA':'G','GGG':'G'}

def translation(rna):
    start = 0
    end = 3

    # amino acid string
    aa_string = ''

    while end <= len(rna):
        codon = rna[start:end]

        amino_acid = codon_aa_table[codon]

        if amino_acid == 'STOP':
            break
        else:
            aa_string = aa_string + amino_acid

        start += 3
        end += 3

    return aa_string
