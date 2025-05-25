def get_book_text(path):
    with open(path) as input:
        file_contents = input.read()
    return file_contents
    
def count_words(text_input):
    words = text_input.split()
    result = 0
    for count in range(0, len(words) + 1):
       result = count
    
    return result

def count_characters(text_input):
    book_content = text_input.lower()
    char_count = {}

    for char in book_content:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
 
    return char_count

def sort_on(unsorted_dic):
    return unsorted_dic["num"]

def sort(unsorted_dic):
    list_format = []
    
    for char_count in unsorted_dic:
        #print(char_count) key alphabet
        #print(unsorted_dic[char_count]) actual values
        list_format.append({"char": char_count, "num": unsorted_dic[char_count]})
        
    list_format.sort(reverse=True, key=sort_on)

    return list_format