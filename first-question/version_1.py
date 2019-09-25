#Importo a biblioteca 'math'. 
import math

#Recebo o valor de x. Passado pelo usuário.
x = int(input('Insert "x" value: '))

#Verificando se o valor está no range passado pelo problema.
if(x >= 10 and x <= 55):
    #Calculando o valor da aresta.
    edge = float(math.pow(x, 3)+(6 * math.pow(x, 2)) + math.sqrt((2 + x) - 7))

    #Calculando o valor do lado do quadrado.
    sideOfSquare = float(1.5 * edge)

    #Calculando a altura da pirâmide.
    #Para calular a altura, eu uso a diagonal do quadrado da base e o valor da aresta.
    diagonal = sideOfSquare * math.sqrt(2)
    height = float(math.sqrt((4 * math.pow(edge, 2)) - (math.pow(diagonal, 2))/4))

    #Calculando o volume.
    volume = float(math.pow(sideOfSquare, 2) * height)/3

    #Exibindo para o usuário.
    print(volume)
#Caso o valor passado não esteja no range aceito, exibo a mensagem abaixo.
else:
    print('Unacceptable value ! Please, restart the software and insert a valid value.')
