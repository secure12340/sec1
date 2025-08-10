def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found!"

filename = input("Enter text file name (e.g., sample.txt): ")
word_count = count_words(filename)
print(f"Word count: {word_count}")