import time
import json
import os

# File to save pet data
SAVE_FILE = "pet_data.json"

# Load pet data from file
def load_pet():
    try:
        with open(SAVE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# Save pet data to file
def save_pet(pet):
    with open(SAVE_FILE, "w") as file:
        json.dump(pet, file, indent=4)

# Create a new pet
def create_pet():
    print("Let's create your virtual pet!")
    name = input("Enter your pet's name: ").strip().capitalize()
    pet_type = input("What kind of pet is it (e.g., dog, cat, bird)? ").strip().capitalize()

    pet = {
        "name": name,
        "type": pet_type,
        "hunger": 50,
        "happiness": 50,
        "health": 50,
        "energy": 50
    }
    save_pet(pet)
    print(f"\n{name} the {pet_type} has been created!")
    return pet

# Display pet stats
def show_stats(pet):
    print(f"\n{pet['name']}'s Stats:")
    print(f"  Hunger: {pet['hunger']} / 100")
    print(f"  Happiness: {pet['happiness']} / 100")
    print(f"  Health: {pet['health']} / 100")
    print(f"  Energy: {pet['energy']} / 100")

# Interact with the pet
def feed_pet(pet):
    print(f"\nYou feed {pet['name']}.")
    pet["hunger"] = min(100, pet["hunger"] + 20)
    pet["health"] = min(100, pet["health"] + 5)
    save_pet(pet)

def play_with_pet(pet):
    if pet["energy"] < 20:
        print(f"\n{pet['name']} is too tired to play!")
        return
    print(f"\nYou play with {pet['name']}.")
    pet["happiness"] = min(100, pet["happiness"] + 20)
    pet["energy"] = max(0, pet["energy"] - 15)
    save_pet(pet)

def rest_pet(pet):
    print(f"\n{pet['name']} takes a nap.")
    pet["energy"] = min(100, pet["energy"] + 30)
    save_pet(pet)

# Dynamic changes over time
def decrease_stats(pet):
    pet["hunger"] = max(0, pet["hunger"] - 5)
    pet["happiness"] = max(0, pet["happiness"] - 5)
    pet["health"] = max(0, pet["health"] - (10 if pet["hunger"] == 0 else 0))
    pet["energy"] = max(0, pet["energy"] - 5)

# Main game loop
def main():
    pet = load_pet()
    if not pet:
        pet = create_pet()

    print("\nWelcome to the Virtual Pet Simulator!")
    while True:
        show_stats(pet)
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Let your pet rest")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            feed_pet(pet)
        elif choice == "2":
            play_with_pet(pet)
        elif choice == "3":
            rest_pet(pet)
        elif choice == "4":
            print(f"\nGoodbye! Don't forget to take care of {pet['name']}!")
            break
        else:
            print("\nInvalid choice! Please try again.")

        decrease_stats(pet)
        save_pet(pet)
        time.sleep(1)  # Simulate time passing

        if pet["health"] <= 0:
            print(f"\nOh no! {pet['name']} has passed away due to neglect. 😢")
            os.remove(SAVE_FILE)  # Delete save file to start fresh
            break

if __name__ == "__main__":
    main()
