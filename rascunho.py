"""

Planejador de cardápio 

Receber informações do usuário 
Quantas pessoas 
Qual proteína 
Quantas refeições 

Propor acompanhamento 
3 acompanhamentos por refeição 
Usuário escolhe quais
Gerar lista de compras
informar quantidade de proteína
Informar quantidade de outros

Mostrar receitas

Lista de proteínas
Lista de legumes
Lista de verduras
Lista de carbo A
Lista de carbo B
Fator de conversão 30% a mais no peso se tiver osso 

Definir combinações com aleatoriedade




12 a 18/04

Marmitas:
Seg. Carne moída
Ter. Frango
Qua. Omelete 
Qui. Frango
Sex. Peixe (feriado, todos em casa)

Refeições (Jantar):
Sab. Joelho (Almoço) picanha (jantar)
Dom. Carne de porco (almoço)
Seg. Carne de porco
Ter. Sopa Canjiquinha com costelinha 
Qua. Frango
Qui. Nhoque 
Sex. Pipoca 

Legumes:
Arroz
Feijão 
Abóbora 
Cenoura 
Abobrinha 
Beterraba 


"""

"""
proteinas = {
    "frango": {"tem_osso": True, "quantidade_por_pessoa": 150},
    "frango sem osso": {"tem_osso": False, "quantidade_por_pessoa": 125},
    "carne": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "ovo": {"tem_osso": False, "quantidade_por_pessoa": 2},
    "peixe": {"tem_osso": True, "quantidade_por_pessoa": 180},
    "carne de porco": {"tem_osso": False, "quantidade_pot_pessoa": 125}
}
carboidrato = {"feijão", "grão de bico", "lentilha", "quinua"}

vegetal_a1 = {"abobrinha", "beringela", "maxixe", "nirá", "cebola", "cogumelos", 
              "couve-flor", "palmito", "pepino", "pimentão", "rabanete", "tomate"}
 
vegetal_a2 = {"agrião", "aipo", "alface", "almeirão", "bertalha", "brócolis", "chicória", "couve", 
             "espinafre", "repolho", "rúcula", "taioba"}

vegetal_a2 = {"folhas", "acelga", "couve-de-bruxelas", "escarola"}

vegetal_b = {"abóbora", "beterraba", "cenoura", "chuchu", "ervilha fresca", "nabo", "quiabo", "vagem"}

Perguntar se eu quero um cardápio semanal ou apenas uma refeição

Semanal:
    Pedir para eu escolher 3 proteínas de uma lista numerada
    perguntar quantas pessoas vão comer
    perguntar se é somente almoço
    perguntar se vou fazer marmitas e para quantas pessoas
uma refeição:
    pedir para eu escolher uma proteína de uma lista numerada
    perguntar quantas pessoas vão comer

sugerir oções de acompanhamento para as proteínas, considerando como
o usuário vai aproventar melhor o tempo e as combinações

indicar como distribuir as refeições durante a semana, entre jantar e marmitas

indicar as quantidades de cada item

por exemplo, 1 x de arroz serve 4 marmitas ou 5 pratos
1 porção de proteína sem osso = 125 g cru.



"""