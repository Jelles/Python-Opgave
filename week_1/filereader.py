contents = open("recourses/diktrom.txt").read()
num_words = len(contents.split())
num_char = len(contents)
num_lines = len(contents.splitlines())

print("Number of lines: ", num_lines)
print("Number of words in text file: ", num_words)
print("Number of characters: ", num_char)
