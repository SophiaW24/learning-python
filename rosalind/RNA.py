#transcribe DNA into RNA

#string with letters of A C G T saved as dna_code
#loop trough every letter
#if letter T is encountered...
#replace T with U and safe as string in rna_code
#if any other letter is encountered continue loop without change
#print rna code

dna_code ='GACT'
​
for letter in dna_code:
    if letter == 'T':
        rna_code = dna_code.replace('T', 'U')
    else:
        continue
​
print(rna_code)
GACU
