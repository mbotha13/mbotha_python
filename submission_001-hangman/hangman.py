#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    words = open(file_name, "r").readlines()
    return (words)


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word = random.randint(0, len(words))
    Hang = words[word]
    alpha = random.randint(0, len(Hang) - 2)
    Man = Hang[alpha]
    rep = Hang.replace(Man, "_", 1)
    print("Guess the word:", rep)
    return Hang



def get_user_input():
    Hang_man = input("Guess the missing letter: ")

    """
    TODO: Step 3 - get user input for answer
    """
    return Hang_man


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

