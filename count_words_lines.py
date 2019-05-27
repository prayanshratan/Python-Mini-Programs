def countWords(fileName):
    numWords= 0
    numChars= 0
    numLines= 0

    with open(fileName, 'r') as file:
        for line in file:
            wordList= line.split()
            numLines += 1
            numWords += len(wordList)
            numChars += len(line)

    print("Words: ", numWords)
    print("Lines: ", numLines)
    print("Characters: ", numChars)

if __name__ == '__main__':
    countWords('/home/prayansh/Desktop/idea')