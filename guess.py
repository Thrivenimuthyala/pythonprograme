import random
guess=random.randint(1,100)
print("guess any number from 1 to 100:")
while True:
    guessingNumber=int(input("enter you guess:"))
    if guess>guessingNumber:
        print("you guessed smaller number")
    elif guess<guessingNumber:
        print("you guessed bigger number")
    else:
        print("you are guessed current")
        break
# import random
# secret_number = random.randint(1, 100)
#
# print("Guess the number between 1 and 100!")
#
# while True:
#     guess = int(input("Enter your guess: "))
#
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
