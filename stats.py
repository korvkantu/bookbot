def get_word_count(path_to_file):
    word_count = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        split_words = file_contents.split()
        for split in split_words:
            word_count+=1
        return word_count

def get_char_count(path_to_file):
    char_dic = {}
    x = 0
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        chars = list(file_contents)
        for char in chars:
            if char in char_dic:
                x = char_dic[char]
                x+=1
                char_dic[char] = x
            else:
                char_dic[char] = 1
        return char_dic
def sort_on(item):
    return item["value"]

def sort_dic(char_dic):
    dic_list = [{"char": k, "value": v} for k, v in char_dic.items()]
    dic_list.sort( reverse=True, key=sort_on)
    return dic_list


def formatted_output(word_count, dic_list, book):

    output = f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    for item in dic_list:
        ch = item["char"]
        num = item["value"]
        if ch.isalpha():
            output += f"\n {ch}: {num}"

    output += "\n============= END ==============="

    return output
