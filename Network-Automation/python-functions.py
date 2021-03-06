# Python functions

def greet_user():
    print('Hi There')
    print('Welcome On Board ...!')


print("Start")
greet_user()
print("Finish")




# passing parameters 

def greet_user(first_name, last_name):
    print(f'Hi {first_name}, {last_name}')
    print('Welcome On Board ...!')


print("Start")
greet_user('John', 'smith')
print("Finish")

# Keyword arguments 

# Python functions

def greet_user(first_name, last_name):
    print(f'Hi {first_name}, {last_name}')
    print('Welcome On Board ...!')


print("Start")
greet_user(first_name='John', last_name='smith')
print("Finish"


# Importance of Keyword arguments are to make code more resable .

greet_user(50, 10,0.1) # not clear for someone new 
greet_user(total=50, shipping=10,discount=0.1) # more redable
