import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constante gravitacional simplificada para a simulação
G = 0.1

class CorpoCeleste:
    def __init__(self, nome, massa, posicao, velocidade, cor, tamanho):
        self.nome = nome
        self.massa = massa 
        self.posicao = np.array(posicao, dtype = float)
        self.velocidade = np.array(velocidade, dtype = float)
        self.cor = cor 
        self.tamanho = tamanho
        self.rastro_x = []
        self.rastro_y = []

    def atualizacao_posicao(self, dt):
        self.posicao += self.velocidade * dt
        self.rastro_x.append(self.posicao[0])
        self.rastro_y.append(self.posicao[1])

class SistemaSolar:
    def __init__(self):
        self.corpos = []

    def adicionar_corpo(self, corpo):
        self.corpos.append(corpo)

    def calcular_gravidade(self, dt):
        for i, corpo_a in enumerate(self.corpos):
            for j, corpo_b in enumerate(self.corpos):
                if i == j:
                    continue

                # Vetor distância entre os corpos
                vetor_r = corpo_b.posicao - corpo_a.posicao
                distancia = np.linalg.norm(vetor_r)

                # Evita divisão por zero se os corpos estiverem na mesma posição
                if distancia == 0:
                    continue

                # Força newtoniana: F = G * (m1 * m2) / r^2
                magnitude_forca = G * corpo_a.massa * corpo_b.massa / (distancia ** 2)
                direcao_forca = vetor_r /  distancia

                # Aceleração da velocidade
                aceleracao = (magnitude_forca * direcao_forca) / corpo_a.massa

                corpo_a.velocidade += aceleracao * dt

ss = SistemaSolar()

sol = CorpoCeleste("Sol", 1000, [0, 0], [0, 0], "yellow", 100)
venus = CorpoCeleste("Vênus", 0.6, [6, 0], [0, 4], "orange", 35)
terra = CorpoCeleste("Terra", 1, [11, 0], [0, 3], "blue", 30)
marte = CorpoCeleste("Marte", 0.8, [16, 0], [0, 2.5], "red", 32)

ss.adicionar_corpo(sol)
ss.adicionar_corpo(venus) 
ss.adicionar_corpo(terra)
ss.adicionar_corpo(marte)

# configuração Gráfica
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("black")
plt.xlim(-20, 20)
plt.ylim(-20, 20)

desenhos = [ax.plot([], [], "o", color=c.cor, ms=c.tamanho/5, label=c.nome) [0] for c in ss.corpos]
rastros = [ax.plot([], [], "-", color=c.cor, alpha=0.3)[0] for c in ss.corpos]

def animate(i):
    ss.calcular_gravidade(0.1)
    for corpo, desenho, rastro in zip(ss.corpos, desenhos, rastros):
        corpo.atualizacao_posicao(0.1)
        desenho.set_data([corpo.posicao[0]], [corpo.posicao[1]])
        rastro.set_data(corpo.rastro_x[-40:], corpo.rastro_y[-40:])
    return desenhos + rastros

ani = FuncAnimation(fig, animate, frames=200, interval=20, blit=True)
plt.legend(loc = "upper right")
plt.title("Simulação Órbital: Sol, Vênus, Terra e Marte")
plt.show()
