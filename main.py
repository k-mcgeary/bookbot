from stats import get_num_words, character_count

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    char_count = character_count(text)
    print(f"{num_words} words found in the document")
    print(char_count)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()