Introduction
The purpose of this project is to create a Geography Hangman game in Python that can be played by running the code. The game allows the player to make a set number of guesses before ending the game and showing the correct answer. It is repeatable and so the player can play again or quit. A scoreboard is also displayed.

Requirements
	•	Python version 3.12+: [download link: https://www.python.org/downloads/]
	•	Visual Studio Code: [download link: https://code.visualstudio.com/download]
	•	GitHub Repository: [https://github.com/anjrehal093/Hangman_Game.git]

The GitHub repository contains the Hangman game as a Python file, this README file and the flowchart for development.

How To Run
	1.	Click on the link to the GitHub repository.
	2.	Click on the Python game file and download it: [Hangman_game_v2.py]. 
	3.	Open the game file with Visual Studio Code.
	4.	Make sure the terminal window is open at the bottom half of the screen.
	5.	Press the triangle in the top right to run the code.
	6.	It will come up with a prompt for you to start the game in the terminal window.

How To Play 
	1.	Once the code has been run a message will appear in the terminal prompting the player to enter their name. Once this has been done press enter.
	2.	Another message will appear asking the player to enter a number for game difficulty. Enter a number from the list and press enter.
	3.	The game will then begin. The message will show how many letters the word has and the player will be asked to guess a letter.
	4.	If the guessed letter is correct,  it will appear on the dashes in the terminal and the guessed letters list. The hangman stage will also appear as a reminder for the player.
	5.	If the player doesn’t input a single letter or they have already guessed that letter, error messages will pop up in the terminal.
	6.	Once the game has ended, it will tell the player whether they have won or lost and the correct word.
	7.	When the round ends, the player will be asked if they want to play again.
	8.	At the end a scoreboard will appear in the terminal.


Dictionary
The different stages of the hangman drawings are shown below.
‘r’ was used before the quotation marks to counteract syntax errors due to the ‘\’ character.

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