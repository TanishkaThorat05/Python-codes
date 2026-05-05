# Program to open a file and handle exceptions

# Take filename from user
filename = input("Enter the filename: ")

try:
    # Try to open the file in read mode
    file = open(filename, 'r')
    
    # Read and display contents
    content = file.read()
    print("\nFile contents:\n", content)
    
    # Close the file
    file.close()

# Exception if file does not exist
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename.")

# Exception if permission is denied
except PermissionError:
    print("Error: You do not have permission to read this file.")

# Optional: handle any other unexpected error
except Exception as e:
    print("An unexpected error occurred:", e)