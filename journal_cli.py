import json
import os
from datetime import datetime


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Initialize JSON file if it doesn't exist
if not os.path.exists("journal.json"):
    with open("journal.json", "w") as f:
        json.dump({}, f)

# Function to add a journal entry


def add_entry():
    clear_console()

    with open("journal.json", "r") as f:
        entries = json.load(f)

    date = str(datetime.now().date())
    text = input("What's on your mind today? ")
    mood = input("On a scale of 1-10, how do you feel today? ")
    tags = input("Enter any tags separated by commas: ").split(",")

    if date in entries:
        entries[date]['text'] += "\n" + text
        entries[date]['mood'].append(mood)
        entries[date]['tags'].extend(tags)
    else:
        entries[date] = {'text': text, 'mood': [mood], 'tags': tags}

    with open("journal.json", "w") as f:
        json.dump(entries, f)

    print("\nEntry added successfully! 😊")

# Function to view entries


def view_entries():
    clear_console()

    with open("journal.json", "r") as f:
        entries = json.load(f)

    print("---- Journal Entries ----\n")
    for date, entry in entries.items():
        print(
            f"{date}: {entry['text']} \n(Mood: {entry['mood']}, Tags: {entry['tags']})")
        print("-------------------------")


if __name__ == "__main__":
    while True:
        clear_console()
        print("---- Journal Menu ----")
        print("1: Add a new entry")
        print("2: View entries")
        print("3: Quit")
        print("----------------------")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again.")

        input("\nPress Enter to continue...")
