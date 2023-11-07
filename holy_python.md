#1a
print ('Hello World!')

#1b
my_text = 'Hello World!'
print (my_text)

#1c
print ('Hoodie', 2, 4, 'Jeans', 'T-shirt', 9)

#2a
glass_of_water = 7
print ('I drank', glass_of_water, 'glasses of water today.')

#2b
glass_of_water = 3
glass_of_water = glass_of_water + 1
print (glass_of_water)

#3a
men_stepped_on_the_moon = 10
print (men_stepped_on_the_moon)

#3b
my_reason_for_coding = 'skill for better jobs'
print (my_reason_for_coding)

#3c
global_mean_sea_level_2018 = 21.36
print (global_mean_sea_level_2018)

#3d
staying_alive = TRUE
print (staying_alive)

#4a
men_stepped_on_the_moon = 12
answer_1 = type (men_stepped_on_the_moon)
print (answer_1)

#4b
my_reason_for_coding = 'skill for better jobs'
answer_2 = type (my_reason_for_coding)
print (answer_2)

#4c
global_mean_sea_level_delta_2018 = 21.36
answer_3 = type (global_mean_sea_level_delta_2018)
print (answer_3)

#4d
staying_alive = True
answer_4 = type (staying_alive)
print (answer_4)

#4e
my_grade = '10'
answer_5 = int (my_grade)
print (answer_5)

#4f
my_temp = 97.70
answer_6 = int (my_temp)
print (answer_6)

#4g
shoe_price = '69.99'
answer_7 = float (shoe_price)
print (answer_7)

#4h
gross_world_product = 84.84
gwp_str = str (gross_world_product)
answer_8 = 'In 2018 gross product of the world (GWP) was ' + gwp_str + ' in trillion US dollars.'
print (answer_8)

#6a
lst = [11, 100, 99, 1000, 999]
answer_1 = lst[0]
print (answer_1)

#6b
print (lst[1])

#6c
answer_1 = lst[4]
print (answer_1)

#6d
gift_list = ['socks', '4K drone', 'wine', 'jam']
gift_list.append ('pajamas')
print (gift_list)

#6e
gift_list.append (['socks', 'tshirt', 'pajamas'])
print (gift_list)

#6f
gift_list.insert (2, 'slippers')
print (gift_list)

#6g
lst = [55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
answer = lst.index (8679)
print (answer_1)

#6h
lst.append (['Navigator', 'Suburban'])

#6i
lst.remove (99)

#6j
lst.reverse ()

#6k
answer_1 = lst.count (6)

#6l
answer_1 = sum(lst)
#Why not: lst.sum () ???

#6m
answer_1 = min(lst)

#6n
answer_1 = max(lst)

#9a
str = 'It´s always darkest before dawn.'

#9b
ans_1 = str[0] + str[1] + str[-1]

#9c
str = str.replace ('.', '!')

#9d
str.lower ()

#9e
str.upper ()

#9f
str.capitalize ()

#9g
ans_1 = str.startswith ('A')

#9h
ans_1 = str.endswith ('.')

#9i
ans_1 = str.index ('v')

#9j
ans_1 = str.find ('m')

#9k
ans_1 = str.find ('X')
ans_2 = str.index ('X')

#9l
ans_1 = str.count ('a')
ans_2 = str.count ('o')

#9m
ans_1 = type (v_1)
ans_2 = type (v_2)

#9n
ans_1 = len(str)

#11a
lst.sort ()

#11b
lst.sort (reverse = False)
# ???

#11c
lst.sort (reverse = True)

#11d
gift_list.sort (reverse = True)

#11e
NFL.sort (reverse = True)
answer_1 = NFL[-1]

#11f
muni.sort (reverse = True)

#11g
key_list = list(dict.keys())
key_list.sort ()
# ???

#12a
popped_item = lst.pop ()
# how is this the last?

#12b
item = lst.pop ([-2])

#12c
italy_gdp = GDP_2018.pop ('Italy')

#17a
ans_1 = wrd[0:4]

#17b
ans_1 = wrd[3:]

#17c
ans_1 = wrd[3:6]

#17d
ans_1 = wrd[0::2]

#17e
ans_1 = wrd[1:-1:2]

#17f
ans_1= wrd[::-1]
# ???

#17g
ans_1 = wrd[-2:]

#17h
ans_1 = wrd[1:3]
