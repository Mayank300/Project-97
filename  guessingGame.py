import random

print('Hello, what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number from 1 to 9.')
secret_number = random.randint(1, 9)

for num_guesses in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    if guess < secret_number:
        print('Your guess was too low.')
    elif guess > secret_number:
        print('Your guess was too high.')
    else:
        break

if guess == secret_number:
    print('Nice job, ' + name + ', you guessed my number in ' + str(num_guesses) + ' guesses!')
else:
    print('Oh no. You ran out of guesses. Try again.')