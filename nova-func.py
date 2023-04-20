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

def conversão(primeiraUnidade, unidadeParaConverter, númeroParaConversão):
    difDeConversão = diferençaConversão(primeiraUnidade, unidadeParaConverter)
    númeroConvertido = númeroParaConversão

    if(primeiraUnidade == 'bit' or unidadeParaConverter == 'bit'):
        if(primeiraUnidade == 'bit'):
            númeroConvertido /= 8
            difDeConversão += 1 
        if(unidadeParaConverter == 'bit'):
            númeroConvertido *= 8 
            difDeConversão -= 1 

    if (difDeConversão < 0):
            difDeConversão *= -1
            difDeConversão = 1024 ** difDeConversão
            númeroConvertido /= difDeConversão
    elif(difDeConversão > 0):
            difDeConversão = 1024 ** difDeConversão
            númeroConvertido *= difDeConversão
            
    return númeroConvertido