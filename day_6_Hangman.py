import random
import hangman_art
import hangman_words
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
display = []
end_of_game = False
lives = 6
guessed_words = ''

print(hangman_art.logo)
print()

for _ in range(0, len(chosen_word)):
    display.append("_")

print()
print(f"{' '.join(display)}")
print()

while end_of_game == False:

    guess = input("Guess a letter: ").lower()

    clear()
    
    if guess in guessed_words:
        print("\nYou already guessed this word. Try another one.\n")
        continue
    else:
        guessed_words += guess

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            for letter in chosen_word[index]:
                if letter == guess:
                    display[index] = guess
    else:
        lives -= 1
        print(f"You guessed the letter {guess}, that's not in the word. You lose a life.")
    
    print(f"\n{hangman_art.stages[lives]}\n{' '.join(display)}\n\nLives: {lives}\n")

    if "_" not in display:
        end_of_game = True
        print("Congratulations!!\nYou win!")
    else:
        if lives > 0:
            continue
        else:
            print("Game over!")
            end_of_game = True