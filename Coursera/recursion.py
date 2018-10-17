# niemasd
# nathaniellovin

def factorial_iterative(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i

    return ans


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * (factorial(n-1))


# fibonacci:
# 1,1,2,3,5,8,13,21

def fibonacci(n):
    # get the kth term in fibonacci sequence

    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib_cache = {}
def fibonacci_memoi(n):
    if n in fib_cache:
        return fib_cache[n]
    elif n==1 or n==2:
        return 1
    else:
        value = fibonacci_memoi(n-1) + fibonacci_memoi(n-2)
    fib_cache[n] = value
    return value


def ApproximatePatternMatching(sequence, kmer, distance):
    pos = [] # initializing list of positions
    # your code here
    start = 0
    end = len(kmer)

    for i in range(len(sequence) - len(kmer) + 1):
        frame = sequence[start:end]
        if hamming(frame, kmer) <= distance:
            pos.append(i)
        else:
            pass

        start += 1
        end += 1

    return pos


def hamming_distance(str1, str2):
    hamming_distance = 0

    if (len(str1) != len(str2)) or (isinstance(str1,str)==False) or (isinstance(str2,str)==False):
        print('input error')
        return False
    else:
        for i in list(zip(str1, str2)):
            if i[0] != i[1]:
                hamming_distance = hamming_distance + 1
            else:
                pass

    return hamming_distance


def hamming(str1, str2):
    distance = 0

    for i,j in zip(str1,str2):
        if i != j:
            distance = distance + 1

    return distance

def Number_To_Pattern(number, klen):
    A = 0
    C = 1
    G = 2
    T = 3

    digits_list = []
    sequence = ''

    for i in range(klen):
        remainder = number%4
        number = int(number/4)

        digits_list.append(remainder)

    # reverse to have digits in right order
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

def Pattern_To_Number(pattern):
    klen = len(pattern)

    num = 0
    pattern = pattern[::-1]

    for i in range(klen):
        if pattern[i] == 'A':
            num = num + 0*(4**i)
        elif pattern[i] == 'C':
            num = num + 1*(4**i)
        elif pattern[i] == 'G':
            num = num + 2*(4**i)
        elif pattern[i] == 'T':
            num = num + 3*(4**i)
        else:
            print('unknown nucleotide')
            break

    return num


def most_frequent_mismatch(sequence, klen, distance):
    # returns most frequent neighbors with at most d mismatches
    # out of all possible kmers in sequence

    kmer_array = [0]*(4**klen)
    mf_mismatch = []

    start = 0
    end = klen

    for i in range(len(sequence) - klen + 1):
        pattern = sequence[start:end]

        neighborhood = neighbors(pattern, distance)
        for n in neighborhood:
            n_number = Pattern_To_Number(n)
            kmer_array[n_number] += 1

        start += 1
        end += 1

    maximum = max(kmer_array)
    for i in range(len(kmer_array)):
        if kmer_array[i] != maximum:
            pass
        else:
            k_mismatch = Number_To_Pattern(kmer_array[i], klen)
            mf_mismatch.append(k_mismatch)


    return mf_mismatch


def neighbor_d1(sequence):
    neighbors_set = set()

    for new_nuc in {'A','T','C','G'}:
        neighbor = sequence.replace(sequence[0], new_nuc)
        neighbors_set.add(neighbor)

    for i in range(1,len(sequence)):
        temp_set = {'A','T','C','G'}
        temp_set.remove(sequence[i])
        for new_nuc in temp_set:
            neighbor = sequence.replace(sequence[i], new_nuc)
            neighbors_set.add(neighbor)


    return neighbors_set


def neighbors(sequence, distance):

    if distance == 0:
        return [sequence]
    if len(sequence)==1:
        return ['A','T','C','G']

    neighbors_set = set()
    suffix = neighbors(sequence[1:],distance)

    for i in suffix:
        if hamming(sequence[1:], i) < distance:
            for j in ['A','T','C','G']:
                neighbors_set.add(j + i)
        else:
            neighbors_set.add(sequence[0] + i)
    return neighbors_set


print(hamming('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT','CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG'))
