import os


def save_passwords_locally(passwords):
    with open("passwords.txt", "w") as file:
        for password in passwords:
            decoded_line = password.decode("utf-8")
            file.write(decoded_line)


def local_passwords_file_exists():
    return os.path.exists("passwords.txt")


def get_local_passwords(args):
    try:
        passwords = []
        with open("passwords.txt", "r") as file:
            passwords = [line.strip() for line in file.readlines()]
        if not passwords:
            print("Password file cannot be empty!")
            exit(0)

        return passwords
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found!")
        exit(1)
    except IOError:
        print("Error: Unable to read the file!")
        exit(1)
