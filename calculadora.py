#classe calculadora com tratamento de exceções
import tkinter as tk
from tkinter import messagebox
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

#Captura valores e executar operação
def calcular(operacao):
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        calc = Calculadora()

        if operacao == "adição":
            result = calc.adicao(x, y)
        elif operacao == "subtração":
            result = calc.subtracao(x, y)
        elif operacao == "multiplicação":
            result = calc.multiplicacao(x, y)
        elif operacao == "divisão":
            result = calc.divisao(x, y)

        messagebox.showinfo("Resultado", f"O resultado da {operacao} é: {result}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

#Criando a janela
root = tk.Tk()
root.title("Calculadora Simples")

tk.Label(root, text="Digite o primeiro número:").grid(row=0, column=0, padx=10, pady=10)
entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Digite o segundo número:").grid(row=1, column=0, padx=10, pady=10)
entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1, padx=10, pady=5)

#Botões
tk.Button(root, text="Adição", command=lambda: calcular("adição")).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Subtração", command=lambda: calcular("subtração")).grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Multiplicação", command=lambda: calcular("multiplicação")).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Divisão", command=lambda: calcular("divisão")).grid(row=3, column=1, padx=10, pady=5)

#iniciar loop da interface
root.mainloop()


