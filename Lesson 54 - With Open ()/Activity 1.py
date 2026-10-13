# Part 1 - Read with Auto-Close
print("=== Science Notes ===")
with open("Science Notes.txt", "r") as s :
    for line in s:
        print(line.strip())
print()

# Part 2 - Count Words in each line
print("===Word Count===")
with open("Maths Notes.txt") as s :
    for line in s:
        words = line.split()
        print(len(words), "words ->", line.strip())
print()

# Part 3 - Check and Merge
import os
print("===Merging Notes===")
if os.path.exists("all-notes.txt"):

 print("all-notes.txt already exists - overwriting")

else:

 print("all-notes.txt not found - creating now")

content = ""

with open("Science Notes.txt", "r") as f:

 content += "--- science-notes.txt ---\n"

 content += f.read() + "\n" 

with open("Maths Notes.txt", "r") as f:

 content += "--- maths-notes.txt ---\n"

 content += f.read() + "\n"

with open("all-notes.txt", "w") as out:

 out.write(content)

print("Saved to all-notes.txt")

print()