def capture_words():
    """
    Reads n words from user input and stores them in an array.

    Returns:
    An array with whe captured words.
    """

    words = []
    word = " "
    print("Input n words to create a new one from them, empty to finish...")
    while word != "":
        word = input("Word #" + str(len(words) + 1) + " ").replace(" ","")
        if len(word) >= len(words) + 1:
            words.append(word) if word != "" else print("Creating word...")
        elif len(word) == 0:
            print("Creating new word...")
            break
        else:
            print("Please input a word with at least " + str(len(words) + 1) + " letters...")
    return words

def create_word(words):
    """
    Iterate through the input array, selecting the letter at the index corresponding to the current word's position. Concatenate these letters to form a new word

    Parameters:
    words: An array containing the words entered by the user.

    Returns:
    A string representing the newly formed word.
    """

    new_word = ""
    for word in words:
        new_word += word[words.index(word)]
    return new_word

print(create_word(capture_words()))