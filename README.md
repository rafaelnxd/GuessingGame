Jogo da Adivinhação
===================

Descrição
---------

Este é um simples jogo da adivinhação em Python, onde o jogador deve tentar adivinhar um número secreto gerado aleatoriamente dentro de um intervalo escolhido.

Funcionalidades
---------------

### `escolher_intervalo()`

Permite que o usuário escolha um intervalo para o número a ser adivinhado (100 ou 1000).

-   Saída: O intervalo numérico escolhido.

### `definir_palpites(intervalo_num)`

Define o número de palpites com base no intervalo escolhido.

-   Entrada: Intervalo numérico (100 ou 1000).
-   Saída: Número de palpites permitidos.

### `gerar_numero_secreto(intervalo_num)`

Gera um número aleatório dentro do intervalo escolhido.

-   Entrada: Intervalo numérico (100 ou 1000).
-   Saída: Número aleatório gerado.

### `obter_palpite(intervalo_num)`

Permite que o usuário insira um palpite.

-   Entrada: Intervalo numérico (100 ou 1000) para validar a entrada.
-   Saída: Palpite numérico inserido pelo usuário.

### `avaliar_palpite(palpite, numero_secreto)`

Avalia o palpite do usuário em relação ao número secreto.

-   Entrada: Palpite do usuário e número secreto.
-   Saída: Uma das três strings: "Maior", "Menor" ou "Correto".

### `jogar()`

Função principal para orquestrar o fluxo do jogo. Permite ao jogador tentar adivinhar o número secreto dentro do limite de palpites. Oferece dicas sobre se o palpite é maior, menor ou correto.

Instruções de Uso
-----------------

1.  Clone o repositório.
2.  Execute o código em um ambiente Python.
3.  Escolha um intervalo (1 para 0-100, 2 para 0-1000).
4.  Insira seus palpites.
5.  Receba dicas sobre se o número secreto é maior, menor ou se você acertou.
6.  O jogo informa se você acertou ou ficou sem palpites.
7.  Pode jogar novamente se desejar.

Divirta-se adivinhando! 🎉
