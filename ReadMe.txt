

# Scrambled Words
Count how many of the words from a dictionary appear as substrings in a long string of characters either in their original form or in their scrambled form. The scrambled form of the dictionary word must adhere to the following rule: the first and last letter must be maintained while the middle characters can be reorganised.



#Prerequisites

1. Place both input files on desktop. 
2. Change "username" to respective username for your machine
3. Pick path directory based on Windows/Mac OS
Total 3 files to be passed as arguments in the order given below:

For Windows 

[PATH TO DICTIONARY FILE] = 'C:/Users/username/Desktop/dictionary.txt'
[PATH TO INPUT FILE] = 'C:/Users/username/Desktop/input.txt'
[PATH FOR LOG OUTPUT] = 'C:/Users/username/Desktop/scrmabled_output.txt'


For Mac OS

[PATH TO DICTIONARY FILE] = '/Users/username/Desktop/dictionary.txt'
[PATH TO INPUT FILE] = '/Users/username/Desktop/input.txt'
[PATH FOR LOG OUTPUT] = '/Users/username/Desktop/scrmabled_output.txt'


#Build executable 

For Windows
Step 1: Add Python to Windows Path
Step 2: Open the Windows Command Prompt
Step 3: Install the Pyinstaller Package
Step 4: Download scrmabled-strings.py from the below URL and place it on your desktop
	https://github.com/harkiratlota/DemoCode
Step 5: Create the executable using Pyinstaller
	* Open CMD and navigate to desktop as current directory
	* Execute:
		pyinstaller --onefile scrmabled-strings.py
	* An executable should be created at your desktop location



# Test Example

Dictionary File
     axpaj
     apxaj
     dnrbt
     pjxdn
     abd

Input File (1 search line example)
aapxjdnrbtvldptfzbbdbbzxtndrvjblnzjfpvhdhhpxjdnrbt

Program Output
Case #1: 4


Dictionary File
     axpaj
     apxaj
     dnrbt
     pjxdn
     c
     ed
     dnrbt
     abd
     apxa
     bbc
     pwe
     wcpowl
     loobbc
     owlllwoo

Input File (2 search lines example)
aapxjapxajaaxpjapaxjjapxajaaxpjpxaa
terqncodqwqwewirhiasdasqweqwdksoakdoapskdsaodkasdbbc

Program Output 
Case #1: 3 (axpaj, apxaj, apxa)
Case #2: 1 (abc)

