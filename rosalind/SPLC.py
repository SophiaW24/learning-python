fasta = open('C:/Users/sophi/Desktop/advent_calendar/FASTA_input.txt', mode='r')
data = fasta.read()
#print(data)

#make each line a string and put it into a list
genome_string = data.splitlines()
#print(genome_string)
#put gene into its own string variable
genome = genome_string[1]
#print(genome)

#put all introns into list of strings
ID = []
introns = []

for i in genome_string:
    if i.startswith('>'):
        ID.append(i)
    else:
        introns.append(i)
introns.pop(0)
#print(introns)

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


def find_intron(gene, intron):
    position = 0
    for i in range(len(gene)-len(intron)):
        if gene[i:i+len(intron)] == intron:
            position = i
    return position

#print(find_intron(genome, intron))

for intron in introns:
    start = find_intron(genome, intron)
    genome = genome[0:start] + genome[start+len(intron):]

print('gene without introns ', genome)

rna_string = ''
def transcribe(dna_string):
    for letter in dna_string:
        if letter == 'T':
            rna_string = dna_string.replace('T', 'U')
        else:
            continue
    return rna_string

print('dna to rna: ', transcribe(genome))
#print('rna: ', rna_string)

protein = ''
for i in range(len(transcribe(genome))//3):
    #connect 3 block steps to triplets as letters
    codon = transcribe(genome)[i*3:i*3+3]
    #append translating letters to triplets in string
    protein += RNA_codon_table[codon]

protein = protein.replace('Stop', '')
print('rna to protein:', protein)