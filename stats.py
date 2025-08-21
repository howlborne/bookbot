def number_of_words(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def count_characters(file_path):

    new_char_dict = {}

    with open(file_path, encoding="utf-8") as f:
        content = f.read()
        low_case = content.lower()
        for char in low_case:
            if char not in new_char_dict:
                new_char_dict[char] = 1
            elif char in new_char_dict:
                new_char_dict[char] += 1
    return new_char_dict


def book_report(file_path):
    chars_dict = count_characters(file_path)
    chars_dict_pair_list = []
    for char in chars_dict:
        chars_dict_pair_list.append({char: chars_dict[char]})

    report_list = []
    for pair in chars_dict_pair_list:
        for key in pair:
            if key.isalpha() == True:
                report_list.append({"char": key, "num": pair[key]})


    report_list.sort(reverse=True, key=lambda x: x["num"])

    return report_list



