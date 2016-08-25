INTEREST_RATE = 0.4

deposit = float(input('Deposit amount: $'))

year_one = deposit + (INTEREST_RATE * deposit)
year_two = year_one + (INTEREST_RATE * year_one)
year_three = year_two + (INTEREST_RATE * year_two)

print('Year one balance: $%.2f') % year_one
print('Year two balance: $%.2f') % year_two
print('Year three balance: $%.2f') % year_three
