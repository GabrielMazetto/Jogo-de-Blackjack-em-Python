import random


class Card:
    """Representa uma carta padrao do jogo."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Ouros', 'Espadas', 'Copas', 'Paus']
    rank_names = [None, 'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Dama', 'Valete', 'Rei']
   
    def __str__(self):
        """Retorna uma representacao em string das cartas."""
        return '%s de %s' %(Card.rank_names[self.rank],
                            Card.suit_names[self.suit])

    def __eq__(self, other):
        """Checa se duas cartas (self e other) possuem o mesmo rank (valor).
        retorna: booleano
        """
        return self.rank == other.rank 
    
    def __lt__(self, other):
        """Compara a carta (self) com outra (other) e verifica se a primeira e menor que a segunda.
        retorna: booleano
        """
        t1 = self.rank   
        t2 = other.rank  
        return t1 < t2

    def __add__(self, other):
        """Permite a soma de duas cartas, retornando o rank total.
        retorna: inteiro
        """
        c1 = self.rank
        c2 = other.rank
        return c1 + c2

class Deck:
    """Representa um deck padrao de cartas.
    Attributes:
      cards: lista de objetos Card.
    """
    def __init__(self):
        """Inicializa o Deck com 52 cartas.
        """
        self.cards = []
        for suit in range(4):
            for rank in range (1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        """Retorna uma representacao em string do Deck.
        """
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, i=-1):
        """Remove e retorna uma carta do deck.
        i: indice da carta a ser removida; por padrao, remove a ultima carta.
        """
        return self.cards.pop(i)

    def add_card(self, card):
        """Adiciona uma carta ao deck.
        card: Card
        """
        self.cards.append(card)

    def remove_card(self, card):
        """Remove uma carta do deck.
        
        card: Card
        """
        self.cards.remove(card)

    def shuffle(self):
        """Embaralha as cartas do deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Organiza as cartas em ordem crecente."""
        self.cards.sort()
     
    def move_cards(self, hand, num):
        """Move o numero dado de cartas do deck para a Hand.
        hand: objeto Hand de destino das cartas
        num: numero inteiro de cartas a serem movidas
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    
class Hand(Deck):
    """Representa a mao de cartas de cada jogador."""

    def __init__(self, label=''):
        """A Hand se inicializa vazia.
        """
        self.cards = [] 
        self.label = label 

    def sum_total(self):
        """Soma os valores das cartas e retorna o total.
        """
        carta = self.cards
        total = 0
        for card in self.cards:
            valor = card.rank
            if valor == 11 or valor == 12 or valor == 13:
                valor = 10
            if valor == 1:
                if total < 11:
                    valor = 11
            total = total + valor
        return total


def pegar_jogadores():
    """Retorna a lista de jogadores da partida.
    """
    quantidade = input("Quantos Jogadores? ")
    quantidade = int(quantidade)
    while quantidade > 6 or quantidade <= 1:
        quantidade = input("O numero digitado e invalido. Por favor, digite um numero entre 2 e 6: ")
        quantidade = int(quantidade)
    jogador = []
    print('')

    for indice in range(0, quantidade):
        nome_jogador = input('Qual o nome do jogador %d? ' %(indice+1))
        jogador.append(nome_jogador)

    return jogador    


def distribuir_cartas():
        """Inicializa o jogo movendo duas cartas do deck para a mao de cada jogador.
        """
        hand = 0
        while hand<len(jogadores):
                baralho.move_cards(hands[hand], 2)
                print('\nCartas do jogador %s:' %jogadores[hand])
                print('Pontuacao: %s' %pontuacao[hand])
                print(hands[hand])
                soma_cartas = soma(hand)
                print('Soma: %d\n' %soma_cartas)
                hand = hand+1

def dar_aposta_obrigatoria():
    """Retira da pontuacao de cada jogador participante a aopsta obrigatoria.
    """
    for indice in range(0, len(pontuacao)):
        pontuacao[indice] -= aposta_obrigatoria

def soma(indice):
        """Retorna a soma das cartas de uma mao, referenciada pelo indice da lista de maos.
        """
        soma = hands[indice].sum_total()
        return soma


def deletar():
    """Apos o termino da partida, as cartas de cada mao retornam ao deck.
    Caso o jogador nao tenha a pontuacao necessaria para participar, ele sera retirado do jogo.
    """
    for hand in hands:
        tamanho = len(hand.cards)
        hand.move_cards(baralho, tamanho)
    i = 0
    for pontos in pontuacao:
        if pontos < aposta_obrigatoria:
              del pontuacao[i]
              del hands[i]
              del jogadores[i]
        if i < len(jogadores)-1:
            i += 1

def criar_pontuacao(n_jogadores):
        """Inicializa a pontuacao dos jogadores.
        """
        pontuacao = []
        for indice in range(0, n_jogadores):
            pontuacao.append(1000)
        return pontuacao

def criar_mao(n):
    hands = []
    for hand in range(0, n):
        hand = Hand()
        hands.append(hand)
    return hands

def partida():
        """Representa uma unica partida do jogo.
        """
        vez = 0
        rodada = 1
        max_rodadas = 2
        total_aposta = aposta_obrigatoria*len(jogadores)
        perdedor = 0
        somas = []
        while True:
            print('\nVez do jogador %s:\n' % jogadores[vez])
            soma_cartas = soma(vez)
            if rodada == max_rodadas:
                somas.append(soma_cartas)
            if soma_cartas > 21:
                print('Que pena, voce perdeu')          
            else:   
                if rodada > max_rodadas:
                    #se forem todas as rodadas
                    maior_soma = max(somas)
                    c = 0   
                    n_vencedores = 0
                    for vencedor in somas:
                        if maior_soma <= 21:
                            if vencedor == maior_soma:
                                n_vencedores += 1
                    for vencedor in somas:
                        if maior_soma <= 21:
                            if vencedor == maior_soma:
                                pontuacao[c] += int(total_aposta/n_vencedores)
                                print('A partida acabou!!\nParabens %s, Voce ganhou %d pontos!!' % (jogadores[c], int(total_aposta/n_vencedores))) 
                        c += 1
                    break 
                if perdedor == n_jogadores-1:
                    #se todos menos 1 perderem antes do limite de rodadas
                    pontuacao[vez] += total_aposta
                    print('A partida acabou!!\nParabens %s, Voce ganhou %d pontos!!' % (jogadores[vez], total_aposta)) 
                    break
                if soma_cartas == 21:
                    print('Voce ja tem 21!')
                if pontuacao[vez] < custo:
                    if soma_cartas != 21:
                    #se o jogador nao tiver pontuacao suficiente
                        print('Voce nao tem pontos suficientes para comprar uma carta')
                        print('Pontuacao: %d' % pontuacao[vez])
                        print('Suas cartas:\n%s' %hands[vez])
                        soma_cartas = soma(vez)
                        print('Soma: %d\n' %soma_cartas)
                        if soma_cartas > 21:
                            print('Que pena, voce perdeu')
                            perdedor += 1
                else:
                    if soma_cartas != 21:
                        resposta = input('Digite C para comprar uma carta (%d), P para passar e D para dobrar (%d): ' % (custo, custo*2))
                        resposta = resposta.upper()
                        resposta_valida = ['C', 'P', 'D']
                        while resposta not in resposta_valida:
                            resposta = input('Resposta invalida. Digite novamente: ')
                            resposta = resposta.upper()
                        if resposta == 'C':
                            pontuacao[vez] -= custo
                            baralho.move_cards(hands[vez], 1)
                            print('Pontuacao: %d' % pontuacao[vez])
                            print('Suas cartas:\n%s' %hands[vez])
                            soma_cartas = soma(vez)
                            print('Soma: %d\n' %soma_cartas)
                            if soma_cartas > 21:
                                print('Que pena, voce perdeu')
                                perdedor += 1
                            if soma_cartas == 21:
                                print('Uau! Voce tem um Blackjack')
                            total_aposta += custo
                        if resposta == 'P':
                            print('%s passou!' %jogadores[vez])
                        if resposta == 'D':
                            pontuacao[vez] -= custo*2
                            baralho.move_cards(hands[vez], 1)
                            print('Pontuacao: %d' % pontuacao[vez])
                            print('Suas cartas sao:\n%s' %hands[vez])
                            soma_cartas = soma(vez)
                            print('Soma: %d\n' %soma_cartas)
                            if soma_cartas > 21:
                                print('Que pena, voce perdeu')
                                perdedor += 1
                            if soma_cartas == 21:
                                print('Uau! Voce tem um Blackjack')
                            total_aposta += custo*2
            vez += 1
            if vez == len(jogadores):
                vez = 0
                rodada += 1

                    

print('BEM VINDO AO 21 DO GABRIEL!!\n\n')
print("""Este jogo tem um numero maximo de 6 jogadores em que cada um deles comeca com 1000 pontos.
Para comecar  jogo, os jogadores precisam dar uma aposta inicial que cresce ao longo das partidas.
O jogador que ficar sem pontos sera eliminado e ganha aquele que sobreviver ate o final.
QUE COMECEM OS JOGOS!!\n\n""")

baralho = Deck()
baralho.shuffle()

jogar_novamente = input('\nGostariam de jogar uma partida? Digite S para jogar: ')
jogar_novamente = jogar_novamente.upper()

while jogar_novamente == 'S':
    hands = criar_mao(6)
    jogadores = pegar_jogadores()
    n_jogadores = len(jogadores)
    pontuacao = criar_pontuacao(n_jogadores)
    custo = 50
    aposta_obrigatoria = 25
    n_rodadas = 0
    while len(jogadores) > 1:
        print('\nA aposta inicial e de: %d' %aposta_obrigatoria)
        baralho.shuffle()
        dar_aposta_obrigatoria()
        distribuir_cartas()
        partida()
        deletar()
        n_jogadores = len(jogadores)
        n_rodadas += 1
        if 300 > aposta_obrigatoria >= 100:
            aposta_obrigatoria += 50
        elif aposta_obrigatoria >= 300:
            if n_rodadas % 2 == 0:
                aposta_obrigatoria += 150
        elif n_rodadas % 3 == 0:
            custo += 50
            aposta_obrigatoria += 25
    print('\nO JOGO ACABOU! %s GANHOU!!!' % jogadores[0].upper())
    print('Voce terminou com %d pontos\n' %pontuacao[0])
    jogar_novamente = input('Gostariam de jogar uma partida? Digite S para jogar: ')
    jogar_novamente = jogar_novamente.upper()
       
print('\n\nOBRIGADO POR JOGAR!!')