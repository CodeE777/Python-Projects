def count_char(text, char):
    count = 0
    for c in text: 
        if c == char: 
            count += 1
    return count 
# custom function with text and char as arguments
#we use a conter argument to start are parsing at 0
# cycling through our txt file 
file = open("codetester.text","w")

file.close()
filename = "codetester.txt"
with open(filename) as f: 
    text = f.read()
# we then loop through for each char as denoted by this for loop and our alphabet string (below)
for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2))) 

# the perc = function gives us the percentage of each by multiplying our count by 100 and then dividing them by total len of txt file
# the .format takes the character percentave and minues it by the rounded two decimal place to give us answers to the 100th place. 