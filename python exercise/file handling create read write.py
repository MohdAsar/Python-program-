with open("sample.txt", "w") as file:
    file.write("This is a sample text.")

with open("sample.txt", "r") as file:
    print("File content after writing:", file.read())

with open("sample.txt", "w") as file:
    file.write("New content written to the file.")

with open("sample.txt", "r") as file:
    print("File content after writing new content:", file.read())

# Clearing file content (acts like deletion of content)
with open("sample.txt", "w") as file:
    file.write("")

with open("sample.txt", "r") as file:
    print("File content after deletion:", file.read())