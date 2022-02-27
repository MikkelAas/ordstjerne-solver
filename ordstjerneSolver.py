"""
@author Mikkel Aas
@date 7/1/2022

Credit:
Word list from Norsk Ordbank
"""

import pandas as pd

# Constants
WORDS_PATH = "words.csv"
COLUMN_TAG_OPPSLAG = "OPPSLAG"

# Dictionary
fullformsliste = pd.read_csv(WORDS_PATH)


# ordstjerne_solver loops through every norwegian word that contains a certain letter and does not contain a list of letters
def ordstjerne_solver(letters_to_include, must_have_letter):
    result = []

    for i in range(len(fullformsliste[COLUMN_TAG_OPPSLAG])):
        word = str(fullformsliste[COLUMN_TAG_OPPSLAG][i]).lower()
        if (
            (len(word) >= 4)
            and (must_have_letter in word)
            and isInWord(letters_to_include, word)
        ):
            result.append(word)

    result = remove_duplicates(result)

    return result


# Removes duplicates from list
def remove_duplicates(x):
    return list(dict.fromkeys(x))


# Checks if a word only consist of a certain set of characters
def isInWord(char_list, string):
    matched_list = [characters in char_list for characters in string]
    string_contains_chars = all(matched_list)
    return string_contains_chars
