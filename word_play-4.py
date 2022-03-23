# Author: SCT (AMDG) 3/23/22


# function to check if letters are in word list
def uses_only(word,letters):
    l = list(letters)
    w = list(word)
    for x in letters:
        if x not in w:
            return False # return false of isnt in list
    
    return True

# opens file
words = open("words.txt")

# reads file
word = words.readlines()
num = 0
u_w = input("Enter the uses only letters: ")
# num tracks number of words with use only letters
for y in word:
    y = y.strip()
    if uses_only(y,u_w) == True:
        num += 1 # adds 1 if has use only letter

print("There are {0} words contain the use only letters.".format(num))
 # closes file
words.close()