#entrada de dados

altura = int(input("Informe a altura: "))

comprimento = int(input("Informe o comprimento: "))

largura = int(input("Informe a largura: "))



#processamento

piso = largura * comprimento

sala = largura * comprimento * altura

parede = 2*altura*largura + 2*altura*comprimento



#saida de dados

print(f'A área do piso da sala equivale: {piso}, O volume da sala equivale: {sala} e a área das paredes da sala equivale: {parede}.')





