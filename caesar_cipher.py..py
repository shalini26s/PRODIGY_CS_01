# Step 1: Get the message and shift value from the user
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def brute_force_decrypt(encrypted_message):
    print("Trying all possible shifts...")
    for shift in range(26):
        print(f"Shift: {shift} | Message: {decrypt(encrypted_message, shift)}")

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Decrypt without a key (brute force)")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            message = input("Enter your message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (0-25): "))
                if 0 <= shift <= 25:
                    encrypted_message = encrypt(message, shift)
                    print("Encrypted message:", encrypted_message)
                else:
                    print("Shift value must be between 0 and 25.")
            except ValueError:
                print("Please enter a valid integer for the shift value.")

        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (0-25): "))
                if 0 <= shift <= 25:
                    decrypted_message = decrypt(encrypted_message, shift)
                    print("Decrypted message:", decrypted_message)
                else:
                    print("Shift value must be between 0 and 25.")
            except ValueError:
                print("Please enter a valid integer for the shift value.")

        elif choice == '3':
            encrypted_message = input("Enter the message to decrypt: ")
            brute_force_decrypt(encrypted_message)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
