from tabulate import tabulate

lista_produtos = []
vendas_produto = []

def adicionar_produtos():
    adicionar_produtos = input("Informe o produto que você deseja adicionar: \n").upper()
    lista_produtos.append(adicionar_produtos)
    
    while True:
        try:
            adicionar_quantidade_vendas = int(input("Informe a quantidade de vendas do produto: \n"))
            vendas_produto.append(adicionar_quantidade_vendas)
            break
        except ValueError:
            print("Por favor, informe um valor numérico válido para a quantidade de vendas.")

def remover_produto():
    if len(lista_produtos) > 0:
        remover_produto = input("Informe o produto que deseja remover: \n").upper()
        if remover_produto in lista_produtos:
            indice_produto = lista_produtos.index(remover_produto)
            lista_produtos.pop(indice_produto)
            vendas_produto.pop(indice_produto)
            print(f"Produto '{remover_produto}' removido com sucesso!")
        else:
            print("Produto não encontrado na lista.")
    else:
        print("A lista está vazia!!")

def produto_menos_vendido():
    if len(lista_produtos) > 0:
        produto_menos_vendas = min(vendas_produto)
        i = vendas_produto.index(produto_menos_vendas)
        print(f'\nO produto menos vendido foi {lista_produtos[i]} com {produto_menos_vendas} vendas.\n')
    else:
        print("A lista está vazia!!")

def produto_mais_vendido():
    if len(lista_produtos) > 0:
        produto_mais_vendas = max(vendas_produto)
        i = vendas_produto.index(produto_mais_vendas)
        print(f'\nO produto mais vendido foi {lista_produtos[i]} com {produto_mais_vendas} vendas.\n')
    else:
        print("A lista está vazia!!")

def listar_produtos():
    if len(lista_produtos) > 0:
        dados = {
            'Produto': lista_produtos,
            'Vendas': vendas_produto
        }
        tabela = tabulate(dados, headers='keys', tablefmt='psql')
        print(tabela)
    else:
        print("A lista está vazia!!")

while True:
    print("\nBem-vindo!! Essa é sua lista de controle de vendas!!\n")
    try:
        opcoes = int(input("Informe o que você deseja fazer:\n"
        "[1] Adicionar à lista\n"
        "[2] Remover\n"
        "[3] Ver produto menos vendido\n"
        "[4] Produto mais vendido\n"
        "[5] Listar\n"
        "[7] Sair\n"))
    except ValueError:
        print("Por favor, informe um valor válido!\n")
        continue

    if opcoes == 1:
        adicionar_produtos()
    elif opcoes == 2:
        remover_produto()
    elif opcoes == 3:
        produto_menos_vendido()
    elif opcoes == 4:
        produto_mais_vendido()
    elif opcoes == 5:
        listar_produtos()
    elif opcoes == 7:
        print("Finalizando o programa... Até logo!")
        break
    else:
        print("Opção inválida! Escolha uma opção de 1 a 7.")
