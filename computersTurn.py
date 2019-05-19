import random
from letters import *

def getting_random_word_for_computer(letters, language):
    try:
        # Getting list of words
        if language == "icelandic":
            with open('./dictionary/icelandicWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split() 
        elif language == "danish":
            with open('./dictionary/danishWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split()
        else:
            with open('./dictionary/englishWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split()
            
    except FileNotFoundError:
        print('file not found')
    finally:
        possibleWords = []
        # Find possible words
        for word in words:
            # Valid word, until proofing guilty
            validWord = 1
            # Getting the random letters
            checker = list(letters)
            for x in word:
                if x in checker:
                    checker.remove(x)
                else:
                    validWord = 0
                    break
            if validWord == 1:
                # Filtering words, shorter than 5 letters
                possibleWords.append(word)
        # Choosing random word from list
        rand = ''
        for i in range(5):
            if rand:
                rand += ':'
            rand += random.choice(possibleWords) 
        return rand

def computers_turn(language):
    ##Computers turn
    # List of tuples with random letters and their corresponding value
    randLettersForComputer = get_rand_letters(language)
    # List of the random letters
    randLettersListForComputer = [i[0] for i in randLettersForComputer]
    # The random letters in a string
    randLettersString = (''.join(randLettersListForComputer)).lower()

    word = getting_random_word_for_computer(randLettersString, language)
    # Get value of word
    wordScore = score_of_word(word.replace(':', ''), language)
    return word, wordScore