from stats import get_num_words
import sys

if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1])

    with open(sys.argv[1]) as f:
        file_contents = f.read()

        word_count, letter_count = get_num_words(file_contents)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Word count: {word_count}")
        sorted_letter_count = dict(sorted(letter_count.items()))
        least_common_letter = min(sorted_letter_count, key=sorted_letter_count.get)
        most_common_letter = max(sorted_letter_count, key=sorted_letter_count.get)
        for letter, count in sorted_letter_count.items():
            print(f"{letter}: {count}")
        
        print("-------------------------------------------------")
        print(f"The least common letter is '{least_common_letter}' and was found {sorted_letter_count[least_common_letter]} times.")
        print(f"The most common letter is '{most_common_letter}' and was found {sorted_letter_count[most_common_letter]} times.")
        print("-------------------------------------------------")
        
        print("--- End report of books/frankenstein.txt ---")
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

