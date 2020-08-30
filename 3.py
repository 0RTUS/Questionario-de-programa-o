def cores(sinal):
    if sinal == 'V':
        print('Siga')
    elif sinal == 'A':
        print('Atenção')
    elif sinal == 'E':
        print('Pare')

def main():
    sinal = str(input("")).upper()
    cores(sinal)
    
if __name__ == '__main__':
    main()

