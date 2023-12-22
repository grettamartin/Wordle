import random 
from colorama import Fore, Back, Style # this is for the colored text

# saller file
inputFile = open('WordleCSVFile2.csv', 'r')
fileDataString = inputFile.read()
smallList = fileDataString.split('\n')
# print(smallList)
inputFile.close()

# bigger file
inputFile = open('validWordsCSVFile.csv', 'r')
fileDataString = inputFile.read()
bigList = fileDataString.split('\n')
inputFile.close()

correctWord = (random.choice(smallList)) # chooses a random word from a smaler list of more common five letter words 

# this tells us the correct word for trial runs
for idx in range(len(correctWord)):
    print(correctWord[idx])
    
# parallel lists that will help us determine what color to make each letter    
letterIndex = []
wordLetters = []

guessCount = 0
numGuesses = int(input('Enter how many times you want to guess (up to 10): '))
    
while numGuesses >= 10 or numGuesses <= 0:  # this determines if the number of guesses is valid
    print('Invalid number of guesses. Please try again.')
    numGuesses = int(input('Enter how many times you want to play (up to 10): '))


wordGuessed = input('Enter a valid five letter word! ')
wordGuessed = wordGuessed.lower()
while numGuesses != guessCount and wordGuessed != correctWord:
    if wordGuessed not in bigList: # if it's a valid English word
        print('Word not in word list. Please try again.')
    if wordGuessed != correctWord and wordGuessed in bigList:
        print('Incorrect. Guess again.')
        for idx in range(len(wordGuessed)):
            if wordGuessed[idx] in correctWord:
                if correctWord[idx] == wordGuessed[idx]:
                    letterIndex.append(1)
                else:
                    letterIndex.append(2)
            else:
                letterIndex.append(0)
            wordLetters.append(wordGuessed[idx])
            if letterIndex[idx] == 1:
                print(Back.GREEN, wordLetters[idx], Style.RESET_ALL, end='')
            if letterIndex[idx] == 2:
                print(Back.YELLOW, wordLetters[idx], Style.RESET_ALL, end='')
            if letterIndex[idx] == 0:
                print(Back.WHITE, wordLetters[idx], Style.RESET_ALL, end='')
        print()
        guessCount += 1
    if numGuesses != guessCount:
        wordGuessed = input('Enter a valid five letter word! ')
        wordGuessed = wordGuessed.lower()
#     print("letterIndex:" + str(letterIndex))
#     print(wordLetters)
    letterIndex = []
    wordLetters.clear()

#     wordGuessed = input('Enter a valid five letter word! ')


if wordGuessed == correctWord:
    for idx in range(len(wordGuessed)):
        print(Back.GREEN, wordGuessed[idx], Style.RESET_ALL, end='')
    if guessCount > 0:
        print('\nYou win! You guessed the word in {} tries.'.format(guessCount + 1))
    else:
        print('\nYou win! You guessed the word in {} try.'.format(guessCount + 1))
else:
    print('You lost! The correct word is {}.'.format(correctWord))
    
 
    

