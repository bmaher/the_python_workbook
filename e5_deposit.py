SMALL_DEPOSIT = 0.10
LARGE_DEPOSIT = 0.25

small_bottles = int(input('Number of small bottles: '))
large_bottles = int(input('Number of large bottles: '))

small_refund = small_bottles * SMALL_DEPOSIT
large_refund = large_bottles * LARGE_DEPOSIT
total_refund = small_refund + large_refund
print('Refund: $%.2f') % total_refund
