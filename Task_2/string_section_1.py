# String Practice Questions (10 Problems)

# 1. Extract the first 3 characters of: text = 'Python'
# 2. Convert to lowercase: name = 'hello WORLD'
# 3. Remove extra spaces: msg = ' Welcome to Python '
# 4. Find the length of: word = 'Programming'
# 5. Split based on comma: text = 'apple,banana,grape'
# 6. Replace 'Java' with 'Python' in: text = 'I love Java'
# 7. Extract 'Science' from: line = 'Data Science'
# 8. Get the last character of: text = 'Python'
# 9. Check if 'Python' is present in: sentence = 'Learning Python is fun'
# 10. Join list into a sentence: words = ['Python', 'is', 'easy']

# Answers: 

# 1. Extract the first 3 characters
text = 'Python'
print(text[:3])   # Pyt

# 2. Convert to lowercase
name = 'hello WORLD'
print(name.lower())   # hello world

# 3. Remove extra spaces
msg = ' Welcome to Python '
print(msg.strip())   # Welcome to Python

# 4. Find the length
word = 'Programming'
print(len(word))   # 11

# 5. Split based on comma
text = 'apple,banana,grape'
print(text.split(','))   # ['apple', 'banana', 'grape']

# 6. Replace 'Java' with 'Python'
text = 'I love Java'
print(text.replace('Java', 'Python'))   # I love Python

# 7. Extract 'Science'
line = 'Data Science'
print(line[5:])   # Science

# 8. Get the last character
text = 'Python'
print(text[-1])   # n

# 9. Check if 'Python' is present
sentence = 'Learning Python is fun'
print('Python' in sentence)   # True

# 10. Join list into a sentence
words = ['Python', 'is', 'easy']
print(' '.join(words))   # Python is easy
