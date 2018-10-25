

def clumpFinding(s,k,L,t):
    out = []
    for start in range(len(s)-L+1):
        window = s[start:start+L]
        counts = {}
        for i in range(len(window)-k+1):
            if window[i:i+k] not in counts:
                counts[window[i:i+k]] = 0
            counts[window[i:i+k]] += 1
        for kmer in counts:
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
    return out

with open('e.txt','r') as f:
    data = f.read()

genome = data.split('\n')[0]
k = 9
L = 500
t = 3

z = clumpFinding(genome,k,L,t)
print(len(z))
