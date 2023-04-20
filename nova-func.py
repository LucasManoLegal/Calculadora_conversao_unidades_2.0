UnidadesDeMedida = ['bit', 'byte', 'Kilobyte', 'Megabyte', 'Gigabyte', 'Terabyte', 'Petabyte']


def diferençaConversão(unidadeInicial, unidadeDeConversão):
    contador = 0
    for i in UnidadesDeMedida:
        if (unidadeInicial == i):
            unidadeInicial = contador

        if (unidadeDeConversão == i):
            unidadeDeConversão = contador

        contador += 1
    fatorDeConversão = unidadeInicial - unidadeDeConversão
    return int(fatorDeConversão)