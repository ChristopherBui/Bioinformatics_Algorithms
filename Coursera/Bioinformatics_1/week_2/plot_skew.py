import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_skew(sequence):
    position_x_axis = np.arange(0,len(sequence)+1,1)
    skew_count_y_axis = [0]

    skew_count = 0

    for i in sequence:
        if i=='G':
            skew_count = skew_count + 1
            skew_count_y_axis.append(skew_count)
        elif i=='C':
            skew_count = skew_count - 1
            skew_count_y_axis.append(skew_count)
        else:
            skew_count_y_axis.append(skew_count)

    plot = plt.plot(position_x_axis, skew_count_y_axis, marker='o', color='blue')

    minimum = min(skew_count_axis)
    maximum = max(skew_count_axis)

    # create string conversion function
    string_convert = lambda x: str(x)

    # mimimum skew value positions
    # origin tends to be at minimum skew
    # terminus tends to be at maximum skew

    origin = list(map(string_convert,[index for index, skew_value in enumerate(skew_count_x_axis) if skew_value == minimum])))
    terminus = list(map(string_convert,[index for index, skew_value in enumerate(skew_count_x_axis) if skew_value == maximum])))

    return plot, origin, terminus
