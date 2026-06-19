# : The Perfect Guess

# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please” . Similarly, if the user’s guess is too low, the program prints “Higher number please” .
# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.


import random
n = random.randint(1, 50)
num = -1
guess = 0

while(num != n):
    guess +=1
    num = int(input('Guess the number: '))

    if(num > n):
        print('lower number please: ')

    else:
        print('higher number please: ')


print(f'You have gussed the number in {guess} atempts: ')
