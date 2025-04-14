def get_num_words(file_contents):
  word_count = len(file_contents.split())
  letter_count = {}
  for letter in file_contents:
      lower_letter = letter.lower()
      if lower_letter.isalpha():
          if lower_letter in letter_count:
              letter_count[lower_letter] += 1
          else:
              letter_count[lower_letter] = 1

  return word_count, letter_count