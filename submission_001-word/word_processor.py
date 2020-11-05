#import re
from string import ascii_lowercase
from functools import reduce

def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    '''
    import re
    text = "These are indeed interesting, an obvious understatement, times. What say you?"
    t_split = re.split(', | |;|?|.', text)
    print = t_split
    print(t_split)
    return "hello"
    pass
    
    for x in delimiters:
    words.append(
    '''
    # words = []
    delimiters = [',', '.', '?', ';',' ']

    words = split(delimiters, text)
    word = filter(lambda x:x!= '', words)
    word = [result.lower() for result in word]
    #map(lambda x:x.lower() , text)
    return word


def words_longer_than(length, text):
    l_text = convert_to_word_list(text)
    word = list(filter(lambda  x: len(x)>length, l_text))
    return word
    #pass


def words_lengths_map(text):
    text = convert_to_word_list(text)
    lengths = sorted(len(word) for word in text)
    result_dict = {}
    for i in lengths:
        result_dict[i] = len([word for word in text if len(word) == i])
    return result_dict
    #pass


def letters_count_map(text):
    text = convert_to_word_list(text)
    alpha = ascii_lowercase
    alpha_dict = {}
    for i in alpha:
        count = [word.count(i) for word in text]
        alpha_dict[i] = reduce(lambda x, y: x + y, count, 0)
    return alpha_dict
    #pass


def most_used_character(text):
    count = letters_count_map(text)
        # all_values = count.values()
        # char = max(all_values)
    char = max(count, key = count.get)
    if text == '':
        return None
    else:
        return char
    #pass

def run_word_proc():
    words = "These are indeed interesting, an obvious understatement, times. What say you?"
    #word = words.lower()
    print(convert_to_word_list(words))
    print(words_longer_than(5,words))
    print(words_lengths_map(words))
    print(letters_count_map(words))
    print(most_used_character(words))

if __name__ == "__main__":
    run_word_proc()