import random

from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)
web2lowerlist = list(web2lowerset)
five_letter_words = list(filter(lambda x: len(x) == 5, web2lowerlist))

print("Hello, welcome to Wordle!")
random_or_set = input("Would you like to play with a random word or have someone set a word for you? (Type RANDOM or SET): ")
if random_or_set == "SET":
    word = input("Type in a real word: ")
else:
    word = (random.choice(five_letter_words))

alet1 = (word[0])
alet2 = (word[1])
alet3 = (word[2])
alet4 = (word[3])
alet5 = (word[4])

glet1 = ""
glet2 = ""
glet3 = ""
glet4 = ""
glet5 = ""
gstat1 = ""
gstat2 = ""
gstat3 = ""
gstat4 = ""
gstat5 = ""
gstat_full = ""

def reader(guess):
    glet1 = (guess[0])
    glet2 = (guess[1])
    glet3 = (guess[2])
    glet4 = (guess[3])
    glet5 = (guess[4])
    gstat1 = letter_check(glet1, alet1)
    gstat2 = letter_check(glet2, alet2)
    gstat3 = letter_check(glet3, alet3)
    gstat4 = letter_check(glet4, alet4)
    gstat5 = letter_check(glet5, alet5)
    gstat_full = str(gstat1) + str(gstat2) + str(gstat3) + str(gstat4) + str(gstat5)
    return gstat_full


def letter_check(glet, alet,):
    if glet == alet:
        gstat = "$"
    elif glet != alet1 and glet != alet2 and glet != alet3 and glet != alet4 and glet != alet5:
        gstat = "."
    else:
        gstat = "-"
    return gstat

guess1 = input("Type in your first guess: ")
status1 = reader(guess1)
print(guess1)
print(status1)
if status1 == "$$$$$":
    print("Congrats! you got the word in 1 guess!")
else:
    guess2 = input("Type in your second guess: ")
    status2 = reader(guess2)
    print(guess1)
    print(status1)
    print(guess2)
    print(status2)
    if status2 == "$$$$$":
        print("Congrats! you got the word in 2 guesses!")
    else:
        guess3 = input("Type in your third guess: ")
        status3 = reader(guess3)
        print(guess1)
        print(status1)
        print(guess2)
        print(status2)
        print(guess3)
        print(status3)
        if status3 == "$$$$$":
            print("Congrats! you got the word in 3 guesses!")
        else:
            guess4 = input("Type in your fourth guess: ")
            status4 = reader(guess4)
            print(guess1)
            print(status1)
            print(guess2)
            print(status2)
            print(guess3)
            print(status3)
            print(guess4)
            print(status4)
            if status4 == "$$$$$":
                print("Congrats! you got the word in 4 guesses!")
            else:
                guess5 = input("Type in your fifth guess: ")
                status5 = reader(guess5)
                print(guess1)
                print(status1)
                print(guess2)
                print(status2)
                print(guess3)
                print(status3)
                print(guess4)
                print(status4)
                print(guess5)
                print(status5)
                if status5 == "$$$$$":
                    print("Congrats! you got the word in 5 guesses!")
                else:
                    guess6 = input("Type in your final guess: ")
                    status6 = reader(guess6)
                    print(guess1)
                    print(status1)
                    print(guess2)
                    print(status2)
                    print(guess3)
                    print(status3)
                    print(guess4)
                    print(status4)
                    print(guess5)
                    print(status5)
                    print(guess6)
                    print(status6)
                    if status5 == "$$$$$":
                        print("Congrats! you got the word in 6 guesses!")
                    else:
                        print("Sorry, you didn't get the word.")
                        print("The word was " + word + ".")
                