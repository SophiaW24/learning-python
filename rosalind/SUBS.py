#Finding a motif in DNA

s = 'GATATATGCATATACTT'
t = 'ATAT'
location = []
​
#loop through string as numbers
for substring in range(0, len(s)):
    #looking at 4 letters at once and checking if they match t
    if s[substring:substring + len(t)] == t:
        #append number of starting position in variable (string)
        location.append(substring+1)
#print result without brackets and commas
print(*location, sep = ' ')
2 4 10
