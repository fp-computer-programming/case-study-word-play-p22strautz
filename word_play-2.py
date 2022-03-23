# Author: SCT (AMDG) 3/23/22

# loop checks if a words contains e
def no_e(word1):
    for x in word1:
        if x == "e":
            # if word contains e returns false
            return False

    return True

# opens files
words = open("words.txt")
file = open("words_without_e.txt","a")

word = words.readlines()
# tracks total words
num1 = 0
# tracks total words without e
num2 = 0
for y in word:
    y = y.strip()
    # each loop adds 1 until total number of words
    num1 += 1
    if no_e(y) == True:
        file.write(y)
        num2 += 1
        # if word does not contain e + 1 and appends word


# calculates the percentage of no e words
percent = num2 / num1 * 100
print("{:.4f} percent of words do not contain e".format(percent))
words.close()
file.close()

