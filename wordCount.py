import sys  # command line arguments

# Get inputs from command line
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

# Dictionary to store words
wordCount = {}

# Open input file to read
with open(inputFileName, 'r') as inputFile:
    text = inputFile.read()
    wordList = text.split()

# Remove any punctuations or white space and make it lowercase
    for word in wordList:
        lowerCaseList = word.lower().replace(".","").replace("\"","").replace(",","").replace(";","").replace(":","")
# Check for words with "-"
        compoundWord = lowerCaseList.split("-")
        if not len(compoundWord) > 1:
            compoundWord = lowerCaseList.split("'")
# Go through lowercase list and check if its in dictionary, keep count of how many times word appears
        for lowerCaseList in compoundWord:
            if lowerCaseList in wordCount:
                wordCount[lowerCaseList] += 1
            else:
                wordCount.setdefault(lowerCaseList,1)
# Sort words in order
sortedWords = sorted(wordCount)

# Open file to write the output
with open(outputFileName, 'w') as outputFile:
    for word in sortedWords:
        if word.isalpha():
            outputFile.write(word + " %s\n" % wordCount[word])
