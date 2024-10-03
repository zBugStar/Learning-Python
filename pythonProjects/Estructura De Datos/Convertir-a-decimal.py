def Dec2Bin(numero):

    if numero == 0:
        return '0'
    elif numero == 1:
        return '1'
    else:
        return Dec2Bin(numero // 2) + str(numero % 2)


numero_decimal = 10
binario = Dec2Bin(numero_decimal)
print(binario)
