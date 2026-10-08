
"""
Program: Word Count Analyzer
Author: Mariam Shatta
Purpose: Read a text file and count how often each word appears.
Starter Code: None
Date: October 8, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            self.__frequencies = {}
            table = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(table)

                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def print_report(self):
        sorted_words = sorted(self.__frequencies.keys())

        print("\n--- Word Count Report ---")

        for word in sorted_words:
            print(f"{word:<20} :: {self.__frequencies[word]}")

def main():
    folder = Path(__file__).parent

    files = {
        "1": folder / "princess_mars.txt",
        "2": folder / "Tarzan.txt",
        "3": folder / "treasure_island.txt",
        "4": folder / "monte_cristo.txt"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. The Count of Monte Cristo")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        elif choice in files:
            filename = files[choice]
            print(f"\nProcessing '{filename.name}'...")

            analyzer = WordAnalyzer(str(filename))

            if analyzer.process_file():
                analyzer.print_report()

        else:
            print("Invalid choice. Please select from 1-5.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
