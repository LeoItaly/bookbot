from stats import get_number_of_words, get_character_count, sort_character_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = get_number_of_words(text)
    char_count = get_character_count(text)
    print(f'Found {num_words} total words')
    sort_character_count(char_count)
    

main()