#classe calculadora com tratamento de exceções

class Calculadora:
    def adicao(self, x, y):
        try:
            return x + y
        except TypeError:
            return "Erro: Tipos de dados inválidos para adição."


    def subtracao(self, x, y):
        try:
            return x - y
        except TypeError:
            return "Erro: Tipos de dados inválidos para subtração."

    def multiplicacao(self, x, y):
        try:
            return x * y
        except TypeError:
            return "Erro: Tipos de dados inválidos para multiplicação."

    def divisao(self, x, y):
        try:
            return x / y
        except TypeError:
            return "Erro: Tipos de dados inválidos para divisão."
        except ZeroDivisionError:
            return "Erro: Não é possível dividir por zero."


#testando implementações
calculadora = Calculadora()

print(calculadora.adicao(5, 3))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(5, 3))
print(calculadora.divisao(5, 0))
