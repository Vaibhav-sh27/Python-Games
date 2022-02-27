#Hangman Game

import random
from time import sleep

HANGMAN = (
"""
 ------
 |     |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     🙂
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |     |
 |     😐
 |    -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |     |
 |     😬
 |   /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |     |
 |     😨
 |   /-+-\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |     |
 |     😰
 |   /-+-\
 |     |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |     |
 |     🥺
 |   /-+-\
 |     |
 |     |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |     |
 |     🥴
 |   /-+-\
 |     |
 |     |
 |   |   |
 |   |   |
 |  
----------
""",
"""
 ------
 |    
 |     🤩 
 |   /-+-\
 |     |
 |     |
 |   |   |
 |   |   |
----------
""")

Youtubers = ("CARRYMINATI", "BBKIVINES", "TECHNICALGURUJI", "TANMAYBHAT", "SAMAY RAINA")
Fruits = ("APPLE", "BANANA", "ORANGE", "MANGO", "GRAPES")
Songs = ("MATARGASHTI", "52GAJ", "TITLIYAN", "KAMARIYA", "SHAYAD")



print("\t \t Welcome to Hangman!\t \t")
print()
print("\nHangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word.")
sleep(5)
y = input( """ \n\nChoose a DIFFICULTY level:
	NOOB (N)  - 6 chances for wrong word
	LAYMAN (L)  - 4 chances for wrong word
	PRO (P)  - 2 chances for wrong word
	--->  """).upper()
if y=='N':
	MAX_WRONG = 6
elif y=='L':
	MAX_WRONG = 4
elif y=='P':
	MAX_WRONG = 2

h = input("""\n\n Choose a CATAGORY to play:
  \tFRUITS (F)
  \tYOU TUBERS (Y)
  \tSONGS(S)
  \t--->  """).upper()
if h == 'F':
	WORDS = Fruits
elif h == 'Y':
	WORDS = Youtubers
elif h == 'S':
	WORDS = Songs

word = random.choice(WORDS)
POSITIVE_SAYINGS = ("Well done!", "Awesome!", "You Legend!")

so_far = ("-") * len(word)
used = []
wrong = 0

input("\nPress Enter to START: ")

while wrong < MAX_WRONG and so_far != word:
    print()
    print(HANGMAN[wrong])
    print("Word so far: ", so_far)
    print("Letters used: ", used)

    guess = input("Guess a letter: ").upper()
    sleep(1) # Time delay - allows userfriendly reading
    print()

    while guess in used:
        print("Try again... You've already used this letter")
        guess = input("Guess a letter: ").upper()
        sleep(1)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS),"...Updating word so far...")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new 

    else:
        print("INCORRECT! Try again!")
        wrong += 1

print("Calculating result...")
sleep(1)
if wrong == MAX_WRONG:
    print(HANGMAN[7])
    print("UNLUCKY! Better luck next time!")

else:
	print(HANGMAN[8])
	print("WINNER! Congratulations!")

print()
print()
hm= input("Move to Home Page ? (Y/N)").upper()
if hm=="Y":
    from subprocess import call
    call(["python","main.py"])
else:
    input("Press Enter to Leave: ")