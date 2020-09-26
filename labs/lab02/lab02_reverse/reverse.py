def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is
    reversed

    For example,
    >>> reverse_words(["Hello World", "I am here"])
    ['World Hello', 'here am I']
    '''

    new_list = []
    for string in string_list:
        words = string.split()
        words.reverse()
        string = ' '.join(words)
        new_list.append(string)

    return new_list


