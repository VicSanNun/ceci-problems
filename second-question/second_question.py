#Recebendo a região do projeto.
#O ".upper()" serve para deixar o texto em Maísculo. Desse modo, evito entradas como: bRasil ou Brasil ou brasil. transformo tudo em BRASIL
country = input('Insert Country: ').upper()

#Recebendo o orçamento
budget = float(input('Insert Budget: '))

#Verificando os Países e os orçamentos
if (country == 'BRASIL'):
    if (budget <= 25000000):
        #Exibo essa frase: "Total project value" e o valor do orçamento + porcentagem de margem de segurança
        print('Total project value: ', budget * 1.10)
    elif (budget > 25000000 and budget <= 33000000):
        print('Total project value: ', budget * 1.20)
    elif (budget > 33000000):
        print('Total project value: ', budget * 1.35)

elif (country == 'EUA'):
    if (budget <= 12500000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 12500000 and budget <= 27000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 27000000):
        print('Total project value: ', budget * 1.10)

elif (country == 'FRANCA' or country == 'FRANÇA'):
    if (budget <= 10000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 10000000 and budget <= 15000000):
        print('Total project value: ', budget * 1.10)
    elif (budget > 15000000):
        print('Total project value: ', budget * 1.10)

else:
    print('Please, restart the software and insert a valid Country !')