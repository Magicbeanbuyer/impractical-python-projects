"""
The six most commonly used letters in the English language can be remembered with
the mnemonic “etaoin”. Write a Python script that takes a
sentence (string) as input and returns a simple bar chart–type display
"""


def alphabet_bar_chart(sentence: str):
    sentence = sentence.lower()
    dict = {}
    for letter in sorted(list(sentence)):
        if letter.isalpha():
            if letter in dict:
                dict[letter].append(letter)
            else:
                dict[letter] = [letter]
    return dict


if __name__ == "__main__":
    sentence = """
    The six most commonly used letters in the English language can be remembered with the mnemonic “etaoin”.
    """
    print(alphabet_bar_chart(sentence))