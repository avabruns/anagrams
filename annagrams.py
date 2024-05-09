import random
import time  # Add this line to import the time module

# List of words for the game
words = ["apple", "summer", "beach", "sunglasses", "strawberry", "watermelon", "cake", "love", "pool", "lemon"]

# Function to shuffle the letters of a word
def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Function to select a random word and its anagram
def select_word():
    word = random.choice(words)
    anagram = shuffle_word(word)
    return word, anagram

# Function to check if a guess is correct
def is_correct(guess, word):
    return guess.lower() == word.lower()

# Main function to run the game
def main():
    score = 0
    total_attempts = 0
    time_limit = 80 # Time limit for the game (in seconds)
    
    print("Welcome to the Anagram Game!")
    print("Unscramble the letters to form a word.")
    print("You have {} seconds to guess as many words as you can.\n".format(time_limit))
    
    start_time = time.time()
    
    while time.time() - start_time < time_limit:
        word, anagram = select_word()
        print("Anagram:", anagram)
        
        guess = input("Your guess: ")
        total_attempts += 1
        
        if is_correct(guess, word):
            score += 1
            print("Correct!\n")
        else:
            print("Incorrect. The correct word is {}\n".format(word))
    
    print("Time's up! Game over.")
    print("Your score: {}/{}".format(score, total_attempts))

if __name__ == "__main__":
    main()
