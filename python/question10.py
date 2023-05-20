import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def count_pos_tags(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Perform part-of-speech tagging
    tagged_words = pos_tag(words)
    
    # Initialize counts
    verb_count = 0
    noun_count = 0
    pronoun_count = 0
    adjective_count = 0
    
    # Count the number of verbs, nouns, pronouns, and adjectives
    for word, tag in tagged_words:
        if tag.startswith('VB'):
            verb_count += 1
        elif tag.startswith('NN'):
            noun_count += 1
        elif tag.startswith('PRP'):
            pronoun_count += 1
        elif tag.startswith('JJ'):
            adjective_count += 1
    
    # Create a dictionary with the counts
    pos_counts = {
        'Verbs': verb_count,
        'Nouns': noun_count,
        'Pronouns': pronoun_count,
        'Adjectives': adjective_count
    }
    
    return pos_counts

# Test case 1
text1 = "The cat is sleeping on the mat."
pos_counts1 = count_pos_tags(text1)
print("Test Case 1 - Text:", text1)
print("POS Counts:", pos_counts1)

# Test case 2
text2 = "I love eating delicious food."
pos_counts2 = count_pos_tags(text2)
print("Test Case 2 - Text:", text2)
print("POS Counts:", pos_counts2)

# Additional Test Case 1
text3 = "She runs fast and jumps high."
pos_counts3 = count_pos_tags(text3)
print("Additional Test Case 1 - Text:", text3)
print("POS Counts:", pos_counts3)

# Additional Test Case 2
text4 = "The big brown dog barked loudly."
pos_counts4 = count_pos_tags(text4)
print("Additional Test Case 2 - Text:", text4)
print("POS Counts:", pos_counts4)
