# Step 1 Create tuples for recipe details 
pasta= ("Pasta", "Italian", 26, "medium")
biriyani= ("Biryani", "Indian", 45, "hard")
print("recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[3])

# Step 2- Nested tuples for recipe details
all_recipes= (pasta, biriyani)
print("\nFirst recipe:", all_recipes[0][0])
print("second recipe:", all_recipes[1][2], "minutes")
print("Pasta details (sliced):", pasta[1:3])

# Step 3 - Interate through a tuple

print("\npasta recipe details:")
for detail in pasta:
    print(" -", detail)

# Step 4 - Create sets for ingredients (no duplicates allowed)

pasta_ingredients= {"tomato", "garlic", "olive oil", "chilli", "parmesan cheese", "chilli"}
briyani_ingredients= {"rice", "chicken", "garlic", "onion", "cumin", "chilli"}
print("\nPasta ingredients:", pasta_ingredients)
print("Biryani ingredients:", briyani_ingredients)
print("total pasta ingredients:", len(pasta_ingredients))

# Step 5 - Modify the set

pasta_ingredients.add("basil")
pasta_ingredients.discard("garlic")
print("\nUpdated pasta ingredients:", pasta_ingredients)

# Step 6 - Set operations
all_ingredients= pasta_ingredients.union(briyani_ingredients)
common = pasta_ingredients.intersection(briyani_ingredients)
only_pasta = pasta_ingredients.difference(briyani_ingredients)
unique_ingredients= pasta_ingredients.symmetric_difference(briyani_ingredients)

print("\nALL ingrediants (union):", all_ingredients)
print("Common ingrediants (intersection):", common)
print("Only pasta ingrediants (difference):", only_pasta)
print(" Not shared (symmetric difference):", unique_ingredients)
