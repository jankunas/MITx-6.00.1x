# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWordList = list(secretWord)
    newWord = len(secretWordList)*['_ ']
    for i in range(len(secretWordList)):
        if secretWordList[i] in lettersGuessed:
            newWord[i] = secretWordList[i]
    return ''.join(newWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = list(string.ascii_lowercase)
    for i in range(len(allLetters)):
        if allLetters[i] in lettersGuessed:
            allLetters[i] = ''
    return ''.join(allLetters)
    
    
def isLetterInSecretWord(letter, secretWord):
    '''
    letter: a letter that the user has enter
    secretWord: secret word that user has to guess
    returns: True if user's entered letter is in the secret word, False if it is not
    '''
    if letter in secretWord:
        return True
    else:
        return False        
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = list('')
    mistakesMade = 0
    line = '-' * 30
    print('I am thinking of a word that is %d letters long.' % len(secretWord))
    while True:
        print('You have %d guesses left' % (8 - mistakesMade))
        print('Available letters: ', getAvailableLetters(lettersGuessed))
        letter = (input('Please guess a letter: ')).lower()
        if isLetterInSecretWord(letter, secretWord) and letter not in lettersGuessed:
            lettersGuessed.append(letter)
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        elif letter in lettersGuessed:
            print("Ooops! You have already guessed this letter: ", getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(letter)
            mistakesMade += 1
            if mistakesMade == 8:
                print('You have lost')
                break   
        print(line)
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break                             
    

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
