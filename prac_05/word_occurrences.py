"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

def main():
    word_to_count = {}

    text = input("Enter text: ").lower()
    print(f"Text: {text}")

    words = text.split()

    for word in words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1

    max_length = max(len(word) for word in word_to_count)

    for word in word_to_count:
        print(f"{word:<{max_length}} : {word_to_count[word]}")

main()
