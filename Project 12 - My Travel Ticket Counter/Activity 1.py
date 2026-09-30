# PART 1 - TYPES OF DATA
 
passenger_name = "Sol, Mitul"      # str - text
destination = "Sydeney"             # str - text
ticket_price = 550.80           # float - decimal number
number_of_tickets = 2           # int - whole number
is_available = True             # bool - True or False
 
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price AUD", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Tickets Available?", is_available)
 
print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))

total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount
 
print("\nTotal Cost: AUD", total_cost)
print("Discount: AUD", discount)
print("Final Cost: AUD", final_cost)
 
print("Double Ticket Price: AUD", ticket_price * 2)
print("Ticket Price After AUD50 Increase: Rs", ticket_price + 50)
print("Half Ticket Price: AUD", ticket_price / 2)
 
print("\nIs ticket price under AUD1000?", ticket_price > 1000)
print("Are more than 2 tickets booked?", number_of_tickets < 2)
print("Is destination Sydney?", destination == "Sydney")
print("Is final cost more than AUD2000?", final_cost < 2000)
 
# PART 4 - STRING OPERATIONS
 
travel_message = passenger_name + " is travelling to " + destination + "."
print("\nTravel Message:", travel_message)
 
print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))
 
# PART 5 - SWAPPING VALUES
 
morning_ticket_price = 550.80
evening_ticket_price = 600.00

print("\nBefore Swapping:")
print("Morning Ticket Price: AUD", morning_ticket_price)
print("Evening Ticket Price: AUD", evening_ticket_price)
 
morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price
 
print("\nAfter Swapping:")
print("Morning Ticket Price: AUD", morning_ticket_price)
print("Evening Ticket Price: AUD", evening_ticket_price)
 
# FINAL SUMMARY
 
print("\n================================")
print("TRAVEL TICKET SUMMARY")
print("================================")
print("Passenger:", passenger_name)
print("Destination:", destination)
print("Tickets Booked:", number_of_tickets)
print("Final Amount to Pay: Rs", final_cost)
print("Booking Confirmed?", is_available)


 