import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

class Projetil:
    def __init__(self, nome, posicao, velocidade, cor, tamanho):
        self.nome = nome 
        self.posicao = np.array(posicao, dtype=float)
        self.velocidade = np.array(velocidade, dtype=float)
        self.cor = cor
        self.tamanho = tamanho

        self.rastro_x = []
        self.rastro_y = []

    def atualizar_posicao(self, dt):
        self.posicao += self.velocidade * dt
        self.rastro_x.append(self.posicao[0])
        self.rastro_y.append(self.posicao[1])

class MovimentoAnimado:
    def __init__(self):
        self.projeteis = []

    def adicionar_projetil(self, projetil):
        self.projeteis.append(projetil)

sistema = MovimentoAnimado()

a = Projetil("A", [0, 5], [1, 0], "yellow", 10)

sistema.adicionar_projetil(a)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor("black")
plt.xlim(0, 40)
plt.ylim(0, 15)

ax.set_xlabel("Posição x")
ax.set_ylabel("Posição y")
ax.set_title("Movimento do projétil", color="white")

ax.tick_params(colors="white")
ax.xaxis.label.set_color("white")
ax.yaxis.label.set_color("white")
ax.title.set_color("white")


desenhos = [ax.plot([], [], "o", color=p.cor, ms=p.tamanho / 5, label=p.nome)[0] for p in sistema.projeteis]
rastros = [ax.plot([], [], "-", color=p.cor, lw=1)[0] for p in sistema.projeteis]

def animate(i):
    for desenho, rastro in zip(desenhos, rastros):
        desenho.set_data([], [])
        rastro.set_data([], [])
    return desenhos + rastros

def animar(frame):
    dt = 0.7

    for indice, projetil in enumerate(sistema.projeteis):
        projetil.atualizar_posicao(dt)

        desenhos[indice].set_data([projetil.posicao[0]], [projetil.posicao[1]])

        rastros[indice].set_data(projetil.rastro_x, projetil.rastro_y)

    return desenhos + rastros

def reiniciar_animacao(evento):
    sistema.reiniciar()

    animate()

    animacao.frame_seq = animacao.new_frame_seq()

    fig.canvas.draw_idle()

animacao = FuncAnimation(fig, animar, frames=200, interval=20, blit=True)

area_botao = fig.add_axes([0.38, 0.05, 0.24, 0.08])

botao_reiniciar = Button(area_botao, "Reiniciar", color="lightgray", hovercolor="lightblue")
botao_reiniciar.on_clicked(reiniciar_animacao)

ani = FuncAnimation(fig, animar, frames=200, interval=20, blit=True)
plt.show()
