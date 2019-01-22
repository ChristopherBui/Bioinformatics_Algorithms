from BA1L import pattern_to_number

def frequency_array(string, klen):
    # generate array of length 4**klen to represent all possible kmers
    # each kmer when turned to a number is represented by the index in kmer array of the same number
    kmer_array = [0] * (4**klen)

    start = 0
    end = klen

    for i in range(len(string) - klen + 1):
        kmer = string[start:end]

        # convert kmer in string to number & add to frequency array
        num = pattern_to_number(kmer)
        kmer_array[num] += 1

        start += 1
        end += 1

    return kmer_array
