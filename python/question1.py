input_string = input("Enter a string: ")
word_frequency = {}
words = input_string.split()

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

max_frequency = max(word_frequency.values())
highest_frequency_word_length = 0

for word, frequency in word_frequency.items():
    if frequency == max_frequency:
        highest_frequency_word_length = max(highest_frequency_word_length, len(word))

print("Length of the highest-frequency word:", highest_frequency_word_length)
