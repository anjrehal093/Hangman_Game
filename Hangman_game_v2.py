import random

word_bank = {
    1: ["CUBA", "SWEDEN", "RUSSIA", "FIJI"],
    2: ["ARGENTINA", "PANAMA", "URUGUAY", "FINLAND"],
    3: ["PHILIPPINES", "TANZANIA", "NETHERLANDS", "AZERBAIJAN"]
}

hangman_stages = [
r"""
   ---------
       |   |
           |
           |
           |
           |
  ===========         
""",
r"""
   ---------
       |   |
       O   |
           |
           |
           |
  =========== 
""",
r"""
   ---------
       |   |
       O   |
       |   |
           |
           |
  =========== 
""",
r"""
   ---------
       |   |
       O   |
      /|   |
           |
           |
  =========== 
""",
r"""
   ---------
       |   |
       O   |
      /|\  |
           |
           |
  =========== 
""",
r"""
   ---------
       |   |
       O   |
      /|\  |
      /    |
     /     |
  =========== 
""",
r"""
   ---------
       |   |
       O   |
      /|\  |
      / \  |
     /   \ |
  =========== 
"""
]

guess_word = None
guessed_letters = []
lives = 6
game_active = True
history = []
word_completed = False
gen_word = None
game_history = []
game_difficulty = None

game_difficulty_map = {1:"Easy",2:"Medium", 3:"Hard"}

player_name = str(input("Please enter your name:"))

print("Hello {}, welcome to this geography hangman game!".format(player_name))

def setup():
    global game_difficulty
    print("Please choose a difficulty level.\n{} for {}\n{} for {}\n{} for {}".format(1, "Easy", 2, "Medium", 3, "Hard"))
    while True:
        try:
            game_difficulty = int(input("Please enter a number for the game mode:"))
            if game_difficulty not in range (1,4):
                print("Enter a number (1, 2 or 3.")
                continue
            break
        except ValueError:
            print("That is not a valid number. Please enter 1,2 or 3.")

    global gen_word 
    gen_word = random.choice(word_bank[game_difficulty])
    global guess_word 
    guess_word = ["_"] * len(gen_word)
    
def update_history():
    global game_history, player_name, lives, gen_word, guessed_letters, game_difficulty
    game_history.append([player_name, lives, gen_word, guessed_letters, game_difficulty])
    
def show_history():
    global game_history, player_name
    print("Stats for Player {} during this run".format(player_name))
    for i in range(0,len(game_history)):
        if game_history[i][1] == 0:
            print("on your {}th attempt you failed to guess {}".format(i+1, game_history[i][2]))
        else:
            print("on your {}th attempt you guessed {} with {} lives remaining".format(i+1, game_history[i][2], game_history[i][1]))
        
def check_complete():
    global lives, word_completed, gen_word
    if gen_word == "".join(guess_word):
        word_completed = True
        update_history()
    elif lives == 0:
        update_history()

def guess_letter(letter):
    
    guessed_letters.append(letter)
    
    if letter in gen_word:
        print("Good job! '{}' is in the word.".format(letter))
        for index, true_letter in enumerate(gen_word):
            if letter == true_letter:
                guess_word[index] = true_letter
                print(guess_word)
        check_complete()
    else:
        global lives
        lives -= 1
        check_complete()
        print("Sorry, '{}' is not in the word. You have {} lives left.".format(letter,lives))
        
    print(hangman_stages[6-lives])
    print(" ".join(guess_word))
    print("Guessed letters:", ", ".join(guessed_letters))
        
def play():
    while not word_completed and lives > 0:
        letter = input("\nGuess a letter:").upper()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter only a single letter.")
            continue

        if letter in guessed_letters: 
            print("You already guessed that letter.")
            continue

        guess_letter(letter)

    if word_completed:
        print("\nCongratulations! You win {}! It was '{}'".format(player_name, gen_word))
    else:
        print("\nGame over! You lost {}. The country was '{}'.".format(player_name, gen_word))   



while game_active:
    setup()
    print("Let's begin {}. The word has {} letters.".format(player_name, len(gen_word)))
    print(" ".join(guess_word))
    play()
    
    while True:
        try:
            play_again = int(input("Please enter 1 to play again, 2 to quit: "))
            if play_again not in range (1,3):
                print("Enter the number 1 or 2")
                continue
            break
        except ValueError:
            print("That is not a valid number. Please enter 1 or 2")
    
    if play_again == 1:
        lives = 6
        word_completed = False
        guessed_letters = []
    else:
        game_active=False

show_history()

