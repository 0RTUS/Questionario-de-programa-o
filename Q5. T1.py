def tamanho(maior):
    for i in range(0, 99):
        valor = int(input(""))
        if valor > maior:
            maior = valor
    print(maior)


def main():
    maior = 0
    tamanho(maior)


if __name__ == '__main__':
    main()
