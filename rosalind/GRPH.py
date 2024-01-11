#Given: DNA strings in Fasta format
#Return: IDs of overlapping DNA strings -> they have to overlap in 3 letters in a row

#Steps:
# - put data into dictionary
# - compare first three letters of a string with last three letters of all other strings
# - do not compare one string with itself
# - print IDs of overlapping strings next to each other

#---------------------Code works only for example not for rosalind file--------------------------------------------

fasta = open('C:/Users/sophi/Desktop/learning-python/rosalind/Data_GRPH.txt', mode='r')
#data = fasta.read()
#print(fasta)

dict_dna = {}
for line in fasta:
    if line[0] == '>':
      key = line
      dict_dna[key] = ''
    else:
      dict_dna[key] += line

#print(dict_dna)
fasta.close()

#remove characters: '>' & '\n' from dict.keys
for key in list(dict_dna.keys()):
    new_key = key.replace('>', '')
    dict_dna[new_key] = dict_dna.pop(key)

for key in list(dict_dna.keys()):
    new_key = key.replace('\n', '')
    dict_dna[new_key] = dict_dna.pop(key)

#print(dict_dna)

#remove characters: '\n' from dict.values
for key in dict_dna:
    dict_dna[key] = dict_dna[key].replace('\n', '')

#print(dict_dna)

#print(dict_dna.keys(), dict_dna.values())

id1 = []
id2 = []

#loop through ids
for i in dict_dna.keys():
   #loop through ids per id from loop before
   for j in dict_dna.keys():
      #avoid comparing one string with itself
      if i != j:
         #if last three letters of a string matches the first three letters of a string
         string1 = dict_dna[i][:3:]
         string2 = dict_dna[j][len(dict_dna[j])-3:len(dict_dna[j]):]
         if string1 == string2:
            #append ids into two seperate lists
            id1.append(i)
            id2.append(j)

#print(id1)
#print(id2)

#print all matching ids next to each other
for i in range(len(id1)):
   print(id1[i], id2[i])
            
#ids = []
#strings = []
#
#for key, value in dict_dna.items():
#    ids.append(key)
#    strings.append(value)
#
#print(type(ids))
#
#for i in range(len(strings)):
#    for DNA in strings:
#        if strings[i] != DNA and strings[i][-3 : ] == DNA[0 : 3]:
#            print(ids[strings[i]], ids[DNA])