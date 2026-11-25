# Task 4: Read from a File
file = open("sample_output.txt", "r")
content = file.read()
print("--- File Content ---")
print(content)
file.close()
