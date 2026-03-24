import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""

    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: Select at least one character type!"

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def main():
    print("🔐 PASSWORD GENERATOR")

    try:
        length = int(input("Enter password length: "))

        use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()
