def resultado(soma):
    for i in range(1, 101):
        valor = int(input(""))
        soma += valor
        total = soma / i
    print("%.2f" % total)


def main():
    soma = 0
    resultado(soma)


if __name__ == '__main__':
    main()
