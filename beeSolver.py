import time

# reads in word library as a set
with open("wordslist.txt") as word_list:
    words = set(word.strip().lower() for word in word_list)

letters = set()

def beeSolver(word_list, other_letters, center):
  intermediates = set()
  final_words = set()

  # for loop checks that a word is possible and is at least 4 letters long
  start = time.time()
  for word in word_list:
    word_as_set = set(word)
    if word_as_set - other_letters == set() and len(word) >= 5:
      intermediates.add(word)

  # for loop checks for center letter
  for word in intermediates:
    inter_as_set = set(word)
    if center in inter_as_set:
      final_words.add(word)

  end = time.time()
  results = ', '.join(final_words)

  print()
  print("Showing " + str(len(final_words)) + " possible words in " + str(end-start) + " seconds.")
  print()
  print(results)

print()
print("So... you want to cheat. You want to start down that slippery slope.")
print("Very well, if you REALLY wish to continue, enter your letters below as prompted:")

print()
center_letter = input("Center Letter: ")
letters.add(center_letter)
letters.add(input("1st Letter: "))
letters.add(input("2nd Letter: "))
letters.add(input("3rd Letter: "))
letters.add(input("4th Letter: "))
letters.add(input("5th Letter: "))
letters.add(input("6th Letter: "))

beeSolver(words, letters, center_letter)
