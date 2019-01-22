# skew = the difference between number of G & C (G minus C). Always start at 0 skew
# return position in string when minimum skew occurs

def minimum_skew(string):
    skew = 0
    skew_loc = {}

    min_skew_loc = []

    for i in range(len(string)):
        if string[i] == 'G':
            skew = skew + 1
        elif string[i] == 'C':
            skew = skew - 1
        else:
            pass

        skew_loc[i] = skew

    min_skew = min(skew_loc.values())

    for j,k in skew_loc.items():
        if k == min_skew:
            min_skew_loc.append(j)

    return min_skew_loc, skew_loc

x,y = minimum_skew('CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG')
print(*x)

print(y[52],y[53],y[96])
