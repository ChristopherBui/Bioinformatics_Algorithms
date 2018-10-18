import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import pattern_to_number
import number_to_pattern

def count_frequency_array(sequence, klen):
    frequency_array = [0] * (4**klen)
    frequent_positions = []

    start = 0
    end = klen

    for i in range(len(sequence) - klen):
        frame = sequence[start:end]

        num = pattern_to_number(frame)
        frequency_array[num] = frequency_array[num] + 1

        start = start + 1
        end = end + 1

    max_count = max(frequency_array)

    for i in range(len(frequency_array)):
        if frequency_array[i] == max_count:
            frequent_positions.append(i)

    # convert numbers to pattern
    f = lambda x: number_to_pattern(x)
    frequent_patterns = list(map(f, frequent_nums))

    return frequency_array, frequent_positions, frequent_patterns
