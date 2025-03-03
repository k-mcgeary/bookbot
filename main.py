from stats import get_num_words, character_count, sort_dict

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    char_count = character_count(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    rejected_symbols = []

    for char in sort_dict(char_count):
        if char['char'].isalpha():
            print(f"{char['char']}: {char['count']}")
        else:
            rejected_symbols.append(f"{char['char']}:{char['count']}")

    print("============= END ===============")

    
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


main()