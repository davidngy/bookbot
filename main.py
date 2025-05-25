from stats import count_words, get_book_text,count_characters, sort
import sys 


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text_content = get_book_text(path)
    num_words = count_words(text_content)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    ordered_dict = sort(count_characters(text_content))
    for pair in ordered_dict:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")
   
main()