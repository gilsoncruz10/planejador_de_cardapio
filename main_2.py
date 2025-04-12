import random

# --- Dados básicos (simulados) ---
proteinas = {
    "frango": {"tem_osso": True, "quantidade_por_pessoa": 150},
    "frango sem osso": {"tem_osso": False, "quantidade_por_pessoa": 125},
    "carne": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "ovo": {"tem_osso": False, "quantidade_por_pessoa": 2},
    "peixe": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "carne de porco": {"tem_osso": False, "quantidade_pot_pessoa": 125}
}
carboidrato = {"feijão", "grão de bico", "lentilha", "quinua"}

#vegetal_a = {"folhas", "abobrinha", "acelga", "agrião", "aipo", "alface", "almeirão", 
#             "aspargos", "beringela", "bertalha", "brócolis", "chicória", "couve", 
#             "couve-de-bruxelas", "escarola", "espinafre", "maxixe", "nirá", "repolho", 
#             "rúcula", "taioba", "cebola", "cogumelos", "couve-flor", "palmito", "pepino", 
#             "pimentão", "rabanete", "tomate"}

vegetal_a1 = {"abobrinha", "beringela", "maxixe", "nirá", "cebola", "cogumelos", 
              "couve-flor", "palmito", "pepino", "pimentão", "rabanete", "tomate"}
 
vegetal_a2 = {"agrião", "aipo", "alface", "almeirão", "bertalha", "brócolis", "chicória", "couve", 
             "espinafre", "repolho", "rúcula", "taioba"}

vegetal_a2 = {"folhas", "acelga", "couve-de-bruxelas", "escarola"}

vegetal_b = {"abóbora", "beterraba", "cenoura", "chuchu", "ervilha fresca", "nabo", "quiabo", "vagem"}

acompanhamentos = ["arroz", "feijão", "salada", "batata", "legumes", "purê", "macarrão"]

"""
segunda = proteinas[0]
terca = proteinas[0]
quarta = proteinas[0]
quinta = proteinas[0]
sexta = proteinas[0]
"""

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
