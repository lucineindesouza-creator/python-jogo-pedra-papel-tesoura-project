"""
Projeto: Jogo de Pedra, Papel e Tesoura
Autor: Lucinei Neris
Versão: 1.0.0
Data de criação: 11/07/2026
Descrição: Aplicação em Python que implementa o clássico jogo Pedra, Papel e Tesoura em modo texto, permitindo partidas entre o usuário e o 
computador com placar acumulado e validação de entradas.
Licença: MIT License
"""

# Importando bibliotecas necessárias
import random

# Informações do jogo e regras do jogo
print("=" * 45)
print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
print("Regras do jogo:")
print("- Pedra ganha de Tesoura")
print("- Tesoura ganha de Papel")
print("- Papel ganha de Pedra")
print("=" * 45)


# Opções do jogo
OPCOES = ("pedra", "papel", "tesoura")
print(f"Faça sua escolha entre: {OPCOES}\n")

# Placar inicial
placar_usuario = 0
placar_computador = 0
placar_empate = 0

jogar_novamente = "sim"

# Loop principal do jogo
while jogar_novamente.lower() == "sim":
    print("Novo round! Placar atual:")
    print("=" * 45)
    print(f"Usuário: {placar_usuario}")
    print(f"Computador: {placar_computador}")
    print(f"Empates: {placar_empate}")
    print("=" * 45)

    # Entrada do usuário
    escolha_usuario = input("Escolha sua jogada: ").lower().strip()

    # Validação da entrada do usuário
    if escolha_usuario not in OPCOES:
        print("Escolha inválida! Use somente as opções disponíveis.\n")
        continue
    
    # Impressão da escolha do usuário
    print(f"\nVocê escolheu: {escolha_usuario}")

    # Escolha aleatória do computador
    escolha_computador = random.choice(OPCOES)
    print(f"Computador escolheu: {escolha_computador}")

    # Determinando o vencedor e a lógica do jogo
    if escolha_usuario == escolha_computador:
        print("Resultado: Empate!\n")
        placar_empate += 1
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra"):
        print("Resultado: Você venceu. Parabéns!\n")
        placar_usuario += 1
    else:
        print("Resultado: O Computador venceu!\n")
        placar_computador += 1

    # Perguntando se o usuário quer jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower().strip()

    # Validação da resposta do usuário
    while jogar_novamente not in ["sim", "não", "nao"]:
        print("Resposta inválida! Por favor, responda com 'sim' ou 'não'.")
        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower().strip()

# Finalização do jogo e exibição do placar final
print("\nObrigado por jogar! Placar final:")
print("=" * 45)
print(f"Vitórias do Usuário: {placar_usuario}")
print(f"Vitórias do Computador: {placar_computador}")
print(f"Empates: {placar_empate}")
print("=" * 45)