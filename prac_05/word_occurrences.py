"""
Word Occurrences
Estimate: 30 minutes
Actual: 47 minutes
"""


def main():
    """Get text from user input and print text."""
    text = input("Enter text: ").lower()
    print(f"Text: {text}")
    words = text.split()
    word_to_count = count_word_occurrences(words)
    print_word_counts(word_to_count)


def count_word_occurrences(words):
    """Count the number of times a word appears in the text."""
    word_to_count = {}
    for word in words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    return word_to_count


def print_word_counts(word_to_count):
    """Sort words and print the word counts aligned to the longest word."""
    sorted_words = sorted(word_to_count)
    max_length = max(len(word) for word in sorted_words)
    for word in sorted_words:
        print(f"{word:<{max_length}} : {word_to_count[word]}")


main()
