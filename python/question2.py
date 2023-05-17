s = input("Enter a string: ")
s = "abcc"
char_frequency = {}

# Count the frequency of each character
for char in s:
    char_frequency[char] = char_frequency.get(char, 0) + 1

# Count the frequency of frequencies
freq_frequency = {}
for freq in char_frequency.values():
    freq_frequency[freq] = freq_frequency.get(freq, 0) + 1

# If all characters have the same frequency, it's valid
if len(freq_frequency) == 1:
    print("YES")
    exit()

# If there are exactly two different frequencies
if len(freq_frequency) == 2:
    freq1, count1 = freq_frequency.popitem()
    freq2, count2 = freq_frequency.popitem()

    # If one frequency occurs only once and its count is 1, it's valid
    if count1 == 1 and freq1 == 1:
        print("YES")
        exit()

    if count2 == 1 and freq2 == 1:
        print("YES")
        exit()

print("NO")
