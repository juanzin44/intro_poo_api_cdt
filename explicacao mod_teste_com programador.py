class celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100
    def fazer_chamada(self, custo_bateria):
        print(f"\n---Chamada no {self.modelo}---")
        try:
            self.bateria -= custo_bateria 
        except TypeError:
            print("Erro: o custo de bateria deve ser um número inteiro.")
        else:
            print(f"sucesso! bateria atual: {self.bateria}%")
        finally:
            print("sistema finalizado.")




















