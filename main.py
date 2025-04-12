import random

# --- Dados básicos (simulados) ---
proteinas = {
    "frango": {"tem_osso": True, "quantidade_por_pessoa": 200},
    "carne": {"tem_osso": False, "quantidade_por_pessoa": 150},
    "ovo": {"tem_osso": False, "quantidade_por_pessoa": 2},
    "peixe": {"tem_osso": True, "quantidade_por_pessoa": 180},
}

acompanhamentos = ["arroz", "feijão", "salada", "batata", "legumes", "purê", "macarrão"]

# --- Entrada do usuário ---
pessoas = int(input("Quantas pessoas vão comer? "))
refeicoes = int(input("Quantas refeições deseja planejar? "))

print("\nOpções de proteína disponíveis:")
for prot in proteinas:
    print(f"- {prot}")

proteinas_escolhidas = input("\nDigite as proteínas preferidas separadas por vírgula: ").lower().split(',')
proteinas_escolhidas = [p.strip() for p in proteinas_escolhidas if p.strip() in proteinas]

# --- Geração do cardápio ---
cardapio = []

for i in range(refeicoes):
    proteina = random.choice(proteinas_escolhidas)
    acompanh = random.sample(acompanhamentos, 3)
    cardapio.append({"refeicao": i+1, "proteina": proteina, "acompanhamentos": acompanh})

# --- Mostrar o cardápio ---
print("\n=== Cardápio Gerado ===")
for item in cardapio:
    print(f"Refeição {item['refeicao']}: {item['proteina'].capitalize()} com {', '.join(item['acompanhamentos'])}")

# --- Calcular lista de compras ---
compras = {}

for item in cardapio:
    prot = item["proteina"]
    dados = proteinas[prot]
    
    quantidade = dados["quantidade_por_pessoa"] * pessoas
    if dados["tem_osso"]:
        quantidade *= 1.3  # fator de correção para osso

    compras[prot] = compras.get(prot, 0) + quantidade

    for a in item["acompanhamentos"]:
        compras[a] = compras.get(a, 0) + 1 * pessoas  # 1 porção por pessoa

# --- Mostrar lista de compras ---
print("\n=== Lista de Compras ===")
for item, qtd in compras.items():
    unidade = "unid." if isinstance(qtd, int) and qtd < 10 else "g" if isinstance(qtd, float) else "porções"
    print(f"- {item.capitalize()}: {round(qtd)} {unidade}")
