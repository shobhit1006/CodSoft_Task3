import random
import string
def generate_password(len):
#character used in generating password
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(char, k=len))
    return password
def main():
    print("Welcome to the Password Generator App!")  
#input desired length
    while True:
        try:
            len = int(input("Enter the length of the password: "))
            if len <= 0:
                print("Length must be greater than zero. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
#Password Generation
    password = generate_password(len)
    print(f"\nGenerated Password: {password}")
if __name__ == "__main__":
    main()