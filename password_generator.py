import random
import string

def generate_password(length=12):
    """Generates a secure random password with the given length."""
    
    if length < 6:
        print("⚠ Password length should be at least 6 characters for security.")
        return None
    
    # Define character sets
    letters = string.ascii_letters  # A-Z, a-z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters

    # Ensure at least one character from each category
    all_chars = letters + digits + symbols
    password = random.choice(letters) + random.choice(digits) + random.choice(symbols)
    
    # Fill the remaining length with random choices
    password += ''.join(random.choices(all_chars, k=length - 3))

    # Shuffle the password
    password = ''.join(random.sample(password, len(password)))

    return password

# Handle EOFError gracefully
try:
    length = input("Enter the desired password length (min 6): ")
    length = int(length) if length else 12  # Default length if no input
except (ValueError, EOFError):
    print("⚠ Invalid or missing input. Using default length: 12")
    length = 12

# Generate and print password
new_password = generate_password(length)
if new_password:
    print(f"🔐 Your secure password: {new_password}")