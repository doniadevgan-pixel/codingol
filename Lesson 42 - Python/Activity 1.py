# part 1 - User Input
city = input("Enter your city name: ")
temperature = float(input("Enter the temperature in Celsius: "))

# part 2 - if statement

if temperature > 29:
    print(f"It's hot in {city}! Wear light clothing!")

# part 3 - else statement

if temperature <= 24:
    print(f"It's not too hot in {city}. You can wear normal clothing.")

else:
    print(f"It's cold in {city}. Wear warm clothing!")

# part 4 - if-elif-else statement

if temperature > 29:
    print(f"It's hot in {city}! Wear light clothing!")
elif temperature <= 24:
    print(f"It's not too hot in {city}. You can wear normal clothing.")
elif temperature > 15:
    print(f"It's a bit chilly in {city}. Wear a jacket!")
else:
    print(f"It's cold in {city}. Wear warm clothing!")

# part 5 - Data time module
import datetime
import calendar

now = datetime.datetime.now()
print("city:", city)
print("Time now:", now)

print(calendar.calendar(now.year))
