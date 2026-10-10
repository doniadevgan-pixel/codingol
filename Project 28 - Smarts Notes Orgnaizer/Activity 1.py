
sample_notes = [
    "IMPORTANT: Finish maths homework\n",
    "TODO: Revise Python file handling\n",
    "NOTE: read(n) shows characters\n",
    "IMPORTANT: Submit school assignment\n",
    "SKIP: This note is not needed\n",
    "NOTE: readlines() makes a list\n",
    "TODO: Practise loops and files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()

print("My notes file has been created.")


print("\nPART 1: Preview my notes")

file = open("class-notes.txt", "r")
print(file.read(40))
file.close()



print("\nPART 2: Show all notes")

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))

for number, line in enumerate(lines, start=1):
    print(number, "->", line.strip())



print("\nPART 3: Reading each note")

file = open("class-notes.txt", "r")

for line in file:
    print("Reading:", line.strip())

file.close()


print("\nPART 4: Sort out my notes")

kept = 0
skipped = 0

file = open("class-notes.txt", "r")

for line in file:
    line = line.strip()

    if line.startswith("SKIP"):
        print("Skipped:", line)
        skipped = skipped + 1
    else:
        print("Kept:", line)
        kept = kept + 1

file.close()

print("Notes kept:", kept)
print("Notes skipped:", skipped)



print("\nPART 5: Save selected notes")

file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

new_file = open("organized-notes.txt", "w")

copied = 0

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        new_file.write(line)
        copied = copied + 1

new_file.close()

print("Notes copied:", copied)


print("\nPART 6: My organized notes")

file = open("organized-notes.txt", "r")

for line in file:
    print(line.strip())

file.close()

print("\nAll done! My notes are organized.")