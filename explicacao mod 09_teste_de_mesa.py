class Celular:
    def __init__(self, marca, modelo, ):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100
    def fazer_chamada(self, duracao):
        try:
            gasto=int(duracao)*2
            if self.bateria >= gasto:
                self.bateria -= gasto
            print(f"Chamada de{duracao} min feita! Bateria: {self.bateria}%")
        
        except ValueError:
            print("Erro: a duracao deve ser um numero inteiro.")

    meu_celular = Celular("samsung", "S24")

    meu_celular.fazer_chamada("10")






