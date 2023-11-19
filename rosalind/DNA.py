#Counting DNA Nucleotides

dna_code = list('AAATGC')
countA = 0
countC = 0
countG = 0
countT = 0
​
for letter in dna_code:
    if letter == 'A':
        countA += 1
    elif letter == 'C':
        countC += 1
    elif letter == 'G':
        countG += 1
    elif letter == 'T':
        countT += 1
​
print(countA, countC, countG, countT)
3 1 1 1
