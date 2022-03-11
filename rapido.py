import string

def listaCaracteres():
    lista = []
    for i in string.printable: #obtenemos todos los caracteres imprimibles
        lista.append(i)
    return lista

x = ''.join(listaCaracteres())