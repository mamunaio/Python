# 1. Setup the inventory (Dictionary)
inventory = {
    "apple": 0.50,
    "banana": 1.30,
    "milk": 2.50,
    "bread": 1.20,
    "tomato": 5.00
}

# 2. Initialize variables
shopping_cart = []
total_price = 0.0

# print("--- Welcome to the Python Store ---")
# print("Avilable items: apple, banana, milk, bread, coffee")
# print("Type 'done' to finish shopping")

# # 3. Use a loop to get user input
# while True:
#     item = input("\nEnter item name:").lower().strip()  # Standardize input
#     if item == "done":
#         break

#     # 4. Check if item exists (Membership test)
#     if item in inventory:
#         price = inventory[item]
#         shopping_cart.append(item)  # Add to List
#         total_price += price  # Update running total
#         print(f"Added {item} to cart. Price: ${price:.0f}")
#     else:
#         print("Sorry, we don't have 그 that item in stock.")

#     # 5. Final Output (Summary)
#     print("\n--- Your Final Receipt ---")
#     print(f"Items purchased: {shopping_cart}")
#     print(f"Total price: {total_price:.2f}")
#     print("--- Thank you for shopping! ---")