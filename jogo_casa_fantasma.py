import random

# Códigos de cores ANSI
VERDE = '\033[92m'
AZUL = '\033[94m'
VERMELHO = '\033[91m'
NEGRITO = '\033[1m'
RESET = '\033[0m'  # Resetar a cor para o padrão

# Título centralizado da Casa Fantasma
titulo = "BEM-VINDO À CASA FANTASMA!"
print(f"{VERMELHO}{NEGRITO}{titulo.center(80)}{RESET}")

# Logo da Universidade de Vassouras e desenho da Casa Fantasma em ASCII lado a lado
logo_universidade = """
    UNIVERSIDADE
     DE VASSOURAS
     _____________
    |             |
    |   VASSOURAS |
    |_____________|
"""
casa_fantasma = """
            .     .
       .  |\\-^-/|  .      
         /| o o |\\        
        / \\  Y  / \\      
   .   (  \\ \\_/ /  )   .
      /\\ \\-^-/ /\\
     /  \\| \\_/ |/  \\
    /    \\_____/    \\
   /_  |/       \\|  _\\
   |    |       |    |
   |    |       |    |
   |____|_______|____|
"""

# Imprimindo o logo e o desenho da casa lado a lado
for line_logo, line_casa in zip(logo_universidade.splitlines(), casa_fantasma.splitlines()):
    print(f"{line_logo:<20} {line_casa}")

# Adicionando duas linhas de espaço antes da escolha dos personagens
print("\n\nVocê precisa escolher um personagem para jogar:")
print("1 - Fred")
print("2 - Robert")
print("3 - John")
print("4 - Joana")

personagem = input("Digite o número do personagem escolhido: ")

if personagem == "1":
    nome_personagem = "Fred"
    descricao_final = "Fred é apenas um civil que foi capturado aleatoriamente por um psicopata anônimo."
    descricao_game_over = "Fred nunca foi encontrado novamente."
elif personagem == "2":
    nome_personagem = "Robert"
    descricao_final = "Robert é um policial que estava na rua e do nada foi capturado por um psicopata anônimo."
    descricao_game_over = "Robert tentou escapar, mas acabou preso para sempre no local."
elif personagem == "3":
    nome_personagem = "John"
    descricao_final = "John é um morador de rua que foi capturado por um psicopata anônimo. Quando escapou e correu para a rua, fatalmente foi atropelado e veio a falecer."
    descricao_game_over = "John desapareceu sem deixar rastros."
elif personagem == "4":
    nome_personagem = "Joana"
    descricao_final = "Joana é uma prostituta que foi capturada por um psicopata anônimo."
    descricao_game_over = "Joana não conseguiu escapar de seu destino sombrio."
else:
    print("Escolha inválida. Encerrando o jogo.")
    exit()

print(f"\nVocê escolheu {nome_personagem}. Boa sorte!\n")

# Variáveis iniciais
chaves = [False, False, False]  # Chaves dos quartos
jogador_vida = 50
boss_vida = 50
escapou = False

# Desafio do Quarto 1 - Múltiplos de 5
while not chaves[0]:
    print(VERDE + "Quarto 1: Para pegar a chave, você precisa falar 3 números múltiplos de 5." + RESET)
    numeros = input("Digite 3 números múltiplos de 5 separados por espaço: ").split()
    
    if all(int(num) % 5 == 0 for num in numeros) and len(numeros) == 3:
        print("Correto! Você pegou a chave do Quarto 1.\n")
        chaves[0] = True
    else:
        print("Resposta incorreta. Tente novamente.\n")

# Desafio do Quarto 2 - Ano Bissexto
while not chaves[1]:
    print(AZUL + "Quarto 2: Para pegar a chave, você precisa dizer um ano bissexto." + RESET)
    ano = int(input("Digite um ano: "))
    
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Correto! Você pegou a chave do Quarto 2.\n")
        chaves[1] = True
    else:
        print("Resposta incorreta. Tente novamente.\n")

# Desenho do Fantasma em ASCII no Quarto 3
fantasma = """
       .-.
      (o o) Boo!
       | O \\
        \\   \\
         `~~~'
"""

# Desenhos para eventos de dano
boneco_com_espada = """
       O
      /|\\    Você acerta o Boss!
      / \\
"""

caveira_rindo = """
      .-.
     (o o)   Hahaha!
      |=|
     __|__
"""

# Desafio do Quarto 3 - Combate contra o Boss
if not chaves[2]:
    print(fantasma)
    print(VERMELHO + "Quarto 3: Você encontrou o Boss! Prepare-se para lutar!\n" + RESET)
    
    while jogador_vida > 0 and boss_vida > 0:
        input("Pressione Enter para jogar o dado...")
        dado = random.randint(1, 6)
        print(f"Você rolou um {dado}!")

        if dado % 2 == 0:
            boss_vida -= 10
            print(VERMELHO + boneco_com_espada + RESET)
        else:
            jogador_vida -= 10
            print(VERMELHO + caveira_rindo + RESET)

        print(f"Vida do Jogador: {jogador_vida} | Vida do Boss: {boss_vida}\n")

    if jogador_vida > 0:
        print("Parabéns! Você derrotou o Boss e pegou a última chave!\n")
        chaves[2] = True
    else:
        # Desenho da Caveira em ASCII
        caveira = """
             _______
            /       \\
           /         \\
          / /       \\ \\
          ||         ||
          ||  RIP    ||
          ||         ||
          ||         ||
        ^^^^^^^^^^^^^^^^^
        """
        print(caveira)
        print("Você foi derrotado pelo Boss. Game Over.\n")
        print(descricao_game_over)

        # Informações do projeto após o Game Over
        print("\nMatéria: PENSAMENTO COMPUTACIONAL")
        print("Equipe do projeto:")
        print("Bruno Macedo da Silva")
        print("Elder Faber Faria Coelho")
        print("Gabriel Nogueira Reis")
        print("João Pedro Oliveira")
        print("Lucas da Silva Alves")
        print("Thiago Ferreira Maia")
        print("Wenderson Luís dos Santos")
        print("Yuri Pereira")

        exit()

# Verificação das chaves e conclusão
if all(chaves):
    print("Parabéns! Você encontrou todas as chaves e escapou da Casa Fantasma!\n")
    print(descricao_final)

    # Informações do projeto ao escapar
    print("\nMatéria: PENSAMENTO COMPUTACIONAL")
    print("Equipe do projeto:")
    print("Bruno Macedo da Silva")
    print("Elder Faber Faria Coelho")
    print("Gabriel Nogueira Reis")
    print("João Pedro Oliveira")
    print("Lucas da Silva Alves")
    print("Thiago Ferreira Maia")
    print("Wenderson Luís dos Santos")
    print("Yuri Pereira")
