# Guess Secret number using while loop

secret_number = 9
guess_count = 0
guess_count_limit = 3
while guess_count < guess_count_limit:
    num_guess = int(input('Enter number '))
    guess_count += 1
    if num_guess == secret_number:
        print("Your guess was right !, You own the Game")
        break
else:
    print(" Wrong guess - Better Luck next Time :-)")
