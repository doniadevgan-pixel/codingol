for i in range(1,11):
    print(f"23 * {i} = {23 * i}")

#Get the number of rows from user
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop for each column in the row
    for j in range(i):
# Print star, end with space instead of new line
        print("*", end=" ")
# after each row, print a new line
    print()

total_sum = 0
num = 1
while num <= 10:
    total_sum += num
    num += 1

print(f"The sum of the first 10 natural numbers is {total_sum}")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             