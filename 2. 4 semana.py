def var(dia, mes, ano, dia2, mes2, ano2, data1, data2):
    if data1 > data2:
        print(f'{dia}/{mes}/{ano}')
    else:
        print(f'{dia2}/{mes2}/{ano2}')

def main():
    dia = int(input(""))
    mes = int(input(""))
    ano = int(input(""))
    
    dia2 = int(input(""))
    mes2 = int(input(""))
    ano2 = int(input(""))
    
    data1 = dia, mes, ano
    data2 = dia2, mes2, ano2
    
    var(dia, mes, ano, dia2, mes2, ano2, data1, data2)

if __name__ == '__main__':
    main()

    
