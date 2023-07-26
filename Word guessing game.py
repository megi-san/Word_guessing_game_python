import random

words = ['rainbow', 'computer', 'science', 'programming',
        'python', 'mathematics', 'player', 'condition',
        'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
guesses = "_"*len(word)
win = False

print("""Good Luck!
Guess the characters""")

print("_\n"*len(word))

while not win:
        guesse = input("Guess the characters : ")
        if len(guesse) != 1: 
            print("One word at the time please. ")
            continue
        if guesse in guesses : print("You already tried this character.")
        for i in range(len(word)):
            if (guesse).upper() == (word[i]).upper():
                guesses = guesses[:i]+ word[i]+guesses[i+1:]
            print(guesses[i])
        if not("_" in guesses):win = True

print("Congratulations you found it was "+ word )
