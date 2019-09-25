country = input('Insert Country: ').up per()
budget = float(input('Insert Budget: '))

if (country == 'BRASIL'):
    if (budget <= 25000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 25000000 and budget <= 33000000):
        print('Total project value: ', budget * 1.20)
    elif (budget > 33000000):
        print('Total project value: ', budget * 1.35)

if (country == 'EUA'):
    if (budget <= 12500000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 12500000 and budget <= 27000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 27000000):
        print('Total project value: ', budget * 1.10)

if (country == 'FRANCA' or country == 'FRANÇA'):
    if (budget <= 10000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 10000000 and budget <= 15000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 15000000):
        print('Total project value: ', budget * 1.10)