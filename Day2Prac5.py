# Sample data
purchases = [
    ("C1", "Laptop", 1200),
    ("C2", "Laptop", 950),
    ("C1", "Mouse", 25),
    ("C3", "Keyboard", 75),
    ("C2", "Mouse", 30),
    ("C3", "Laptop", 1200),
    ("C1", "Keyboard", 50),
    ("C2", "Keyboard", 60),
    ("C3", "Mouse", 20)
]

# 1. Aggregate Purchase Data
customer_totals = {}
product_totals = {}

for customer_id, product, amount_spent in purchases:
    if customer_id in customer_totals:
        customer_totals[customer_id] += amount_spent
    else:
        customer_totals[customer_id] = amount_spent

    if product in product_totals:
        product_totals[product] += amount_spent
    else:
        product_totals[product] = amount_spent

# print(customer_totals)
# print(product_totals)
# 2. Find Top Customers
# Convert dictionary items to a list of tuples
# print(customer_totals)
customer_list = list(customer_totals.items())
# print(customer_list)
# Sort the list manually
for i in range(len(customer_list)):
    for j in range(i + 1, len(customer_list)):
        if customer_list[i][1] < customer_list[j][1]:
            customer_list[i], customer_list[j] = customer_list[j], customer_list[i]

top_customers = customer_list[:2]
# print(customer_list)

# 3. Find Most Popular Products
# Convert dictionary items to a list of tuples
product_list = list(product_totals.items())

# Sort the list manually
for i in range(len(product_list)):
    for j in range(i + 1, len(product_list)):
        if product_list[i][1] < product_list[j][1]:
            product_list[i], product_list[j] = product_list[j], product_list[i]

top_products = product_list[:3]

# Output the results
print("Customer Report")
print("Top 2 Customers:")
for customer, total in top_customers:
    print(f"{customer}: Total Spent = {total}")

print("\nMost Popular Products:")
for product, total in top_products:
    print(f"{product}: Total Spent = {total}")
