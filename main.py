from stats import get_word_count, get_char_count, sort_dic, formatted_output
import sys



def check_valid_cli_input():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    book = check_valid_cli_input()
    word_count = get_word_count(book)
    char_dic = get_char_count(book)
    sorted_list_of_dics = sort_dic(char_dic)
    formatted = formatted_output(word_count, sorted_list_of_dics, book)
    print(formatted)

if __name__ == "__main__":
    main()

