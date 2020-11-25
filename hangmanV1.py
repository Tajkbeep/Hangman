user_name = input("Hi, welcome to a boof version of hangman, please enter your name: ")
ready_to_play = input("Are you ready to play?: ")

if ready_to_play == "no":
    print("Okay, too bad... GAME OVER")
else:
    print("YAY! lets play\n")

#this is where you change the word
word = "Salmon"
print("\nOkay I will give you a hint, your word is", len(word), "characters long")

guesses = ''
turns = 8

while turns > 0:
    failed = 0
    for char in word.lower():
        if char in guesses:
            print(char)
        else:
            print("\n_")
            failed += 1
    if failed == 0:
        print("You Win!")
        print("The word was: ", word.lower())
        break



    guess = input ("Guess a character: ")
    guesses += guess

    if guess not in word.lower():
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, "more chances")
        if turns == 0:
            print("You lose")


