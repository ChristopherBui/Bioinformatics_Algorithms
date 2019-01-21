def number_to_pattern(number, klen):

    digits_list = []
    pattern = ''

    for i in range(klen):
        remainder = number%4
        number = int(number/4)

        digits_list.append(remainder)

    # reverse digits_list to have ith element correspond to ith digits place
    digits_list = digits_list[::-1]

    for j in digits_list:
        if j == 0:
            pattern = pattern + 'A'
        elif j == 1:
            pattern = pattern + 'C'
        elif j == 2:
            pattern = pattern + 'G'
        elif j == 3:
            pattern = pattern + 'T'
        else:
            print('error')
            return None

    return pattern
