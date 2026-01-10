import sys
from stats import count_words
from stats import count_chars
from stats import make_dict_of_chars
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return 1
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        text = get_book_text(sys.argv[1])
        num_words = count_words(text)
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        char_stats = count_chars(text)
        print("--------- Character Count -------")
        char_dict = make_dict_of_chars(char_stats)
        for item in char_dict:
            print(f"{item['char']}" + ": " + f"{item['num']}")
        return 0

main()
