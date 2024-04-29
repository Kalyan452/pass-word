import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    
    if length <= 0:
        print("Error: Password length should be greater than 0.")
    else:
        password = generate_password(length)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
