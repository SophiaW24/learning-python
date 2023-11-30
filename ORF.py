#6 possible ways to read adna string
#more possible protein strings possible -> from every start codon until stop codon

#all possible ORFs
#all possible ORFs on both strands
#all possible ORFs on both strands on all RFs
#all possible ATG....Stop on both strands on all RFs
#strands = foward & reverse complement strand

#for triplet in sequence: until Stop:
#if triplet is ATG:
#start trnaslating

dna_code = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

#transcribe DNA into RNA
for letter in dna_code:
    if letter == 'T':
        rna_code = dna_code.replace('T', 'U')
    else:
        continue

#print(rna_code)

#complement DNA and then transcribe into RNA
new_code = ''

for letter in dna_code:
    if letter == 'T':
        new_code += 'A'
    elif letter == 'G':
        new_code += 'C'
    elif letter == 'C':
        new_code += 'G'
    elif letter == 'A':
        new_code += 'T'

#print(new_code)

complement_code = new_code[::-1]
#print(complement_code)

for letter in complement_code:
    if letter == 'T':
        rna_code_reverse = complement_code.replace('T', 'U')
    else:
        continue

#print(rna_code_reverse)

#Run trough string in blocks of 3, starting from the beginning
#put them into a list

RF1 = []
for i in range(0, len(rna_code), 3):
    codon = rna_code[i:i+3]
    RF1.append(codon)

#print(RF1)

#Run trough string in blocks of 3, starting from second letter
#put them into a list

RF2 = []
for i in range(1, len(rna_code), 3):
    codon = rna_code[i:i+3]
    RF2.append(codon)

#print(RF2)

#Run trough string in blocks of 3, starting from third letter
#put them into a list

RF3 =[]
for i in range(2, len(rna_code), 3):
    codon = rna_code[i:i+3]
    RF3.append(codon)

#print(RF3)

#same thing for the reverse string

RF4 = []
for i in range(0, len(rna_code_reverse), 3):
    codon = rna_code_reverse[i:i+3]
    RF4.append(codon)

RF5 = []
for i in range(1, len(rna_code_reverse), 3):
    codon = rna_code_reverse[i:i+3]
    RF5.append(codon)

RF6 = []
for i in range(2, len(rna_code_reverse), 3):
    codon = rna_code_reverse[i:i+3]
    RF6.append(codon)

#print(RF4)
#print(RF5)
#print(RF6)

#read trough all reading frames and translate every ATG...Stop sequence
#save in a list

RNA_codon_table = {"CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "UUA":"L", "UUG":"L", 
            "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", 
            "GCC":"A", "GCU":"A", "GCA":"A", "GCG":"A", 
            "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", 
            "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", 
            "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", 
            "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", 
            "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", 
            "AUU":"I", "AUC":"I", "AUA":"I", 
            "UUU":"F", "UUC":"F", 
            "GAU":"D", "GAC":"D", 
            "GAA":"E", "GAG":"E", 
            "AGU":"S", "AGC":"S", 
            "AAA":"K", "AAG":"K", 
            "AAU":"N", "AAC":"N", 
            "CAU":"H", "CAC":"H", 
            "UAU":"Y", "UAC":"Y", 
            "UGU":"C", "UGC":"C", 
            "CAA":"Q", "CAG":"Q", 
            "UGG":"W", 
            "AUG":"M", 
            "UAA":"Stop", "UAG":"Stop", "UGA":"Stop"}
protein_string = ''

#attempt 1
for i in RF1:
    if i == 'AUG':
        protein_string1 += RNA_codon_table[i]
        while i != RNA_codon_table[:'Stop']:
            protein_string1 += RNA_codon_table[i]:
        else:
            break

#print(protein_string1)

#second attempt

i = 0

while i < len(RF1):
    codon = RF1[i]

    if codon == 'AUG':
        while i < len(RF1) and codon not in ('UAA', 'UAG', 'UGA'):
            protein_string1 += RNA_codon_table[codon]
            i += 1
            if i < len(RF1):
                codon = RF1[i]

        if i < len(RF1):
            i += 1  # Move to the next codon after the stop codon

    else:
        i += 1

print(protein_string1)

#both codes don´t work... I couldn´t figure it out...