# Author: SCT (AMDG) 3/23/22

# check if word contains forbidden letters

def avoid(word,string):
    # entered string/letters into list
    li = list(string)
    for x in word:
        if x in li:
            return False
            # if contains forbidden letters return False
    
    return True

words = open("words.txt")

word = words.readlines()
num = 0
forb_w = input("Enter the forbidden letters: ")
# interates file to check if word contains letter if not + 1
for y in word:
    y = y.strip()
    if avoid(y,forb_w) == True:
        num += 1

print("There are {0} words that don't contain the forbidden letters.".format(num))

# closes file
words.close()