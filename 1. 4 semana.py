def anos(dia, mes, ano, dia_n, mes_n, ano_n):
    idade = ano - ano_n
    if mes_n > mes:
        idade -= 1
    elif mes_n == mes:
        if dia_n < dia:
            idade -= 1
    return idade

def main():
    dia = int(input(""))
    mes = int(input(""))
    ano = int(input(""))
    dia_n = int(input(""))
    mes_n = int(input(""))
    ano_n = int(input(""))
    print(anos(dia, mes, ano, dia_n, mes_n, ano_n))

if __name__ == '__main__':
    main()