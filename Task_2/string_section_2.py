# Medium to Hard String Practice Questions (10)

# 1. Extract 'Programming' from: text = 'PythonProgramming' using slicing only.
# 2. Count how many times 'Hello' appears in: s = 'Hello, Python, Hello, World'.
# 3. Reverse the string without using reverse(): word = 'Development'.
# 4. Replace 'awesome' with 'powerful' only if 'Python' exists in: sentence = 'Python is awesome'.
# 5. Count occurrences of 'aaa' (including overlapping) in: text = 'aaabbbcccaaa'.
# 6. Extract username and domain from: email = 'username@example.com'.
# 7. Extract the numeric value from: line = 'The price is 1500 rupees'.
# 8. Split by '-' and rejoin with spaces: words = 'python-is-simple-and-powerful'.
# 9. Remove numbers and keep only letters from: text = 'Hello123World45Python'.
# 10. Find the first character that appears more than once in: text = 'Mississippi'.


# Answers:

# 1. Extract 'Programming' from text using slicing
text = 'PythonProgramming'
print(text[6:])              # Programming


# 2. Count how many times 'Hello' appears
s = 'Hello, Python, Hello, World'
print(s.count('Hello'))      # 2


# 3. Reverse the string without using reverse()
word = 'Development'
print(word[::-1])            # tnemepoleveD


# 4. Replace 'awesome' with 'powerful' only if 'Python' exists
sentence = 'Python is awesome'
if 'Python' in sentence:
    sentence = sentence.replace('awesome', 'powerful')
print(sentence)              # Python is powerful


# 5. Count occurrences of 'aaa' (including overlapping)
text = 'aaabbbcccaaa'
count = sum(1 for i in range(len(text)) if text[i:i+3] == 'aaa')
print(count)                 # 2


# 6. Extract username and domain from email
email = 'username@example.com'
username, domain = email.split('@')
print(username)              # username
print(domain)                # example.com


# 7. Extract numeric value from a string
line = 'The price is 1500 rupees'
number = ''.join(ch for ch in line if ch.isdigit())
print(number)                # 1500


# 8. Split by '-' and rejoin with spaces
words = 'python-is-simple-and-powerful'
print(' '.join(words.split('-')))   # python is simple and powerful


# 9. Remove numbers and keep only letters
text = 'Hello123World45Python'
letters = ''.join(ch for ch in text if ch.isalpha())
print(letters)               # HelloWorldPython


# 10. Find first character that appears more than once
text = 'Mississippi'
seen = set()
result = None
for ch in text:
    if ch in seen:
        result = ch
        break
    seen.add(ch)
print(result)                # s
