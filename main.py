import sys
from stats import number_of_words
from stats import count_characters
from stats import book_report 


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) > 1:
        file_path = sys.argv[1]
        words_list = number_of_words(file_path)
        words_count = words_list.split()
    
        sorted_report = book_report(file_path)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {len(words_count)} total words")
        print("--------- Character Count -------")

        for char in sorted_report:
            print(f"{char["char"]}: {char["num"]}")
    
        print("============= END ===============")


main()


