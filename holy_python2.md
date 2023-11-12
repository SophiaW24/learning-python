8a.


lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for word in lst:
	print(word)

8b.

lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for name in lst:
	print('Hello!,' + name)

8c.

str="Antarctica"
for letter in str:
	print(letter)

8d.

str="Civilization"

c=0
for i in str:
	c = c + 1
print(c)

8e.

lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2=[]
for name in lst1:
	lst2.append('Dr. ' + name)
print(lst2)

8f.

lst1=[3, 7, 6, 8, 9, 11, 15, 25]
lst2=[]
for number in lst1:
	lst2.append(number**2)
print(lst2)

8g.

lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2=[]
for number in lst1:
	if number > 0:
	lst2.append(number)
print(lst2)

8h.

dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst=[]
for number in dict:
	if dict[number] > 1000:
	lst.append(dict[number] - 1000)
print(lst)
# Why dict[number] and not just number?

8i.

lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
for item in lst1:
	lst2.append(type(lst1))
print(lst2)
