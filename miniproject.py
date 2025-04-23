import random
advice_list = [
    "Believe in yourself and your abilities.",
    "Take small steps towards your goals every day.",
    "Practice gratitude and focus on the positive.",
    "Surround yourself with supportive people.",
    "Learn from your failures and keep moving forward.",
    "Take care of your physical and mental health.",
    "Set realistic expectations and prioritize self-care.",
    "Stay curious and keep learning new things.",
    "Be kind to others and show empathy.",
    "Celebrate your achievements and progress."
]

def get_random_advice():
    return random.choice(advice_list)

def main():
    print("Random Advice Generator")
    while True:
        print("\nOptions:")
        print("1. Get Random Advice")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nHere's your random advice:")
            print(get_random_advice())
        elif choice == "2":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
