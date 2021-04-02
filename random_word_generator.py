# Description: This file generates "random" words using the random library. Chances of somebody generating a real,
#              random English word are probably infinitesimal.

import random

upper_letter_dict = {1: "A",
                     2: "B",
                     3: "C",
                     4: "D",
                     5: "E",
                     6: "F",
                     7: "G",
                     8: "H",
                     9: "I",
                     10: "J",
                     11: "K",
                     12: "L",
                     13: "M",
                     14: "N",
                     15: "O",
                     16: "P",
                     17: "Q",
                     18: "R",
                     19: "S",
                     20: "T",
                     21: "U",
                     22: "V",
                     23: "W",
                     24: "X",
                     25: "Y",
                     26: "Z"
                     }

lower_letter_dict = {}

counter = 1
for letters in upper_letter_dict:
    lower_letter_dict[counter] = upper_letter_dict[letters].lower()
    counter += 1


def make_random_word():
    word_length = random.randint(4, 10)
    word_string = str(upper_letter_dict[random.randint(1, 26)])
    word_length -= 1

    for letter_intervals in range(0, word_length):
        word_string = word_string + str(lower_letter_dict[random.randint(1, 26)])

    return word_string


def main():
    words = []
    for word_intervals in range(0, 10000):
        words.append(make_random_word())
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
