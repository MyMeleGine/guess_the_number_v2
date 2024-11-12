import random as rd

counter = 1
magic_number = rd.randint(1,100)
guess_list = []
player_score = 0
computer_score = 0
win = False

print("==== WELCOME TO THE GUESSING GAME ====")

while True:
    while counter <= 10:
        print("You have already guessed: ")
        print(guess_list)
        user_number=int(input("Guess the number between 1 - 100: "))
        guess_list.append(user_number)
        if magic_number == user_number:
            print("You're correct!")
            win = True
            break
        else:
            print("Wrong!")
            
            if user_number > magic_number:
                print("Too high!")
            elif user_number < magic_number:
                print("Too Low!")
            print()
            
        counter = counter+1

    if win:
        player_score += 1
        print("Great job! you did not waste your guesses!")
    else:
        computer_score += 1
        print("You used up all of your guesses.")
    
    play_again = input("Do you want to play again? (y/n)") == "y"
    if not play_again:
        print("Thank you for playing!")
        break
    
    magic_number = rd.randint(1,100)
    counter = 0
    guess_list = []

    print("==== Scoreboard ====")
    print(f"{player_score}-{computer_score}")
    print("====================")
    
