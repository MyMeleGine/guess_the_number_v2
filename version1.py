import random as rd

magic_number = rd.randint(1,10)
print("Welcome to the guess number game!")
user_number=int(input("Guess the number between 1 - 10: "))

if magic_number == user_number:
  print("You're correct!")
else:
  print("You are NOT correct!")
