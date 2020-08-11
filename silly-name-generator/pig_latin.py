"""
To form Pig Latin, you take an English word that begins with a consonant, move that
consonant to the end, and then add “ay” to the end of the word. If the word begins with
a vowel, you simply add “way” to the end of the word. One of the most famous Pig Latin
phrases of all time is “ixnay on the ottenray,” uttered by Marty Feldman in Mel Brooks’s
comedic masterpiece Young Frankenstein.
"""

VOWEL_LIST = ['a', 'e', 'i', 'o', 'u']


def pig_latin(word: str):
    i = 0
    for letter in list(word):
        if letter in VOWEL_LIST:
            if i == 0:
                return word + "way"
            else:
                return word[i:] + word[:i] + "ay"
        else:
            i += 1


if __name__ == '__main__':
    print(pig_latin("throw"))