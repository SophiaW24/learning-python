#1.

number = 1
while number < 11:
        print(number)
        i += 1

#2.

print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")

#I had NO idea how to solve this, so I checked the solution..
#I don´t understand why stop of range is row + 1 and why do we need the variable row at all?

#3.

number = 11
for n in range(number):
        x = sum(n)
print('Enter number ' + number)
print('Sum is ' + x)

# I know this is wrong, but this was my honest attempt.. :´)

#4.

n = 2
for number in range(1, 11, 1):
        result = n * 1
print(result)

#5.

numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
        if n > 500:
                break
        elif n > 150:
                continue
        elif n % 5 == 0:

#looked up n % 5 == 0 -> meaning: divides first number by second number & returns the remainder! very cool.
#I solved this with the hints
