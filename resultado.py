class Resultado:
    
    def __init__(self):
        self.timeouts = 0
        self.rodadas = []
        self.impulsivo = 0
        self.aleatorio = 0
        self.exigente = 0
        self.cauteloso = 0

    def setTimeouts(self, valor = 1):
        self.timeouts += valor

    def setRodadas(self, valor = 1):
        self.rodadas.append(valor)

    def setGanhadores(self, ganhador, valor = 1):
        if ganhador == 'impulsivo':
            self.impulsivo += valor
        elif ganhador == 'aleatorio':
            self.aleatorio += valor
        elif ganhador == 'exigente':
            self.exigente += valor
        elif ganhador == 'cauteloso':
            self.cauteloso += valor

    def getMaiorVencedor(self):
        ganhador = 0

        if self.exigente > ganhador:
            ret = 'exigente'
            ganhador = self.exigente

        if self.impulsivo > ganhador:
            ret = 'impulsivo'
            ganhador = self.impulsivo

        if self.aleatorio > ganhador:
            ret = 'aleatorio'
            ganhador = self.aleatorio

        if self.cauteloso > ganhador:
            ret = 'cauteloso'
            ganhador = self.cauteloso

        return ret

    def getTimeouts(self):
        return self.timeouts

    def getMediaRodadas(self):
        return sum(self.rodadas) / len(self.rodadas)    

    def getPorcentagemGanhadores(self):
        ret = '\nExigente :' + str((self.exigente / (self.exigente + self.impulsivo + self.aleatorio + self.cauteloso)) * 100) + '%'
        ret += '\nImpulsivo :' + str((self.impulsivo / (self.exigente + self.impulsivo + self.aleatorio + self.cauteloso)) * 100) + '%'
        ret += '\nAleatorio :' + str((self.aleatorio / (self.exigente + self.impulsivo + self.aleatorio + self.cauteloso)) * 100) + '%'
        ret += '\nCauteloso :' + str((self.cauteloso / (self.exigente + self.impulsivo + self.aleatorio + self.cauteloso)) * 100) + '%'

        return ret

    def getResultadoFinal(self):
        ret = 'Quantidades de timeouts: ' + str(self.getTimeouts())
        ret += '\nMédia de rodadas: ' + str(self.getMediaRodadas())
        ret += '\nVitorias por comportamento: ' + str(self.getPorcentagemGanhadores())
        ret += '\nComportamento mais vitorioso: ' + str(self.getMaiorVencedor())

        return ret

