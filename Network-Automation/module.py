utils.py

def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num




app.py 


import utils

numbers = [8, 1393, 976, 7, 45]
max_num = utils.find_max(numbers)
print( max_num)



