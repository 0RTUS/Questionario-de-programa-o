def parcela(preco):
    for i in range(1, 25):
        valor = preco / i
        print(f'{i}x de R$ {valor:.2f}')

def main():
    preco = float(input(""))
    parcela(preco)

if __name__ == '__main__':
    main()