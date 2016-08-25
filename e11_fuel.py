L_TO_MPG = 235.214

mpg = float(input('MPG: '))
l_per_100km = L_TO_MPG / mpg
print('%s mpg = %.2f l/100km') % (mpg, l_per_100km)
