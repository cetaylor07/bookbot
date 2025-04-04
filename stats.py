def count_words(file_text):
    count = len(file_text.split())
    return count

def sort_on(char_dict):
    return char_dict["num"]

def char_count(file_text):
    text = file_text.lower()
    text_dict = {}

    for char in text:
        if char in text_dict:
            text_dict[char] += 1
        else:
            text_dict[char] = 1

    return text_dict

def dict_to_sorted_list(text_dict):
    sorted_list = []

    for char, num in text_dict.items():
        char_dict = {
            "char":char,
            "num":num
        }
        sorted_list.append(char_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
