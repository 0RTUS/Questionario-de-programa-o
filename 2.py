def impar(numero):
    if numero % 2 == 1:
        print(True)
    else:
        print(False)

def main():
    numero = int(input(""))
    impar(numero)

if __name__ == '__main__':
    main()