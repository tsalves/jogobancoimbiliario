import resultado, tabuleiro

res = resultado.Resultado()

for i in range(0, 299):
    inicio = tabuleiro.Tabuleiro()
    inicio.iniciar(res)
    del inicio

print(str(res.getResultadoFinal()))