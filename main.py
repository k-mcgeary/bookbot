import sys
from stats import get_num_words, character_count, sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_count = character_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
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