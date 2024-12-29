import random
import string

def password_generator():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 for better security.")
            return

        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
        include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        include_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        characters = string.ascii_lowercase  # Start with lowercase letters
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_special:
            characters += string.punctuation

        if not characters:
            print("You must include at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")

if __name__ == "__main__":
    password_generator()
