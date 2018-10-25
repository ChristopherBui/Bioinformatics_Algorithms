import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def hamming_distance_(str1, str2):
    distance = 0

    for i,j in zip(str1,str2):
        if i != j:
            distance = distance + 1

    return distance
