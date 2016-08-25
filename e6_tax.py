TAX_RATE = 0.175
TIP_RATE = 0.18

cost = float(input('Meal cost: '))
tax = TAX_RATE * cost
tip = TIP_RATE * cost
total = cost + tax + tip
print('Cost: $%.2f') % cost
print('Tax: $%.2f') % tax
print('Tip: $%.2f') % tip
print('Total: $%.2f') % total
