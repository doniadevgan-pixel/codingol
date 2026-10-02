# Part one: Create a bucket list file

file = open ("bucket-list.txt", "w")
file.write (" 1. Visit the Grand Canyon\n")
file.write (" 2. Play piano in a concert\n")
file.write (" 3. Code my own video game\n")
file.close()
print ("Bucket list is saved in bucket-list.txt!")

# Part two: Read the file

file = open ("bucket-list.txt", "r")
content = file.read()
print ("\n== Bucket List ==")
print (content)
file.close()

# Part three: Count the number of items

file = open ("bucket-list.txt", "r")
lines = file.readlines()
print (lines)
print (f"You have {len(lines)} items in your bucket list.")
file.close()

# Part four: Add more items to the list, append mode

file = open ("bucket-list.txt", "a")
file.write(" 4. Surf in Hawaii\n")
file.write (" 5.Run a 3k race in under 30 minutes\n")
file.close()
print ("\n2 more items have been added to your bucket list!")

# Part five: Read the updated file

file = open ("bucket-list.txt", "r")
print ("\n=== Updated Bucket List ===")
print (file.read())
file.close()

# 