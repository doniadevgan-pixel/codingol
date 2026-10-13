# Part 1

n=int(input("How many characters do you want to preview? "))
file= open("Notes.txt", "r")
print(file.read(n))
file.close()
print()

# Part 2

file= open("Notes.txt", "r")
lines=file.readlines()
file.close()
print("total lines:", len(lines))
print(lines)
for i in range(len(lines)):
    print(i+1, "->", lines[i].strip())
print()

# Part 3

word=input("Skip lines starting with: ")
file= open("Notes.txt", "r")
for line in file:
    if line.startswith(word):
        print ("skip ->", line.strip())
    else:
        print(line.strip())
file.close()
print()

# Part 4

file= open ("notes.txt", "r")
lines= file.readlines()
file.close()
out= open ("notes2.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd lines saved to notes2.txt")
    