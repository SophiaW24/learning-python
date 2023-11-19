#Complementing a strand of DNA

#Thought process
#loop through a DNA strand
#replace every letter with their complementing letter
#save as new string
#reverse string
#print string

dna_code ='GACT'
new_code = ''
​
for letter in dna_code:
    if letter == 'T':
        new_code += 'A'
    elif letter == 'G':
        new_code += 'C'
    elif letter == 'C':
        new_code += 'G'
    elif letter == 'A':
        new_code += 'T'
​
print(new_code)
​
complement_code = new_code[::-1]
print(complement_code)
CTGA
AGTC
