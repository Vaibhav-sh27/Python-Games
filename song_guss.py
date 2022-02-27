#Song Gussing Game
from playsound import playsound
import random
from time import sleep

def oldsong():
    global n
    if word=='1':
        playsound("Songs\Aane is uske.mp3")
        n="AANE SE USKE"
    elif word=='2':
        playsound("Songs\AudioCutter_Yeh Parda Hata Do - Ek Phool Do Mali _ Hit Romantic Song _ Sadhana_ .mp3")
        n="YE PARDA HATA DO"
    elif word=='3':
        playsound("Songs\Bholi si surat.mp3")
        n="BHOLI SI SURAT"
    elif word=='4':
        playsound("Songs\AudioCutter_Mere meheboob.mp3")
        n="MERE MEHEBOOB"
    elif word=='5':
        playsound("Songs\Bhook Surat Dil ke khote.mp3")
        n="BHOLI SURAT DIL KE KHOTE"
def newsong():
    global n
    if word=='1':
        playsound("Songs\Saibo.mp3")
        n="SAIBO"
    elif word=='2':
        playsound("Songs\Sanam teri kasam.mp3")
        n="SANAM TERI KASAM"
    elif word=='3':
        playsound("Songs\Proper patola.mp3")
        n="PROPER PATOLA"
    elif word=='4':
        playsound("Songs\Zara zara.mp3")
        n="ZARA ZARA"
    elif word=='5':
        playsound("Songs\Shayad.mp3")
        n="SHAYAD"
def englishsong():
    global n
    if word=='1':
        playsound("Songs\Memories.mp3")
        n="MEMORIES"
    elif word=='2':
        playsound("Songs\cradles.mp3")
        n="CRADLES"
    elif word=='3':
        playsound("Songs\Senorita.mp3")
        n="SENORITA"
    elif word=='4':
        playsound("Songs\Criminal.mp3")
        n="CRIMINAL"
    elif word=='5':
        playsound("Songs\Girls like you.mp3")
        n="GIRLS LIKE YOU"


WORDS = ("1", "2", "3", "4", "5")

print("\t \t Welcome to Song Gussing Game\t \t")
print()
print("""\nGuess the song is a simple addictive music trivia game. You just need to listen to the song and guess the title of the song. """)
sleep(5)
def game():
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

    h = input("""\n\n Choose GENRE to play:
    \tOLD SONGS (O)
    \tNEW SONGS (N)
    \tENGLISH SONGS (E)
    \t--->  """).upper()
    global word
    word = random.choice(WORDS)
    print("Listen to song carefully...... ")
    if h == 'O':
        oldsong()
    elif h == 'N':
        newsong()
    elif h == 'E':
        englishsong()


    POSITIVE_SAYINGS = ("Well done!", "Awesome!", "You Legend!")

    used = []
    wrong = 0
    guess = 0
    s = input("Want to Listen AGAIN ?  (Y/N) ").upper()
    while s=='Y':
        if h == 'O':
            oldsong()
        elif h == 'N':
            newsong()
        elif h == 'E':
            englishsong()
        break
    input("\nPress Enter to START: ")

    #guess = input("Guess the song TITLE: ").upper()
    #sleep(1) # Time delay - allows userfriendly reading
    print()
    while wrong < MAX_WRONG and guess!=n:
        print()
        print("SONG TITLES used: ", used)

        guess = input("Guess the song TITLE: ").upper()
        sleep(1) # Time delay - allows userfriendly reading
        print()

        while guess in used:
            print("Try again... You've already used this name")
            guess = input("Guess the song TITLE: ").upper()
            sleep(1)
            print()
        used.append(guess)

        if guess == n:
            print(random.choice(POSITIVE_SAYINGS))

        else:
            print("INCORRECT! Try again!")
            wrong += 1

    print("Calculating result...")
    sleep(1)
    if wrong == MAX_WRONG:
        print("UNLUCKY! Better luck next time!")

    else:
        print("WINNER! Congratulations!")
    

game()
print()
k ='Y'
while(k=='Y'):
    k=input("Want to play AGAIN ?  (Y/N)").upper()
    if k=='Y':
        game()
hm= input("Move to Home Page ? (Y/N)").upper()
if hm=="Y":
    from subprocess import call
    call(["python","main.py"])
else:
    input("Press Enter to Leave: ")