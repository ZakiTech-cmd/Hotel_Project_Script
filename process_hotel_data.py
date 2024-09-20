import json

# Load JSON data
with open('hotel_data.json', 'r') as file:
    data = json.load(file)

# Extract assignment results
assignment = data["assignment_results"][0]
prices = assignment["shown_price"]
net_prices = assignment["net_price"]
taxes_str = assignment["ext_data"]["taxes"]

# Parse the taxes from the string format
taxes = json.loads(taxes_str)

# Find the cheapest price manually (without min function)
cheapest_price = float('inf')
cheapest_room_type = None

for room_type, price in prices.items():
    price = float(price)  # Convert to float for comparison
    if price < cheapest_price:
        cheapest_price = price
        cheapest_room_type = room_type

# Find number of guests (it is the same for all rooms in this case)
num_guests = assignment["number_of_guests"]

# Print the cheapest room type and price
print(f"Cheapest room type: {cheapest_room_type}")
print(f"Number of guests: {num_guests}")
print(f"Cheapest price: ${cheapest_price}")

# Calculate and print the total price for all rooms
total_prices = {}

for room_type, net_price in net_prices.items():
    net_price = float(net_price)
    total_price = net_price + sum(float(tax) for tax in taxes.values())
    total_prices[room_type] = total_price

# Print the total prices for all rooms
for room_type, total_price in total_prices.items():
    print(f"Room type: {room_type} - Total price (Net + Taxes): ${total_price:.2f}")

# Save the results to a file
with open('output.txt', 'w') as output_file:
    output_file.write(f"Cheapest room type: {cheapest_room_type}\n")
    output_file.write(f"Number of guests: {num_guests}\n")
    output_file.write(f"Cheapest price: ${cheapest_price}\n")
    output_file.write("\nTotal price for all rooms (Net + Taxes):\n")
    for room_type, total_price in total_prices.items():
        output_file.write(f"Room type: {room_type} - Total price: ${total_price:.2f}\n")

# End of the script
