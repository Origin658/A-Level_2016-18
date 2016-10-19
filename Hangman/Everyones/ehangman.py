""" Hangman Game (v1.0)
    Name: 
    Date: 
    """

# imported modules go here

def load_file(filename):
    """ Function to return a word list from a plain text file;
        Note: You will need to open the file, read and append
        each line to an array (or list), close the file and
        then return the array.
        """
##    word_list = []
##
##    file = open(filename, "r")
##    temp = file.readlines()
##
##    for item in temp:
##        word_list.append(item.replace("\n", "").lower())
##
##    file.close()
##    
##    print(word_list)
##    return word_list

    word_list = []

    with open(filename, "r") as file:
        temp = file.readlines()

        for item in temp:
            word_list.append(item.replace("\n", "").lower())

    print(word_list)
    return word_list


def select_word(word_list):
    """ Function to return a random word from an array of words;
        Note: You will need to import the random module and use
        random.randint() to select a random index in the array.
        """
    # your code goes here
    return word

def find_character(char, word):
    """ Function to return the position(s) of a character in word;
        Note: This should return the index of the character as an integer,
        if the character is not found, it should return a value of -1
        """
    # your code goes here
    return char_pos

# do you need any other functions or procedures?

def main():
    """ Note: This is your main function and should contain your game loop.
        """
    filename = "word_list.txt"
    attempts_remaining = 10
    # do you need any other variables?

    word_list = load_file(filename)
##    word = select_word(word_list)
    
    # your code goes here


if __name__ == "__main__":
    main()
