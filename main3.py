import random

def truth_and_lies():
    print("\n Welcome to the Truth and Lies Game!")
    print("You meet three people: Alice, Bob, and Charlie.")
    print("Each of them either ALWAYS tells the truth or ALWAYS lies.")
    print("Your goal is to find out who tells the truth.\n")
    
    characters = {
        "Alice": random.choice(["truth", "lie"]),
        "Bob": random.choice(["truth", "lie"]),
        "Charlie": random.choice(["truth", "lie"])
    }
    while True:
        question = input("Ask a yes/no question (or type 'quit' to stop): ").strip().lower()
        if question == "quit":
            break

        print("\n--- Answers ---")
        for name, nature in characters.items():
            if "truth" in question:
                answer = "yes" if nature == "truth" else "no"
            elif "lie" in question:
                answer = "no" if nature == "truth" else "yes"
            else:
                answer = random.choice(["yes", "no"])
            print(f"{name} says: {answer.upper()}")
            
    guess = input("Who do you think always tells the truth? (Alice/Bob/Charlie): ").capitalize()
    
    print("\n Truth Revealed!")
    
    for name, nature in characters.items():
        print(f"{name}: {nature.upper()}")
        
    if guess in characters and characters[guess] == "truth":
        print("\n You guessed correctly! Well done!")
        
    else:
        print("\n Wrong guess! Better luck next time.")
        
truth_and_lies()

