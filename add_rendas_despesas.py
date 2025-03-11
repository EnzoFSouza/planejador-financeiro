import json

def criarDicionario():
    nome = input("Nome: ")
    valor = input("Valor: ")
    prioridade = input("Prioridade: ") #Utilizado principalmente nas despesas
    x = {
        'nome': nome,
        'valor': valor,
        'prioridade': prioridade,
    }
    return x

def escrever_ativos(tipo, lista):
    f = open(f"{tipo}.txt", "a+")
    y = json.dumps(lista)
    f.write(y)
    f.close()

rendas = list()
despesas = list()

n_rendas = int(input())
n_despesas = int(input())

for i in range(n_rendas):
    print("Adicione fonte de renda")
    rendas.append(criarDicionario())

for i in range(n_despesas):
    print("Adicione despesas")
    despesas.append(criarDicionario())

escrever_ativos("rendas", rendas)
escrever_ativos("despesas", despesas)