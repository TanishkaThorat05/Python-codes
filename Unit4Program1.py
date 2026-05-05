# File Handling Demonstration

# 1. Writing to a file (creates file if it doesn't exist)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This file is created using Python.\n")
file.close()   # Properly closing the file

# 2. Reading the file
file = open("sample.txt", "r")
content = file.read()
print("File Content after Writing:\n")
print(content)
file.close()

# 3. Appending data to the file
file = open("sample.txt", "a")
file.write("This line is added later using append mode.\n")
file.close()

# 4. Reading again after appending
file = open("sample.txt", "r")
content = file.read()
print("File Content after Appending:\n")
print(content)
file.close()