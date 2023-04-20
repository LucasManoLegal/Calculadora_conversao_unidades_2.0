UnidadesDeMedida = ['bit', 'byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte']



def Conversão (Valor1, Valor2):
    contador = 0
    for i in UnidadesDeMedida:
        if (Valor1 == i):
            Valor1 = contador

        if (Valor2 == i):
            Valor2 = contador


            contador += 1
            return Valor1 - Valor2