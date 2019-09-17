#!/usr/bin/env python
import sys

dictionary_file_name = sys.argv[1]  # first argument - dictionary.txt
input_file_name = sys.argv[2]       # second argument - input.txt
log_file_name = sys.argv[3]         # third arugment - log file

sys.stdout = open(log_file_name,"a")
#read dictionary.txt and fill up dictionary list
print "Reading dictionary file"
dictionary = []
readDict = open(dictionary_file_name)
for readWords in readDict:
    readWords = readWords.strip()
    if len(readWords) <2 or len(readWords) >105:
        print "\n ERROR - Word length is out of scope. Not adding: ",readWords
        continue
    
    if readWords in dictionary:
        print "\n ERROR - Word - ",readWords," is already present in dictionary.",
    else:
        dictionary.append(readWords)
readDict.close()

#read input.txt and fill up inputText list
print "\n\n Reading input file"
inputText = []
readInputString = open(input_file_name)
for readText in readInputString:
    readText = readText.strip()
    inputText.append(readText)
readInputString.close()

# Build our dictionary using dictionary list filled earlier
word_groups = {}    # dictionary storing first and last character of dict words and the frequency of characters in between those letters
word_lengths = []   # length of every word in dictionary
freq = []           # frequency list - 26 characters - will be eventually appended to <word_groups> dictionary
i=0
wordsInDict = len(dictionary)

while i < wordsInDict:
    for words in dictionary:
        word_lengths.append(len(words))  # inserting length of words in word_lengths list
        word_groups[i] = [words[0], words[len(words)-1]] # building our initial dictionary - word_groups with first and last character of word
        freq = [0] * 26     #initialize to 0
        for ch in words:
            freq[ord(ch)-ord('a')] = freq[ord(ch)-ord('a')] + 1     # increment frequency by 1 for corresponding letters. [0]=a, [1]=b.. [26]=z
        word_groups[i].append(freq)     # append the freq list to <word_groups> dictionary
        i=i+1


# Time to read input file, line by line and compare every line with our dictionary
for counter in range(0,len(inputText)):
    inputLine = inputText[counter]  #reading line by line of input text stored in list
    totalCount=0
    answer=0
    input_groups = {}   # similar dict being created for our input txt. Will also be reinitialized when it's time to read a newline
    input_freq = []
    j=0
    for length in word_lengths:
        if length > len(inputLine):
            print "\nLength of dictionary word is more than the input string. Incorrect scenario!"
            j=j+1
            continue
    
        for k in range(0,len(inputLine)-length+1):
            input_groups[k] = [ inputLine[k], inputLine[k+length-1]]
            input_freq = [0]*26
            inputSubStr = inputLine[k:k+length]
            for ch in inputSubStr:
                input_freq[ord(ch)-ord('a')] = input_freq[ord(ch)-ord('a')]+1
            input_groups[k].append(input_freq)
            #compare one by one, words in dictionary against input string in the form of same length substrings
            #comparison is done by matching first and last letter of the word and the frequency of letters in between
            #break after first occurrence - no need to continue till EOL
            if word_groups[j] == input_groups[k]:
                answer = 1
                break
            else:
                answer = 0
        
        j=j+1   #increment to read the next word in our dictionary
        if answer == 1:
            totalCount = totalCount + 1

    print "Result - Case#",counter+1,":",totalCount

