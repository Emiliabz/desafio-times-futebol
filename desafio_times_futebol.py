"""
DESAFIO: Tuplas com Times de Futebol
-------------------------------------------------------------------------
Enunciado:
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:

A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.

Destaques:
- Uso de fatiamento de tuplas (Slicing).
- Método index() para localizar itens.
- Função sorted() para ordenação temporária.
-------------------------------------------------------------------------
"""

VERDE = '\033[32m'
LARANJA = '\033[33m'
AMARELO = '\033[93m'
AZUL = '\033[34m'
ROXO_PRETO = '\033[45;30m'
RESET = '\033[m'

times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
         'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
         'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
         'Bahia', 'Santos', 'Goiás', 'Coritiba', 'Chapecoense')

print(f'{AMARELO}-=' * 50)
print(f'LISTA DE TIMES: {times}')
print(f'-=' * 50 + RESET)


print(f'- Os 5 primeiros são: {VERDE}{times[0:5]}{RESET}')


print(f'- Os 4 últimos são: {LARANJA}{times[-4:]}{RESET}')


print(f'- Times em ordem alfabética: {AZUL}{sorted(times)}{RESET}')


pos = times.index('Chapecoense') + 1
print(f'A Chapecoense está na {ROXO_PRETO} {pos}ª posição {RESET}')