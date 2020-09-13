def contador(par, impar):
    for i in range(100):
        num = int(input(""))
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
    print(par)
    print(impar)

def main():
    par = 0
    impar = 0
    contador(par, impar)

if __name__ == '__main__':
    main()