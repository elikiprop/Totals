prices = []

while True:
    value = input("Enter a price (or 'q' to quit): ")
    if value.lower() == 'q':
        break
    prices.append(float(value))

total = sum(prices)
print(f"The total is: {total}")
