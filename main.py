# Import Logo and Stages from hangman_art, import words from hangman_words
from hangman_art import stages, logo
from hangman_words import word_list
import random

# Print the hangman logo
print(logo)

# Choose random words from the word list for the game
random_word = random.choice(word_list)
print(random_word)

placeholder = ""
lives = 6

for i in range(0, len(random_word)):
    placeholder += "_"

print(f"Word to Guess: {placeholder}")

correct_letters = []
incorrect_letters = []

game_over = False

while not game_over:
    print(f"***************{lives}/6 LIVES LEFT***************")

    # Ask user to guess a letter
    guess_a_letter = input("Guess a letter: ").lower()
    
    # Tell the user if they have already guessed this letter
    if guess_a_letter in correct_letters:
        print(f"You already guessed {guess_a_letter}. Guess another letter.")
    
    if guess_a_letter in incorrect_letters:
        print(f"You already guessed {guess_a_letter}. Guess another letter.")
        

    display = ""

    for letter in random_word:
        if letter == guess_a_letter:
            display += letter
            correct_letters.append(guess_a_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(f"Word to guess: {display}")
    

    if guess_a_letter not in random_word:
        if guess_a_letter not in incorrect_letters:
            print(f"You guessed {guess_a_letter}, that's not in the word. You lose a life.")
            lives -= 1
            incorrect_letters.append(guess_a_letter)        

            if lives == 0:
                game_over = True
                print(f"You are out of lives, Game Over!!!\nCorrect word was {random_word}.")
                
    
    if "_" not in display:
        game_over = True
        print("You guessed the word\n***************Congratulations You Won****************")
        
    
    print(stages[lives])
        

    
          


