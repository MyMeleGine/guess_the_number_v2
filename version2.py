import random as rd

magic_number = rd.randint(1,10)
print("Welcome to the guess number game!")


while True:
  user_number=int(input("Guess the number between 1 - 10: "))
  if magic_number == user_number:
    print("You're correct!")
    break
  else:
    print("You are NOT correct!")
