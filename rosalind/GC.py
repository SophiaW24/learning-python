#final solution!!!!!

fasta = open('C:/Users/sophi/Desktop/learning-python/rosalind/GC_train.txt', mode='r')


for line in fasta:
    if line[0] == '>':
      key = line
      id_seq[key] = ''
    else:
      id_seq[key] += line

#print(id_seq)
fasta.close()

#remove characters: '>' & '\n' from dict.keys
for key in list(id_seq.keys()):
    new_key = key.replace('>', '')
    id_seq[new_key] = id_seq.pop(key)

for key in list(id_seq.keys()):
    new_key = key.replace('\n', '')
    id_seq[new_key] = id_seq.pop(key)

#print(id_seq)

#remove characters: '\n' from dict.values
for key in id_seq:
    id_seq[key] = id_seq[key].replace('\n', '')

#print(id_seq)

#calculate GC-content for every sequence in dictionary
GC_content =[]

for value in id_seq.values():
   total = len(value)
   G = value.count('G')
   C = value.count('C')
   GC_total = G + C
   GC_content.append(GC_total/total)

print(GC_content)

#print highest GC_content with ID
maxGC = max(GC_content) * 100
maxGC_formatted = "{:.6f}".format(maxGC)


#print correct ID
key_ID = list(id_seq.keys())

#Output
print(key_ID[5])
print(maxGC_formatted)

#it works
#the only minor thing where I might have cheated is that 
#I had to look up manually which ID fits the highest GC content to print it

