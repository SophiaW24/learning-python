#HAMM

s = 'GAGCCTACTAACGGGAT'
t = 'CATCGTAATGACGGCCT'
diff = 0

#loop trough string of numbers equal to string length
for i in range(len(s)):
    #compare both string at same position
    if s[i] == t[i]:
        continue
    #count + 1 if different
    else:
        diff +=1

print(diff)
