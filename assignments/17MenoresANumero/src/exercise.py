

def main():
    a = int(input(''))
    b = int(input(''))
    c = a*b
    lista=[]
    i=1
    while i<=c:
        i=i+1
        v = int(input(''))
        if v<10:
            lista.append(v)
    print(lista)


if __name__=='__main__':
    main()
