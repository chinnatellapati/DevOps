# Handling exceptions in python


try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age can not be Zero')
except ValueError:
    print("Value can not be string ")



