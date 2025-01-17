import random
import string

def generate_password():
    """
    A password generator that creates strong passwords 
    based on user-defined requirements.
    """
    print('Welcome to the Password Generator!')

    # Function to get valid input from the user
    def get_valid_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    # Prompt the user for input on password composition
    num_digits = get_valid_input('Enter the number of digits you want in your password: ')
    num_lowercase = get_valid_input('Enter the number of lowercase letters you want: ')
    num_uppercase = get_valid_input('Enter the number of uppercase letters you want: ')
    num_symbols = get_valid_input('Enter the number of symbols you want in your password: ')

    # Generate each component of the password
    digits = random.choices(string.digits, k=num_digits)
    lowercase_letters = random.choices(string.ascii_lowercase, k=num_lowercase)
    uppercase_letters = random.choices(string.ascii_uppercase, k=num_uppercase)
    symbols = random.choices(string.punctuation, k=num_symbols)

    # Combine all components into one list
    password_components = digits + lowercase_letters + uppercase_letters + symbols

    # Shuffle the components to ensure randomness
    random.shuffle(password_components)

    # Ensure the password starts with a capital letter if any uppercase letters exist
    if num_uppercase > 0:
        # Move an uppercase letter to the start
        for i, char in enumerate(password_components):
            if char in string.ascii_uppercase:
                password_components.insert(0, password_components.pop(i))
                break

    # Convert the list into a single password string
    password = ''.join(password_components)

    # Output the final password
    print("\nYour generated password is:")
    print(password)

# Run the password generator
if __name__ == "__main__":
    generate_password()
