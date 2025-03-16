import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo


# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(logo)


chosen_word = random.choice(word_list).lower()
print(chosen_word)
display = ""
placeholder = []
word_length = len(chosen_word)
for position in range(word_length):
    placeholder.append("_")
for char in placeholder:
    display += char
print("Word to guess: " + display)

game_over = False
correct_letters = []

while not game_over:



    # # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"You have {lives}/6 lives left")
    guess = input("Guess a letter: ").lower()

    # # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in correct_letters:
        print(f"You have already guessed this letter {guess}, try again")
        print("Word to guess: " + display)
    elif guess in chosen_word:
        i = 0
        display = ""
        for letter in chosen_word:
            if letter == guess:
                placeholder[i] = letter
                correct_letters.append(guess)
            i += 1
        if len(correct_letters) != word_length:
            for char in placeholder:
                display += char
            print("Word to guess: " + display)
        elif len(correct_letters) == word_length:
            for char in placeholder:
                display += char
            print("You win!!! The word was " + display)
            game_over = True

    elif guess not in chosen_word:
        lives -= 1
        print("The guess was wrong,you lose a life")
        print(stages[lives])
        display = ""
        for char in placeholder:
            display += char
        print("Word to guess: " + display)

        if lives == 0:
            game_over = True
            print("The word was " + chosen_word + ". You Lose!!!")




