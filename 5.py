nota1 = int(input(""))
nota2 = int(input(""))
nota3 = int(input(""))

if nota3 > 8:
    nota3 = nota3 + 1
    
media = (nota1 + nota2 + nota3) /3

if media > 10:
    media = 10
    
print(f'{media}')