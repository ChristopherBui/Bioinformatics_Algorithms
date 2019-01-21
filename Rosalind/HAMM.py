def hamming_distance(str1, str2):

    if len(str1) != len(str2):
        return None
    else:
        distance = 0
        for i,j in zip(str1, str2):
            if i != j:
                distance = distance + 1

    return distance
