UnidadesDeMedida = ['bit', 'byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte']


def diferençaConversão(primeiraUnidade, unidadeParaConverter):
    contador = 0
    for i in UnidadesDeMedida:
        if (primeiraUnidade == i):
            primeiraUnidade = contador

        if (unidadeParaConverter == i):
            unidadeParaConverter = contador

        contador += 1
    difDeConversão = primeiraUnidade - unidadeParaConverter
    return int(difDeConversão)