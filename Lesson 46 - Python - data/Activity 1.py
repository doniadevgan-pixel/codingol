classmates = ["Ibrahim", "Ebin", "Yohaan", "Erash", "Aiden"]
print("Class list:", classmates)

print("total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three students:", classmates[:3])

#Step three modify the list
classmates.append("Midge")
print("\nAfter adding Midge:", classmates)
classmates.remove("Ebin")
print("After removing Ebin:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed order:", classmates)

# Step 4 Create a teacher dictionary
teacher = {"name": "Mr. Andrew", "subject": "Science", "years_of_experience": 10}
print("\nTeacher Information:")

# Step 5 Dictionary operations
print("subject:", teacher["subject"])
print("Experience:", teacher.get("years_of_experience", "Not specified"))
teacher["years_of_experience"] = 10
teacher["email"] = "mr.andrew@school.com"
print("Updated teacher information:", teacher)

#Step 6 Convert lists to a student dictionary
roll_numbers = [1, 2, 3, 4, 5]
names = ["Ibrahim", "Ebin", "Yohaan", "Erash", "Aiden"]
students = dict(zip(roll_numbers, names))
print("\nStudent Dictionary:", students)
print("student at roll 3:", students[3])
