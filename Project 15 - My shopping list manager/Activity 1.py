file_name = "shopping_list.txt"

shopping_file = open(file_name, "w")

shopping_file.write("Running shoes (Nike zoom)\n")
shopping_file.write("Pull up bar (for home)\n")
shopping_file.write("Watch (Garmin Forerunner 245)\n")
shopping_file.write("Air pods 5th gen\n")
shopping_file.close()

print("Shopping list has been created and saved to", file_name)

shopping_file = open(file_name, "r")

print("Here is your shopping list:")
content = shopping_file.read()
print(content)
shopping_file.close()

shopping_file = open(file_name, "a")

shopping_file.write("New two bike tires (Maxxis)\n")
shopping_file.write(" 20 packs Lychee Juice (mogu mogu)\n")
shopping_file.close()
print("New items have been added to your shopping list.")

shopping_file = open(file_name, "r")

print("Here is your updated shopping list:")
updated_content = shopping_file.read()
print(updated_content)
shopping_file.close()

shopping_file = open(file_name, "r")

print("Here is your shopping list in reverse order:")

line_number = 1

for line in shopping_file:
    print(f"{line_number}. {line.strip()}")
    line_number += 1

shopping_file.close()

print("\n=================")
print("Shopping list Manager")
print("=================")
print("file name:", file_name)
print("Items were written to the file and read back successfully.")
print("Thank you for using the shopping list program. Goodbye!")
print("==================")


