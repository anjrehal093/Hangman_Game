#imports the random library
import random


#create a dictionary of the words
word_bank = {
    1: ["KENYA", "SWEDEN", "RUSSIA", "FIJI","ITALY","FRANCE","INDIA"],
    2: ["ARGENTINA", "PANAMA", "URUGUAY", "FINLAND","GERMANY","MONACO","COLOMBIA"],
    3: ["PHILIPPINES", "TANZANIA", "NETHERLANDS","LUXEMBOURG", "AZERBAIJAN","UGANDA","MYANMAR"]
}


#defines 7 hangman stages (from the start of the game to the end)
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


#define the global variables and set number of lives
guess_word = None
guessed_letters = []
lives = 6
game_active = True
history = []
word_completed = False
gen_word = None
game_history = []
game_difficulty = None


#Asks player to input their name
player_name = str(input("Please enter your name:"))


#prints a statement for introduction
print("Hello {}, welcome to Geography Hangman!".format(player_name))

"""
function to set up difficulty 
choice at start of game 
"""
def setup():
    global game_difficulty
    #allows player to choose a difficulty level
    print("Please choose a difficulty level.\n{} for {}\n{} for {}\n{} for {}".format(1, "Easy", 2, "Medium", 3, "Hard"))
    #error statement to prevent crashing
    while True:
        try:
            game_difficulty = int(input("Please enter a number for the game mode:"))
            if game_difficulty not in range (1,4):
                print("Enter a number (1, 2 or 3.")
                continue
            break
        except ValueError:
            print("That is not a valid number. Please enter 1,2 or 3.")


#chooses random word from dictionary based on chosen difficulty
    global gen_word 
    gen_word = random.choice(word_bank[game_difficulty])
    global guess_word 
    guess_word = ["_"] * len(gen_word)


"""function for scoreboard with variables required
 in final score to update when game is repeated"""
def update_history():
    global game_history, player_name, lives, gen_word, guessed_letters, game_difficulty
    game_history.append([player_name, lives, gen_word, guessed_letters, game_difficulty])


"""function for showing the final
score when game is endedfrom the
start of the game to the last game
played by the same person"""   
def show_history():
    global game_history, player_name
    print("Stats for {} :".format(player_name))
    for i in range(0,len(game_history)):
        if game_history[i][1] == 0:
            print("On attempt {} you failed to guess {}".format(i+1, game_history[i][2]))
        else:
            print("On attempt {} you guessed {} with {} lives remaining".format(i+1, game_history[i][2], game_history[i][1]))


#function to check if word is guessed correct or wrong"
def check_complete():
    global lives, word_completed, gen_word
    if gen_word == "".join(guess_word):
        word_completed = True
        update_history()
    elif lives == 0:
        update_history()


#function to allow user to guess letters
def guess_letter(letter):
    
    guessed_letters.append(letter)
    
    """instructs game to reduce number of lives if the
    letter guessed is wrong and refers to check complete function"""
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

    #informs player of lives left and which letters they have already guessed    
    print(hangman_stages[6-lives])
    print(" ".join(guess_word))
    print("Guessed letters:", ", ".join(guessed_letters))


"""prompts user to make a guess and prints an error
statement if a single letter from the alphabet is not used"""   
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


#
    if word_completed:
        print("\nCongratulations! You win {}! It was '{}'".format(player_name, gen_word))
    else:
        print("\nGame over! You lost {}. The country was '{}'.".format(player_name, gen_word))   



#prompts game to start if repeated and links to play function for instructions
while game_active:
    setup()
    print("Let's begin {}. The country has {} letters.".format(player_name, len(gen_word)))
    print(" ".join(guess_word))
    play()
    
    #gives user the choice to play again or quit
    while True:
        try:
            play_again = int(input("Please enter 1 to play again, 2 to quit: "))
            if play_again not in range (1,3):
                print("Enter the number 1 or 2")
                continue
            break
        except ValueError:
            print("That is not a valid number. Please enter 1 or 2")
    
    #restarts game with full lives and ends game if player chooses
    if play_again == 1:
        lives = 6
        word_completed = False
        guessed_letters = []
    else:
        game_active=False


#states game has ended and shows players statistics
print("Thanks for playing {}! Goodbye".format(player_name))
show_history()

