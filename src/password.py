import os
from pathlib import Path
from typing import List, Optional, Union

DATA_DIR = Path(os.getcwd()) / "data"
PASSWORD_PATH = DATA_DIR / "passwords.txt"


def ensure_data_directory() -> bool:
    """
    Ensure the data directory exists.

    Returns:
        True if directory exists or was created, False on error
    """
    try:
        if not DATA_DIR.exists():
            DATA_DIR.mkdir(parents=True)
            print(f"Created directory: {DATA_DIR}")
        return True
    except Exception as e:
        print(f"Error creating data directory: {e}")
        return False


def write_passwords(passwords: List[Union[bytes, str]]) -> bool:
    """
    Save a list of passwords to the local passwords file.

    Args:
        passwords: List of passwords as bytes or strings

    Returns:
        True if successful, False otherwise
    """
    if not ensure_data_directory():
        return False

    try:
        with open(PASSWORD_PATH, "w", encoding="utf-8") as file:
            count = 0
            for password in passwords:
                # Handle both string and bytes types
                try:
                    if isinstance(password, bytes):
                        line = password.decode("utf-8", errors="replace").strip()
                    else:
                        line = str(password).strip()

                    if line:  # Only write non-empty lines
                        file.write(f"{line}\n")
                        count += 1
                except Exception as e:
                    print(f"Warning: Skipped invalid password entry: {e}")

            print(f"Successfully saved {count} passwords to {PASSWORD_PATH}")
            return count > 0
    except PermissionError:
        print(f"Error: Permission denied when writing to '{PASSWORD_PATH}'")
        print("Try running with higher privileges or check file permissions.")
        return False
    except Exception as e:
        print(f"Error saving passwords: {e}")
        return False


def read_passwords() -> Optional[List[str]]:
    """
    Read passwords from the passwords file.

    Returns:
        List of passwords if successful, None otherwise
    """
    if not PASSWORD_PATH.exists():
        print(f"Error: Password file not found at '{PASSWORD_PATH}'")
        return None

    if PASSWORD_PATH.stat().st_size == 0:
        print("Error: Password file is empty")
        return None

    try:
        # Read file with error handling for encoding issues
        passwords = []
        with open(PASSWORD_PATH, "r", encoding="utf-8", errors="replace") as file:
            line_count = 0
            for line in file:
                line_count += 1
                stripped = line.strip()
                if stripped:
                    passwords.append(stripped)

        if not passwords:
            print("Error: No valid passwords found in file")
            return None

        return passwords

    except PermissionError:
        print(f"Error: Permission denied when accessing '{PASSWORD_PATH}'")
        print("Check file permissions or try running with higher privileges.")
        return None
    except UnicodeDecodeError:
        print("Error: File contains invalid characters - trying alternative encoding")
        # Fallback to Latin-1 encoding which can handle any byte sequence
        try:
            with open(PASSWORD_PATH, "r", encoding="latin-1") as file:
                passwords = [line.strip() for line in file if line.strip()]
            if passwords:
                return passwords
            return None
        except Exception as e:
            print(f"Error in fallback encoding: {e}")
            return None
    except Exception as e:
        print(f"Error reading password file: {e}")
        return None
