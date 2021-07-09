# Remove the duplicates of a list.
# Take an empty list and add element if not there & iterate with for loop.
numbers = [2, 3, 4, 5, 13, 56, 4, 4, 5, 2, 2, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


