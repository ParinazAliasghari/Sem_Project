import os

def get_version():
    """Read the current version from the VERSION file."""
    with open("VERSION", "r") as file:
        return file.read().strip()

def main():
    print(f"Welcome to Sem_Project v{get_version()}!")

if __name__ == "__main__":
    main()
