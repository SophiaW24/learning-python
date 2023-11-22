#Translating RNA into Protein
#still working the solution, couldn´t figure it out yet

RNA_string = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
protein_string = ''
RNA_codon_table = {'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G' }

#loop trough string in blocks of 3
for i in range(len(RNA_string)%3):
    #translate i to AminoAcid (AA)
    for key in RNA_codon_table.items():
        #save output in string/append trnaslation in new string
        protein_string += RNA_codon_table.values

print(protein_string)
