import random

# Dados base
proteinas = {
    "frango": {"tem_osso": True, "quantidade_por_pessoa": 150},
    "frango sem osso": {"tem_osso": False, "quantidade_por_pessoa": 125},
    "carne": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "ovo": {"tem_osso": False, "quantidade_por_pessoa": 2},
    "peixe": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "carne de porco": {"tem_osso": False, "quantidade_por_pessoa": 125}
}

carboidrato = ["feijão", "arroz", "arroz integral", "macarrão", "grão de bico", "lentilha", "quinua"]
vegetal_a1 = ["abobrinha", "beringela", "maxixe", "nirá", "cebola", "cogumelos", 
              "couve-flor", "palmito", "pepino", "pimentão", "rabanete", "tomate"]
vegetal_a2 = ["agrião", "aipo", "alface", "almeirão", "bertalha", "brócolis", "chicória", 
              "couve", "espinafre", "repolho", "rúcula", "taioba", "folhas", 
              "acelga", "couve-de-bruxelas", "escarola"]
vegetal_b = ["abóbora", "beterraba", "cenoura", "chuchu", "ervilha fresca", "nabo", "quiabo", "vagem"]

# Mostrar lista numerada de proteínas
def listar_proteinas():
    print("\nEscolha as proteínas:")
    for i, prot in enumerate(proteinas.keys(), 1):
        print(f"{i}. {prot}")

def escolher_proteinas(qtd):
    listar_proteinas()
    escolhidas = []
    while len(escolhidas) < qtd:
        escolha = int(input(f"Escolha a proteína {len(escolhidas)+1}: ")) - 1
        prot_lista = list(proteinas.keys())
        if 0 <= escolha < len(prot_lista):
            prot_nome = prot_lista[escolha]
            if prot_nome not in escolhidas:
                escolhidas.append(prot_nome)
            else:
                print("Você já escolheu essa proteína.")
        else:
            print("Escolha inválida.")
    return escolhidas

# Calcular proteína considerando osso
def calcular_proteina(nome, pessoas):
    dados = proteinas[nome]
    qtd = dados["quantidade_por_pessoa"] * pessoas
    if dados["tem_osso"]:
        qtd *= 1.3
    return round(qtd)

# Sugerir acompanhamentos aleatórios por enquanto
def sugerir_acompanhamentos():
    return [
        random.choice(carboidrato),
        random.choice(vegetal_a1),
        random.choice(vegetal_a2),
        random.choice(vegetal_b)
    ]

# Planejamento semanal
def planejar_semanal():
    print("\n== PLANEJAMENTO SEMANAL ==")
    proteinas_semana = escolher_proteinas(3)
    pessoas = int(input("Quantas pessoas vão comer no almoço? "))
    so_almoco = input("Vai precisar fazer marmitas? (s/n): ").lower() == 's'
    marmitas = 0
    if so_almoco:
        marmitas = int(input("Quantas pessoas vão receber marmitas? "))

    total_refeicoes = 5  # de segunda a sexta
    total_pessoas = pessoas + marmitas

    cardapio = []
    compras = {}

    for i in range(total_refeicoes):
        prot = proteinas_semana[i % len(proteinas_semana)]
        acomp = sugerir_acompanhamentos()
        cardapio.append((prot, acomp))

        # Adiciona proteína à lista de compras
        qtd_prot = calcular_proteina(prot, total_pessoas)
        compras[prot] = compras.get(prot, 0) + qtd_prot

        # Adiciona acompanhamentos
        for a in acomp:
            compras[a] = compras.get(a, 0) + total_pessoas

    # Exibe o cardápio
    print("\nCardápio da semana:")
    dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
    for i, (prot, acomp) in enumerate(cardapio):
        print(f"{dias[i]}: {prot} com {', '.join(acomp)}")

    # Exibe lista de compras
    print("\nLista de compras (estimativa):")
    for item, qtd in compras.items():
        if item in proteinas:
            print(f"- {item}: {qtd}g")
        else:
            porcao_ref = "porções (1 por pessoa/refeição)"
            print(f"- {item}: {qtd} {porcao_ref}")

# Planejar uma refeição simples
def planejar_uma_refeicao():
    print("\n== PLANEJAMENTO DE UMA REFEIÇÃO ==")
    prot = escolher_proteinas(1)[0]
    pessoas = int(input("Quantas pessoas vão comer? "))
    acomp = sugerir_acompanhamentos()

    print(f"\nRefeição sugerida: {prot} com {', '.join(acomp)}")
    print("\nQuantidade necessária:")
    print(f"- {prot}: {calcular_proteina(prot, pessoas)}g")
    for a in acomp:
        print(f"- {a}: {pessoas} porções")

# Menu principal
def menu():
    print("Bem-vindo ao Planejador de Cardápio!")
    tipo = input("Você quer um cardápio semanal (s) ou apenas uma refeição (r)? ").lower()

    if tipo == 's':
        planejar_semanal()
    elif tipo == 'r':
        planejar_uma_refeicao()
    else:
        print("Opção inválida. Tente novamente.")

menu()
