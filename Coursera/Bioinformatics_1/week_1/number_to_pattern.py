import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def number_to_pattern(number, klen):

    digits_list = []
    sequence = ''

    for i in range(klen):
        remainder = number%4
        number = int(number/4)

        digits_list.append(remainder)

    # reverse to have ith index correspond to ith digit
    digits_list = digits_list[::-1]

    for i in digits_list:
        if i == 0:
            sequence = sequence + 'A'
        elif i == 1:
            sequence = sequence + 'C'
        elif i == 2:
            sequence = sequence + 'G'
        elif i == 3:
            sequence = sequence + 'T'
        else:
            print('unknown nucleotide')
            break

    return sequence
