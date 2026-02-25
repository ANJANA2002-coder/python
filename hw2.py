paragraph = """
   This Python course is designed for beginners who want to learn programming.
   The course covers Python basics, problem-solving skills, and real-world examples.
"""
paragraph = paragraph.strip()

length = len(paragraph)
print("Length of paragraph:", length)
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])
print("Preview (first 50 characters):", paragraph[:50])
replaced_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", replaced_paragraph)
lowercase_paragraph = paragraph.lower()
print("\nLowercase paragraph:\n", lowercase_paragraph)
words = paragraph.split()
print("\nList of words:\n", words)
exists = "course" in paragraph.lower()
print("Does the word 'course' exist?", exists)
