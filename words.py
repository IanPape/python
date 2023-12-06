
def print_upper_words(words):
    """ takes a list of words and prints them all out in uppercase"""
    for word in words:
            if word.lower().startswith('h') or word.lower().startswith('y'):
                 print(word.upper())



