# Task 3: Write to a File
file = open("sample_output.txt", "w")
file.write("Hello! This is Task 3.\n") 
file.write("This file is created to demonstrate writing to a file in Python.\n")
file.close()

print("Content successfully written to sample_output.txt")
