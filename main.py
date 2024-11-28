with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    word_count = len(file_contents.split())
    letter_count = {}
    for letter in file_contents:
        lower_letter = letter.lower()
        if lower_letter.isalpha():
            if lower_letter in letter_count:
                letter_count[lower_letter] += 1
            else:
                letter_count[lower_letter] = 1
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Word count: {word_count}")
    sorted_letter_count = dict(sorted(letter_count.items()))
    least_common_letter = min(sorted_letter_count, key=sorted_letter_count.get)
    most_common_letter = max(sorted_letter_count, key=sorted_letter_count.get)
    for letter, count in sorted_letter_count.items():
        print(f"The '{letter}' character was found {count} times.")
    
    print("-------------------------------------------------")
    print(f"The least common letter is '{least_common_letter}' and was found {sorted_letter_count[least_common_letter]} times.")
    print(f"The most common letter is '{most_common_letter}' and was found {sorted_letter_count[most_common_letter]} times.")
    print("-------------------------------------------------")
    
    print("--- End report of books/frankenstein.txt ---")