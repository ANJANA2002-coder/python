# Store a short paragraph using multiline string
paragraph = '''
Python is a popular programming language.
This Python course helps beginners understand Python basics,
data types, functions, and simple projects.
It is an easy and practical course for students.
'''

# Remove extra whitespaces from start and end
paragraph = paragraph.strip()

# Display length of paragraph
length = len(paragraph)
print("Length of paragraph:", length)

# Display first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Slice first 50 characters
print("Preview (first 50 characters):")
print(paragraph[:50])

# Replace "Python" with "PYTHON"
replaced_para = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing Python with PYTHON:")
print(replaced_para)

# Convert entire paragraph to lowercase
lower_para = paragraph.lower()
print("\nParagraph in lowercase:")
print(lower_para)

# Split paragraph into words
words = paragraph.split()
print("\nList of words:")
print(words)

# Check if word "course" exists
if "course" in paragraph:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is NOT found in the paragraph.")

# Display final formatted message
print("\nFinal Message:")
print("The course description is {} characters long and has {} words.".format(length, len(words)))
