import random as rd
counter = 1
magic_number = rd.randint(1,10)
print("Welcome to the guess number game!")


while counter <= 10:
  user_number=int(input("Guess the number between 1 - 10: "))
  if magic_number == user_number:
    print("You're correct!")
    break
  else:
    print("You're NOT correct!")
  counter = counter+1

print("You used up all of your guesses.")
