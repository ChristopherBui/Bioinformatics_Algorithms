def hamming_distance(str1, str2):

    if len(str1) != len(str2):
        return None
    else:
        distance = 0
        for i,j in zip(str1, str2):
            if i != j:
                distance = distance + 1

    return distance

# find locations where pattern appears in text with at most d mismatches
def approximate_occurences(text, pattern, d):

    locations = []

    start = 0
    end = len(pattern)

    while end <= len(text):
        if hamming_distance(text[start:end], pattern) <= d:
            locations.append(start)
        else:
            pass

        start += 1
        end += 1

    return locations
