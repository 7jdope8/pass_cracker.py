from urllib.request import urlopen, hashlib
import codecs

sha1hash = input("Please input the hash to crack. \n> ") #User inputs the hash to crack

with codecs.open("crackstation-human-only.txt", 'r', encoding='ISO-8859-1') as f:
    text = f.read()
# This is a list of th 10000 most common passwords in the world


# for loop through every word, split it and hash it

for guess in text.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'ISO-8859-1')).hexdigest()

        # If you find the password, spit it out and terminate
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        text.close()
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, trying next...")

# If the password didn't match through any of those, do this:
print("Password not found. ")
