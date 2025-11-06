Password = "12345" 
maxattempts = 5

def main():
    attempts = 0
    while attempts < maxattempts:
        guess = input("Enter the password: ").strip()
        attempts += 1
        if guess == Password:
            print("Correct password! Access granted.")
            return
        else:
            remaining = maxattempts - attempts
            if remaining > 0:
                print(f"Incorrect password. You have {remaining} attempts remaining.")
            else:
                print("Maximum attempts reached. Access denied.")
if __name__ == "__main__":
    main()