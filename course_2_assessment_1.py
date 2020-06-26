# 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

file = open("travel_plans.txt")
data = file.read()
num = len(data)

# 2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.

file = open("emotion_words.txt", "r")
data = file.read()
words = data.split()
num_words = len(words)
print(num_words)

# 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.

file = open("school_prompt.txt", "r")
data = file.readlines()
num_lines = len(data)
print(num_lines)

# 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

file = open("school_prompt.txt", "r")
data = file.read()
beginning_chars = data[:30]
print(beginning_chars)

# 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

file = open('school_prompt.txt', 'r')
three = []
for line in file:
    word = line.split()
    three.append(word[2])
print(three)

# 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

file = open('emotion_words.txt', 'r')
emotions = []
for line in file:
    word = line.split()
    emotions.append(word[0])
print(emotions)

# 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

file = open('travel_plans.txt', 'r')
first_chars = file.read(33)
print(first_chars)

# 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

file = open('school_prompt.txt', 'r')
p_words = []
for line in file:
    words = line.split()
    for word in words:
        if "p" not in word:
            continue
        p_words.append(word)
print(p_words)
