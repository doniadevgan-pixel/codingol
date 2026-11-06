scores=[1,4,7,10,13,16,19,22]

input("list: " + str(scores) +" n=9 Press Enter to continue")
guess= input("Max checks to find any number in this list: ?")
target= int(input("Enter a number to search for in the list: "))

input("Binary search- checks the middle, drops half the list each time. Press Enter to continue")
low, high = 0, len(scores) - 1
steps = 0
while low <= high:
    mid = (low + high) // 2
    steps += 1
    print("Round", steps, "-> cheaked", scores[mid])
    if scores[mid] == target:
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print("found", target, "at position", mid+1, "in", steps, "steps your guess was", guess,"-> o(log n)")

input("Steps grow slowly with n. Press Enter")
for n, s in [(9,4), (100,10), (1000,10)]:
    print("n=", n, "max steps=", s, "-> O(log n)")