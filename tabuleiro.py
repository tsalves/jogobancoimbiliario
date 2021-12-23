import random
from jogadorimpulsivo import Impulsivo
from jogadoraleatorio import Aleatorio
from jogadorexigente import Exigente
from jogadorcauteloso import Cauteloso
from propriedade import Propriedade

class Tabuleiro:

    def __init__(self):

        self.vencedor = None
        self.propriedades = [
            Propriedade('Taubaté', 400, 100),
            Propriedade('Holambra', 200, 50),
            Propriedade('Itapevi', 150, 40),
            Propriedade('Alphaville', 220, 55),
            Propriedade('Guaianases', 180, 50),
            Propriedade('Osasco', 300, 80),
            Propriedade('Diadema', 350, 85),
            Propriedade('Araçariguama', 180, 50),
            Propriedade('Silveira', 600, 150),
            Propriedade('Itaquera', 250, 60),
            Propriedade('Linhaes', 190, 52),
            Propriedade('Votorantim', 300, 80),
            Propriedade('Araçatuba', 120, 30),
            Propriedade('Araraquara', 100, 20),
            Propriedade('Lins', 200, 50),
            Propriedade('Vila Velha', 450, 130),
            Propriedade('Esperantina', 400, 200),
            Propriedade('Santa Cecilia', 320, 90),
            Propriedade('Paulista', 300, 100),
            Propriedade('Yamauchi', 400, 95)
        ]

        self.jogadores = [
            Impulsivo('Impulsivo'),
            Aleatorio('Aleatorio'),
            Exigente('Exigente'),
            Cauteloso('Cauteloso')
        ]

    def iniciar(self, resultado = None):

        jogadores = 4
        ativo = None
        for rodada in range(0, 999):
            if ativo == None:
                break

            for vezDoJogador in filter(lambda jogador: not jogador.estaFalido(), self.jogadores):
                posicao = self.__rodarDado()
                vezDoJogador.pularPosicao(posicao, len(self.propriedades))
                propriedade = self.propriedades[vezDoJogador.posicao]
                if self.temQuePagarAluguel(propriedade, vezDoJogador):
                    self.pagarAluguel(propriedade, vezDoJogador)

                elif vezDoJogador.deveComprar(propriedade):
                    self.comprarPropriedade(propriedade, vezDoJogador)

                if vezDoJogador.estaFalido():
                    self.removerAsPropriedades(vezDoJogador)
                    jogadores -= 1

            if jogadores == 1:
                for jogador in self.jogadores:
                    if not jogador.estaFalido():
                        resultado.setGanhadores(str(jogador.nome).lower())
                        resultado.setRodadas(int(rodada + 1))
                        ativo = None
        
        if rodada == 999:
            resultado.setTimeouts(1)
            resultado.setRodadas(rodada + 1)
            self.vencedor = self.obterJogadorComMaiorSaldo()

    def obterJogadorComMaiorSaldo(self):
        return max(self.jogadores, key=lambda jogador: jogador.saldo)

    def removerAsPropriedades(self, vezDoJogador):
        propriedadesDoJogador = filter(lambda propriedade: propriedade.pertence(vezDoJogador), self.propriedades)
        for propriedade in propriedadesDoJogador:
            propriedade.proprietario = None

    def temQuePagarAluguel(self, propriedade, vezDoJogador):
        return propriedade.estaVendida() and propriedade.proprietario != vezDoJogador
    
    def comprarPropriedade(self, propriedade, vezDoJogador):
        propriedade.proprietario = vezDoJogador
        vezDoJogador.saldo -= propriedade.valorDaVenda

    def __rodarDado(self):
        return random.randint(1, 6)
    
    def pagarAluguel(self, propriedade, vezDoJogador):
        vezDoJogador.saldo -= propriedade.valorDoAluguel
        proprietario = self.obterJogador(propriedade.proprietario.nome)
        proprietario.saldo += propriedade.valorDoAluguel

    def obterJogador(self, nome):
        return next(jogador for jogador in self.jogadores if jogador.nome == nome)
    
