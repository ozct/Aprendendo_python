# Desafio
class Bicicleta:
  def __init__(self, cor, modelo, ano, valor, aro=19, nro_marcha):
    self.cor = cor
    self.ano = ano
    self.modelo = modelo
    self.valor = valor
    self.aro = aro
    self.nro_marcha = nro_marcha

  def buzzinar(self):
    print("Plim Plim ...")

  def parar(self):
    print("Parando bicicleta ...")
    print("Bicicleta parada!")

  def correr(self):
    print("Vrummm...")

  def _trocar_marcha(self, nro_marcha):
    print("Trocando marcha...")

    _self = self

    def _trocando_marcha():
      if nro_marcha > _self.marcha:
        print("March trocado!")
      else:
        print("Não foi possível trocar de marcha...")

  # def __str__(self):
  #   return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}. valor={self.valor}"

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self. __dict__.items()])}"


# b1 = Bicicleta("Dark Blue", "Monark", "2023", 1000)
# b1.buzzinar()
# b1.correr()
# b1.parar()
# b1.correr()
# b1.buzzinar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)


b2 = Bicicleta("Black", "Monark", 2015, 1000)
b2.buzzinar()
Bicicleta.buzzinar(b2)
print(b2)

