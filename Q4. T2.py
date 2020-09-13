def musica(msc):
    for msc in range(msc, 0, -11):
        if msc < 100:
            print(f'{msc} bugs no software, pegue onze deles e conserte...\n'
                  'Tecle "Ctrl+F5"')
        if msc < 12:
            print(f'Sem erros no software! Está estabilizado!')


def main():
    msc = 99
    musica(msc)


if __name__ == '__main__':
    main()
