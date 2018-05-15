import re

from data import DICTIONARY, LETTER_SCORES


def load_words() -> list:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as f:
        return [re.sub("\n", "", i) for i in f.readlines()]


def calc_word_value(word: str):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = 0
    for char in word.upper():
        value += LETTER_SCORES.get(char, 0)
    return value


def max_word_value(arg=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if arg == DICTIONARY:
        words = load_words()
        max_value = max(([calc_word_value(i) for i in words]))
        zipped_data = dict(zip([calc_word_value(i) for i in words], words))
    else:
        max_value = max([calc_word_value(i) for i in arg])
        zipped_data = dict(zip([calc_word_value(i) for i in arg], arg))

    return zipped_data.get(max_value)


if __name__ == "__main__":
    print(max_word_value())
