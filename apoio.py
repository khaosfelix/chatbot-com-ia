# Listas
lista_nova = []
nomes = ["Khaos", "Bubba"]

nomes.append("Loretta")
print(nomes)

# Dicionário = {chave: valor}

idades = {"Khaos": 27, "Bubba": 27}
idades["Bubba"] = 30
idades["Loretta"] = 14
print(idades)

mensagem1 = {"role": "assistant", "content": "Bora aprender Python"}
mensagem2 = {"role": "user", "content": "Bora sim"}
mensagem3 = {"role": "assistant", "content": "Vamos começar"}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Opa, então bora botar Python pra jogo"}
lista_mensagens.append(nova_mensagem)

print(lista_mensagens)
