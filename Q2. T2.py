def musica(msc):
    for msc in range(msc, 251, 7):
        if msc < 244:
            print(f'{msc} bugs no software, pegue sete deles e conserte...\n'
                  'Tecle "Ctrl+F5"')
        if msc > 245:
            print(f'{msc} bugs no software, pegue sete deles e conserte...\n'
                  'Tecle "Ctrl+F5"\n'
                  'Vamos fazer mais um café!')


def main():
    msc = 99
    musica(msc)


if __name__ == '__main__':
    main()
