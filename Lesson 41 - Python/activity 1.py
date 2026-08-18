sport_name = "soccer" # String
number_of_players = 11 # Integer - Whole number
cost_of_equipment = 100.50 # Float - Decimal number
is_the_most_popular_game = True # Boolean - True or False

print("Sport Name:", sport_name)
print("Number of Players:", number_of_players)
print("Cost of Equipment:", cost_of_equipment)
print("Is the most popular game:", is_the_most_popular_game)

print(type(sport_name))
print(type(number_of_players))
print(type(cost_of_equipment))
print(type(is_the_most_popular_game))

# Part 2: Arithmetic Operations

total= number_of_players * cost_of_equipment
print("total cost of equipment for all players:", total)
print("sale price $", total * 0.9)
print("double the number of players:", number_of_players * 2)

#part 3: comparison operators

print("Is the number of players greater than 10?", number_of_players > 10)
print("Is the cost of equipment less than 200?", cost_of_equipment < 200)
print("Is the sport name equal to 'soccer'?", sport_name == "soccer")

# part 4: String operations

shop_name = "Sports World"
print("Shop Name:", shop_name)
print("Letters in shop name:", len(shop_name))
print("first letter:", shop_name[0])

# part 5: swapping values

price1 = 50
price2 = 75
print("Before:, price1 =", price1, ", price2 =", price2)

temp = price1
price1 = price2
price2 = temp

print("After:, price1 =", price1, ", price2 =", price2)


