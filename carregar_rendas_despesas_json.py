import json

def somar(lista_de_dicts):
    soma = 0
    for i in range(len(lista_de_dicts)):
        soma += float(lista_de_dicts[i]['valor'])
    
    return soma

with open("rendas.txt", "r") as f:
    rendas = json.load(f)
    f.close()

with open("despesas.txt", "r") as f:
    despesas = json.load(f)
    f.close()


total_rendas = somar(rendas)
total_despesas = somar(despesas)

print(rendas)
print("Total rendas: ", total_rendas)

print(despesas)
print("Total despesas: ", total_despesas)