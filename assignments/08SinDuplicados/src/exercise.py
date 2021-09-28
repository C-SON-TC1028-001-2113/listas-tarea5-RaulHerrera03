def main():
    #escribe tu código abajo de esta línea
    a = int(input())
    listas = []
    i = 0
    if a>=0 :
        while i<a :
            valor = input()
            listas.append(valor)
            i = i+1
        print(listas)
        noduplicados = []
        for i in listas :
            if i not in noduplicados :
                noduplicados.append(i)
        print(noduplicados)
    else:
        print('Error')


    pass
if __name__=='__main__':
    main()
