from stats import count_words,char_count, dict_to_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = sys.argv[-1]
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    file_text = get_book_text(path)
    word_count = count_words(file_text)
    text_dict = char_count(file_text)
    sorted_list = dict_to_sorted_list(text_dict)
    print( f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()