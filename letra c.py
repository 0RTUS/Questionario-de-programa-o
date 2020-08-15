#entrada de dados
horas = int(input('Quantas horas: '))

minutos = int(input('Quantos minutos: '))

segundos = int(input('Quantos segundos: '))



#processamento

h = (horas*3600)

m = (minutos*60)

s = (segundos*1)



#saida de dados

print(f'{h+m+s} segundos já se passaram da meia-noite até agora.')