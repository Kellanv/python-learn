secret_word = "fish"
guesses = 5
print("Welcome to the guessing game! You currently have " + str(guesses) + " guesses left to guess the word!")
guess = input("Type your first guess: ")

while guess != secret_word:
    guesses -= 1
    print("You now have " + str(guesses) + " guesses left.")
    guess = input("Type your next guess: ")
    if guesses == 1:
        guess = secret_word

if guesses > 1:
    print("Congrats! You found the secret word with " + str(guesses - 1) + " guesses left!")
else:
    print("Sorry, you didn't guess the secret word in time.")
    