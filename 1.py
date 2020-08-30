def proc(nome, sexo):
    if sexo == 1:
        print(f'Ilmo Sr. {nome}')
    else:
        print(f'Ilma Sra. {nome}')
    
def main():
    nome = input("")
    sexo = int(input(""))
    proc(nome, sexo)
    
if __name__ == '__main__':
    main()