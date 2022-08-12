# Alexandre Silvestrin
# Iniciado 05/09/2019
# Finalizado 28/09/2021
# Alterado 18/01/2022
# Equação de Segundo Gral com class e self adiciado

class Baskara:
    def __init__(self):
        self.d = None
        self.x1 = None
        self.x2 = None
        while True:
            try:
                self.a = float(input('Qual o valor de A?: '))
                self.b = float(input('Qual o valor de B?: '))
                self.c = float(input('Qual o valor de C?: '))
            except ValueError:
                print('Digite um valor numerico')
            else:
                Baskara.delta(self)
                Baskara.rx1(self)
                Baskara.rx2(self)
                Baskara.resultado(self)
                try:
                    float(input('\nAcabamos! Se deseja continuar digite 0: '))
                except ValueError:
                    print('Programa finalizado')
                    fim = 'fim'
                    print(f'\n{fim:=^20}')
                    break

    def delta(self):
        self.d = self.b ** 2 - 4 * self.a * self.c

    def rx1(self):
        self.x1 = (-self.b + self.d ** (1 / 2)) / (2 * self.a)

    def rx2(self):
        self.x2 = (-self.b - self.d ** (1 / 2)) / (2 * self.a)

    def resultado(self):
        if self.d > 0:
            print(f'\nDelta = {self.d}\nX1 = {self.x1:.2f}\nX2 = {self.x2:.2f}')
        elif self.d == 0:
            print(f'\nDelta = {self.d}\nX1 = {self.x1:.2f}')
        else:
            print(f'\nDelta = {self.d}\nDelta negativo não ha raizes reais.\n ')


Baskara()
