import random as rd

counter = 1
magic_number = rd.randint(1,100)
guess_list = []
win = False

print("Welcome to the guess number game!")

while counter <= 5:
    print("You previously guessed:")
    print(guess_list)
    user_number=int(input("Guess the number between 1 - 100: "))
    guess_list.append(user_number)
    if magic_number == user_number:
        print("You're correct!")
        win = True
        break
    else:
        print("You're NOT correct!")
        if user_number > magic_number:
            print("Too high!")
        elif user_number < magic_number:
            print("Too Low!")
        print()
        
    counter = counter+1
  
if win:
  print("Great job! you did not waste your guesses!")
else:
  print("You used up all of your guesses.")

