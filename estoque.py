
import json

# Parte 1: Criando os dados da loja
loja = {
    "nome": "TechStore",
    "produtos": [
        {
            "nome": "Teclado",
            "preco": 150.00,
            "quantidade": 10
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
            "quantidade": 15
        },
        {
            "nome": "Monitor",
            "preco": 950.00,
            "quantidade": 5
        }
    ]
}

# Salvando os dados iniciais
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)


# Parte 2: Lendo os dados do arquivo
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)


# Exibindo os produtos
print(f'Loja: {dados_lidos["nome"]}\n')

for produto in dados_lidos["produtos"]:
    print(
        f'O produto {produto["nome"]} '
        f'custa R$ {produto["preco"]:.2f}'
    )


# Adicionando um novo produto
novo_produto = {
    "nome": "Fone de Ouvido",
    "preco": 120.00,
    "quantidade": 8
}

dados_lidos["produtos"].append(novo_produto)


# Desafio extra: desconto de 10% no Mouse
for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Mouse":
        produto["preco"] *= 0.90
        print(
            f'\nNovo preço do Mouse: '
            f'R$ {produto["preco"]:.2f}'
        )


# Salvando o estoque atualizado
with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print("\nEstoque atualizado com sucesso!")