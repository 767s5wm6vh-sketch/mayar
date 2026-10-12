import random

def main():
    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
