def numeros(num):
    for i in range(10, num, 10):
        if i < 999:
            print(i, end=', ')
        else:
            print(i, end='.')

def main():
    num = 1001
    numeros(num)

if __name__ == '__main__':
    main()