from time import sleep

print("""\t\t\tWELCOME TO LCLV GAMES\t\t\t""")
sleep(2)
print("Hello There!")
sleep(2)
u= input("""\n--->  Which Game you would like to play?
\tTic TaC Toe (T)
\tHangman   (H)
\tSong Gussing Game (S)
-->  """).upper()

if u=='T':
  from subprocess import call
  call(["python", "Tictak.py"])

elif u=='H':
  from subprocess import call
  call(["python", "Hangman.py"])

elif u=='S':
  from subprocess import call
  call(["python", "song_guss.py"])
