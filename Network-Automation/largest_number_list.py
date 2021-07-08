# Program to print largest number in list.

numbers = [8, 3, 76, 7, 45]
max = numbers[0] # assuming first number in list is larger. If first number is not large, we need to reset number and move on.
for number in numbers:
    if number > max:
        max = number
print(max)



