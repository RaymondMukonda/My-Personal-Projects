import random
playing = True


while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("thank you for playing!")
        break
    else:
        print("Invalid choice")