# Author: SCT (AMDG) 3/16/22

# open the file and creates "file.txt"
words = open("words.txt")
file = open("file.txt","a")

word = words.readlines()
for x in word:
# Interate through the words list 

    if len(x.strip()) > 20: # remove the escape characters and checks if the word is > 20
        file.write(x)

# closes files
words.close()
file.close()