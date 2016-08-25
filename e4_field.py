FEET_IN_ACRE = 43560

length = float(input('Length (feet): '))
width = float(input('Width (feet): '))
area = length * width
acres = area // FEET_IN_ACRE
print('Area: %s acres') % acres
