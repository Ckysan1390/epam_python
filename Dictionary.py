class Dictionary:
    """
    A simple dictionary class to store and retrieve words and their descriptions.

    Attributes:
        dic: A dictionary to store words and their corresponding descriptions.

    Methods:
        new_entry(word, description): Adds a new word and its description to the dictionary.
        look(word): Searches the dictionary for a given word and prints its description if found.
    """

    def __init__(self):
        self.dic = {}

    def new_entry(self, word, desc):
        """
        Adds a new word and its description to the dictionary.

        Args:
            word: The word to be added.
            desc: The description of the word.
        """

        if word not in self.dic.keys():
            self.dic[word] = desc
            print(word + " was added to the dictionary!")
        else:
            print(word + " already on dictionary!")

    def look(self, word):
        """
        Searches the dictionary for a given word and prints its description if found.

        Args:
            word: The word to be searched.
        """

        print(self.dic.get(word)) if word in self.dic else print("Can't find entry for " + word + "!")


op = 0
dictionary = Dictionary()
while op != 3:
    try:
        op = int(input ("\n\nSelect one of options below:\n"
                        "1. Add word\n"
                        "2. Look word\n"
                        "3. Exit\n"))
        match op:
            case 1:
                has_space = True
                while has_space:
                    word = input("Name: ").lower()
                    if not " " in word:
                        has_space = False
                    else:
                        print("Please enter a single word")
                desc = input("Entry description: ")
                dictionary.new_entry(word, desc)

            case 2:
                word = input("Name: ").lower()
                dictionary.look(word) if len(dictionary.dic) > 0 else print("Dictionary is empty!")

            case 3:
                print("Bye...")

            case _:
                print("Please select an option between 1 - 3!")
    except ValueError:
        print("Please input a valid option between 1 - 3!")