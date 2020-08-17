"""
The six most commonly used letters in the English language can be remembered with
the mnemonic “etaoin”. Write a Python script that takes a
sentence (string) as input and returns a simple bar chart–type display
"""


def alphabet_bar_chart(sentence: str):
    """
    The function creates an alphabet bar chart from a sentence.
    Parameters
    ----------
    sentence: str
        A sentence.
    Returns
    -------
    Dictionary
        A dictionary of lists, with alphabets as keys.
    """
    sentence = sentence.lower()
    dictionary = {}
    for letter in sorted(list(sentence)):
        if letter.isalpha():
            if letter in dictionary:
                dictionary[letter].append(letter)
            else:
                dictionary[letter] = [letter]
    return dictionary


if __name__ == "__main__":
    SEN = """
    The six most commonly used letters in the English language can be remembered with the mnemonic “etaoin”.
    """
    print(alphabet_bar_chart(SEN))
