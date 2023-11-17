#Rosalind INI6: 



#First try -> didn´t work completly 
 

str = ('We tried list and we tried dicts also we tried Zen') 
dict = {} 

for word in str.split(' '): 
    if word not in dict: 
        dict[word] = str.count(word) 

for key, value in dict.items(): 
    print(key, value) 

 

#Solution solution 
 

str = 'We tried list and we tried dicts also we tried Zen' 
dict = {} 
words = str.split() 

for word in words: 
    if word in dict: 
        dict[word] += 1 
    else: 
        dict[word] = 1 

for key, value in dict.items():
    print(key, value) 
