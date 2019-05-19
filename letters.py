import random

def get_rand_letters(language):
    randLettersList = []
    if language == "icelandic":
        # Letters in Ocelandic scrabble
        lettersList = (
            'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 
            'S', 'S', 'S', 'S', 'S', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'T', 'T', 
            'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'U', 'U', 'L', 'L', 'L', 'L', 'L', 'K', 'K', 'K', 'K', 'Ð', 'Ð', 
            'Ð', 'Ð', 'M', 'M', 'M', 'E', 'E', 'E', 'F', 'F', 'F', 'G', 'G', 'G', 'Ó', 'Ó', 'Á', 'Á', 'Æ', 'Æ', 'Í', 
            'U', 'H', 'V', 'O', 'Ý', 'D', 'P', 'B', 'J', 'Y', 'Ö', 'É', 'Þ', 'X')
    elif language == "dansih":
        # Letters in Danish scrabble
        letterlist = (
            'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'N', 'N', 'N', 'N', 'N', 
            'N', 'R', 'R', 'R', 'R', 'R', 'R', 'D', 'D', 'D', 'D', 'D', 'L', 'L', 'L', 'L', 'L', 'O', 'O', 'O', 'O', 
            'O', 'S', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'B', 'B', 'B', 'B', 'I', 'I', 'I', 'I', 'K', 'K', 
            'K', 'K', 'F', 'F', 'F', 'G', 'G', 'G', 'M', 'M', 'M', 'U', 'U', 'U', 'V', 'V', 'V', 'H', 'H', 'J', 'J', 
            'P', 'P', 'Y', 'Y', 'Æ', 'Æ', 'Ø', 'Ø', 'Å', 'Å', 'C', 'C', 'X', 'Z')
    else:
        # Letters in english scrabble
        lettersList = (
            'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
            'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'N', 'N', 'N', 'N',
            'N', 'N', 'R', 'R', 'R', 'R', 'R', 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'L', 'L', 'L', 'L', 'S', 'S', 'S',
            'S', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M', 'P', 'P', 'F',
            'F', 'H', 'H', 'V', 'V', 'W', 'W', 'Y', 'Y', 'K', 'J', 'X', 'Q', 'Z')

    # Getting random retters
    for i in range(10):
        # Get a random letter from lettersList
        randLetter = random.choice(list(lettersList))
        # Append a tuple of (random letter, score of letter) to the random Letters List
        randLettersList.append(tuple((randLetter, score_of_letter(randLetter, language))))
    # Return list of tuple
    return randLettersList

def score_of_letter(letter, language):
     # Score for icelandic scrabble
    if language == "icelandic":
        scores = {'A':'1', 'R':'1', 'S':'1', 'I':'1', 'N':'1', 'T':'2', 'U':'2', 'L':'2', 'K':'2', 'Ð':'2', 'M':'2', 
            'E':'3', 'F':'3', 'G':'3', 'Ó':'3', 'Á':'3', 'Æ':'4', 'Í':'4', 'Ú':'4', 'H':'4', 'V':'5', 'O':'5', 
            'Ý':'5', 'D':'5', 'P':'5', 'B':'5', 'J':'6', 'Y':'6', 'Ö':'6', 'É':'7', 'Þ':'7', 'X':'10'}
    elif language == "danish":
        scores = {'E': '1', 'A': '1', 'N': '1', 'R': '1', 'D': '2', 'L': '2', 'O': '2', 'S': '2', 'T': '2', 'B': '3', 
            'I': '3', 'K': '3', 'F': '3', 'G': '3', 'M': '3', 'U': '3', 'V': '3', 'H': '4', 'J': '4', 'P': '4', 
            'Y': '4', 'Æ': '4', 'Ø': '4', 'Å': '4', 'C': '8', 'X': '8', 'Z': '8'}
    # Score for english scrabble
    else:
        scores = {'A': '1', 'B': '3', 'C': '3', 'D': '2', 'E': '1', 'F': '4', 'G': '2', 'H': '4', 'I': '1', 'J': '8',
              'K': '5', 'L': '1', 'M': '3', 'N': '1', 'O': '1', 'P': '3', 'Q': '10', 'R': '1', 'S': '1', 'T': '1',
              'U': '1', 'V': '4', 'W': '4', 'X': '8', 'Y': '4', 'Z': '10'}

    # Dictionary with all the letters and their corresponding value
    return scores.get(letter)

def score_of_word(word, language):
    # Every letter in the word is evaluated in score_of_letter and the value is stored in a list
    # We then calculate the sum of that list and return it as a string
    return str(sum(int(score_of_letter(letter.upper(), language)) for letter in word))

# Check if a word is valid
def check_if_valid(word, language):
    words = []
    try:
        if language == "icelandic":
            # Get icelandic words
            with open('./dictionary/icelandicWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split() 
        elif language == "danish":
            # Get danish words
            with open('./dictionary/danishWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split() 
        else:
            # get english words
            with open('./dictionary/englishWords.txt', 'r', encoding='UTF-8') as f:
                words = f.read().split()
    except FileNotFoundError:
        print('words not found')
    finally:
        # Check if word is legit
        if word in words:
            return True
        else:
            return False


# Take string of letters, and returnig a tuple of word and it's score.
def string_to_tuple(letters, language):
    temp = []
    for i in letters:
        i = i.upper()
        temp.append(tuple((i, score_of_letter(i, language))))
    return temp

def ValidateWord(userWord, language, randLettersString):
    #EF það er búið að setja inn eitthvað orð
    if userWord and not check_if_valid(userWord.lower(), language):
        userWord = ''
    return userWord

