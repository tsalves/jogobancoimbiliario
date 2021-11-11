class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 300
        self.posicao = 0

    def temSaldoPositivo(self):
        return self.saldo > 0
    
    def pularPosicao(self, posicao, quantidadeDePropriedade):
        for i in range(posicao):
            self.posicao += 1
            self.posicao = 0 if self.posicao == quantidadeDePropriedade else self.posicao
            self.saldo += 100 if self.posicao == quantidadeDePropriedade else 0

    def estaFalido(self):
        return not self.temSaldoPositivo()