def inicializacion():
    try:
        lista = []
        with open("frecuencia.txt") as f:
            frecuencia = f.readlines()

        for i in frecuencia:
            dicc = {
                "caracter":i.split()[0],
                "frecuencia":i.split()[1],
                "probabilidad":i.split()[2]
            }
            lista.append(dicc)
        return lista
    except:
        print("escoja un archivo txt")