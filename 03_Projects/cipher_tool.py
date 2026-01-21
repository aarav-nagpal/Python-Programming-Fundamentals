import random
import string
import os

def get_random_chars(length=3):
    """Generates a random string of fixed length."""
    letters = string.ascii_letters  # Contains both lowercase and uppercase
    return ''.join(random.choice(letters) for _ in range(length))

def encrypt_text(text):
    """Encrypts text by shifting characters and adding random noise."""
    words = text.split()
    result = []
    
    for word in words:
        if len(word) < 3:
            # Simple reverse for short words
            result.append(word[::-1])
        else:
            # Logic: [Random] + [Word without 1st char] + [1st char] + [Random]
            start_noise = get_random_chars()
            end_noise = get_random_chars()
            encrypted_word = f"{start_noise}{word[1:]}{word[0]}{end_noise}"
            result.append(encrypted_word)
            
    return " ".join(result)

def decrypt_text(text):
    """Reverses the encryption logic to retrieve original text."""
    words = text.split()
    result = []
    
    for word in words:
        if len(word) < 3:
            result.append(word[::-1])
        else:
            # Remove the 3 random characters from start and end
            core_word = word[3:-3]
            # Move the last character back to the front
            original_word = f"{core_word[-1]}{core_word[:-1]}"
            result.append(original_word)
            
    return " ".join(result)

def main():
    print("=== SECRET MESSAGE TOOL ===")
    try:
        choice = int(input("1: Encrypt (read from decoded.txt)\n0: Decrypt (read from coded.txt)\nEnter choice: "))
        
        if choice == 1:
            if not os.path.exists("decoded.txt"):
                print("Error: 'decoded.txt' file not found. Please create it first.")
                return
                
            with open("decoded.txt", "r") as f:
                data = f.read()
            
            output = encrypt_text(data)
            
            with open("coded.txt", "w") as f:
                f.write(output)
            print("Success! Message encrypted to 'coded.txt'.")
            
        elif choice == 0:
            if not os.path.exists("coded.txt"):
                print("Error: 'coded.txt' file not found.")
                return

            with open("coded.txt", "r") as f:
                data = f.read()
            
            output = decrypt_text(data)
            
            with open("decoded.txt", "w") as f:
                f.write(output)
            print("Success! Message decrypted to 'decoded.txt'.")
            
        else:
            print("Invalid input! Please enter 1 or 0.")
            
    except ValueError:
        print("Error: Please enter a number.")

if __name__ == "__main__":
    main()
