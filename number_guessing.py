import random
import os

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue
            
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"Your Score: {score}/100")
            break

def word_counter():
    print("\n--- Word Counter & Frequency Analysis ---")
    filename = input("Enter the text file name (e.g., sample.txt): ")
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Creating a new sample file...")
        with open(filename, "w", encoding="utf-8") as f:
            f.write("Python is an amazing programming language. Learning Python is easy and fun.")
        print(f"File '{filename}' created successfully.")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
            
        words = text.split()
        total_words = len(words)
        print(f"\nTotal Words in File: {total_words}")
        
        word_freq = {}
        for word in words:
            clean_word = word.strip('.,!?;:"').lower()
            if clean_word:
                word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
                
        print("\nWord Frequencies:")
        for w, freq in word_freq.items():
            print(f"'{w}': {freq} time(s)")
            
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Number Guessing Game")
        print("2. Word Counter Tool")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_counter()
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()