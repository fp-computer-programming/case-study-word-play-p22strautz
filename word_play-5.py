# Author: SCT (AMDG) 3/23/22

# check if the letters in word are in order
def is_abecedarian(word):
    w = list(word)
    # x starts as 1 because loop check letter at x index and x - 1
    x = 1
    while x < len(word):
        # if not in order return False
        if not w[x] >= w[x-1]:
            return False
        
        x += 1

    return True

# opens file
words = open("words.txt")

# reads file
word = words.readlines()
num = 0

# if the word is abecedarian, variable num will plus one
for y in word:
    y = y.strip() # removes escape characters
    if is_abecedarian(y) == True:
        num += 1

print(num)

# closes file
words.close()