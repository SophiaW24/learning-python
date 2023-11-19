#Computing GC content

dna_string = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

#calculate GC-content
total =len(dna_string)
G = dna_string.count('G')
C = dna_string.count('C')

GC_total = G + C

GC_content = GC_total/total


#formating deciaml to percent with 6 decimal places
GC_content = float(GC_content) * 100
print('{:.6f}'.format(GC_content) + '%')


GC_content.append((strand.count('G') + strand.count('C'))/len(strand))






#cheated by formating fasta file dna code in one line...
#didn´t know how else to solve it
#I know won´t work with big data

fasta_format = '''
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT
'''
GC_content = []

for strand in fasta_format.splitlines():
    if strand == '>':
        next(strand)
    else:
        GC_content.append((strand.count('G') + strand.count('C'))/len(strand))

print(GC_content)


#I tried to solve this but couldn´t figure it out..
#This is my best attempt
