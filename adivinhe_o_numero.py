
import math
import random


def escolher_intervalo():
    intervalo_num = int(input("Escolha um intervalo entre 1 e 100 (1) e 1 e 1000 (2): "))
        
    if intervalo_num == 1:
        return 100
    elif intervalo_num == 2:
        return 1000
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")
        return escolher_intervalo()
    
    
    """
    Permite que o usuário escolha um intervalo para o número a ser adivinhado.
    Saída: O intervalo numérico escolhido (100 ou 1000).

    exemplo. se o jogador escolher 1 retorna 100. se o jogador escolher 2 retorna 1000.
    Caso o usuario digite um valor diferente, é impresso a mensagem `Escolha inválida. Por favor, digite 1 ou 2.`
    """
    return None

def definir_palpites(intervalo_num):
    palpites = 0

    if intervalo_num == 100:
        palpites = 7
    elif intervalo_num == 1000:
        palpites = 10
    else:
        return None

    return palpites
   
    """
    Define o número de palpites com base no intervalo escolhido.
    Entrada: Intervalo numérico (100 ou 1000).
    Saída: Número de palpites permitidos.

    Se o intervalo for 0 - 100 o jogador terá 7 palpites permitidos
    Se o intervalo for 0 - 1000 o jogador terá 10 palpites permitidos
    """

def gerar_numero_secreto(intervalo_num):
    if intervalo_num == 100:
        return random.randint(0, 100)
    elif intervalo_num == 1000:
        return random.randint(0, 1000)
    else:
        return None
    
    
    """
    Gera um número aleatório dentro do intervalo escolhido.
    Entrada: Intervalo numérico (100 ou 1000).
    Saída: Número aleatório gerado.

    esse numero secreto é gerado utilizando a função random do python, pesquise!
    """

def obter_palpite(intervalo_num):
    palpite = int(input("Digite o seu palpite: "))

    if intervalo_num == 100 and 1 <= palpite <= 100:
        return palpite
    elif intervalo_num == 1000 and 1 <= palpite <= 1000:
        return palpite
    else:
        print(f"Entrada inválida. Por favor, digite um número entre 1 e {intervalo_num}.")
        return obter_palpite(intervalo_num)
    

    """
    Permite que o usuário insira um palpite.
    Entrada: Intervalo numérico (100 ou 1000) para validar a entrada.
    Saída: Palpite numérico inserido pelo usuário.

    é permitido apenas valores numéricos, caso não seja um valor numero dentro do intervalo numerico
    o jogo exibe a mensagem `Entrada inválida. Por favor, digite um número entre 0 e {intervalo_num - 1}.`
    """

def avaliar_palpite(palpite, numero_secreto):
    if palpite > numero_secreto:
        return "Menor"
    elif palpite < numero_secreto:
        return "Maior"
    elif palpite == numero_secreto:
        return "Correto"
    else:
        return None

    
    
    
    """
    Avalia o palpite do usuário em relação ao número secreto.
    Entrada: Palpite do usuário e número secreto.
    Saída: Uma das três strings: "Maior", "Menor" ou "Correto".

    """
def jogar():
    while True:
        intervalo_num = escolher_intervalo()
        palpites = definir_palpites(intervalo_num)
        numero_secreto = gerar_numero_secreto(intervalo_num)

        while palpites > 0:
            palpite = obter_palpite(intervalo_num)
            resultado = avaliar_palpite(palpite, numero_secreto)

            if resultado == "Correto":
                print(f"Parabéns você acertou o número secreto, que era {numero_secreto}.")
                break
            else:
                palpites -= 1

                if palpites > 0:
                    print(f"Tente novamente. Dica: o número secreto é {resultado} que o seu palpite.")
                    print(f"Você tem {palpites} restantes.")
                else:
                    print(f"Seus palpites acabaram. O número secreto era {numero_secreto}.")
                    break  

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != 's':
            break


    """
    Função principal para orquestrar o fluxo do jogo.

 
    """


if __name__ == "__main__":
    jogar()
