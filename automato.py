from tkinter import *

class VendingMachineAutomaton:
    def __init__(automato):
        # Estados e estado inicial
        automato.states = {
            's0': 0.00, 's1': 0.25, 's2': 0.50, 's3': 0.75,
            's4': 1.00, 's5': 1.25, 's6': 1.50, 's7': 1.75, 's8': 2.00
        }
        automato.current_state = 's0'

        # Função de transição
        automato.transitions = {
            ('s0', 'm25'): ('s1', 'n'), ('s0', 'm50'): ('s2', 'n'), ('s0', 'm100'): ('s4', 'n'),
            ('s1', 'm25'): ('s2', 'n'), ('s1', 'm50'): ('s3', 'n'), ('s1', 'm100'): ('s5', 'n'),
            ('s2', 'm25'): ('s3', 'n'), ('s2', 'm50'): ('s4', 'n'), ('s2', 'm100'): ('s6', 'n'),
            ('s3', 'm25'): ('s4', 'n'), ('s3', 'm50'): ('s5', 'n'), ('s3', 'm100'): ('s7', 'n'),
            ('s4', 'm25'): ('s5', 'n'), ('s4', 'm50'): ('s6', 'n'), ('s4', 'm100'): ('s8', 'n'),
            ('s5', 'm25'): ('s6', 'n'), ('s5', 'm50'): ('s7', 'n'), ('s5', 'm100'): ('s8', 't25'),
            ('s6', 'm25'): ('s7', 'n'), ('s6', 'm50'): ('s8', 'n'), ('s6', 'm100'): ('s8', 't50'),
            ('s7', 'm25'): ('s8', 'n'), ('s7', 'm50'): ('s8', 't25'), ('s7', 'm100'): ('s8', 't75'),
            ('s8', 'm25'): ('s8', 't25'), ('s8', 'm50'): ('s8', 't50'), ('s8', 'm100'): ('s8', 't100'),
            ('s8', 'b'): ('s0', 'r'),  # Liberar refrigerante
            ('s0', 'b'): ('s0', 'n'), ('s1', 'b'): ('s1', 'n'), ('s2', 'b'): ('s2', 'n'),
            ('s3', 'b'): ('s3', 'n'), ('s4', 'b'): ('s4', 'n'), ('s5', 'b'): ('s5', 'n'),
            ('s6', 'b'): ('s6', 'n'), ('s7', 'b'): ('s7', 'n')
        }

    def input(automato, coin_or_button):
        """Processa uma entrada (moeda ou botão) e altera o estado."""
        if (automato.current_state, coin_or_button) in automato.transitions:
            next_state, output = automato.transitions[(automato.current_state, coin_or_button)]
            automato.current_state = next_state
            return output
        else:
            return 'n'  # Nada acontece


# Interface Tkinter
janela = Tk()
janela.title("Simulador de Máquina de Vendas")
janela.geometry("700x300")

# Instanciar o autômato
vm = VendingMachineAutomaton()

texto_titulo = Label(janela, text="Máquina de Refrigerante", font=("Calibri", 15), fg="darkolivegreen")
texto_titulo.grid(row=0, column=0, pady=20, padx=10)

# Saldo inicial
saldo = 0
texto_saldo = Label(janela, text="Saldo: R$ " + str(saldo),  font=("Calibri", 13), fg="dimgray")
texto_saldo.grid(row=0, column=4, pady=20, padx=10)

texto_titulo = Label(janela, text="Valor R$ 2,00", font=("Calibri", 13), fg="palegreen4")
texto_titulo.grid(row=1, column=0)

texto_orientacao = Label(janela, text="Selecione valor para inserir:", font=("Calibri", 13), fg="dimgray")
texto_orientacao.grid(row=2, column=0)

# Funções para alterar saldo usando o autômato
def alterar_saldo(coin_value):
    global saldo
    # Limpa a mensagem quando uma moeda é inserida
    texto_liberacao["text"] = ""
    output = vm.input(coin_value)
    saldo = vm.states[vm.current_state]
    texto_saldo["text"] = "Saldo: R$ " + str(saldo)
    if output.startswith('t'):
        if output == 't25':
            texto_liberacao["text"] = "Troco: R$ 0.25"
        elif output == 't50':
            texto_liberacao["text"] = "Troco: R$ 0.50"
        elif output == 't100':
            texto_liberacao["text"] = "Troco: R$ 1.00"

# Botões de moeda
botao_25 = Button(janela, text="R$ 0.25", command=lambda: alterar_saldo('m25'), bg="darkgoldenrod3", fg="cornsilk1", width=10, height=1, font=("Calibri", 12))
botao_25.grid(row=2, column=1, padx=10, pady=10)

botao_50 = Button(janela, text="R$ 0.50", command=lambda: alterar_saldo('m50'), bg="ivory3", fg="cornsilk1", width=10, height=1, font=("Calibri", 12))
botao_50.grid(row=2, column=2, padx=10, pady=10)

botao_100 = Button(janela, text="R$ 1.00", command=lambda: alterar_saldo('m100'), bg="gold2", fg="cornsilk1", width=10, height=1 , font=("Calibri", 12))
botao_100.grid(row=2, column=3, padx=10, pady=10)

# Função para liberar refrigerante
def liberar_refrigerante():
    global saldo
    if saldo >= 2.00:
        alterar_saldo('b')
        texto_liberacao["text"] = "Refrigerante liberado!"
    else:
        texto_liberacao["text"] = "Saldo insuficiente! Insira mais moedas."

# Botão para liberar refrigerante
botao_1 = Button(janela, text="Liberar Refrigerante", command=liberar_refrigerante,  font=("Calibri", 14), bg='darkolivegreen', fg='cornsilk')
botao_1.grid(row=3, columnspan=5, pady=30)

# Exibir mensagem de liberação
texto_liberacao = Label(janela, text="", fg="darkolivegreen", font=("Calibri", 13))
texto_liberacao.grid(row=4, columnspan=5)

texto_nomes = Label(janela, text="Desenvolvido por: ", font=("Calibri", 13), fg="violetred3")
texto_nomes.grid(row=5, column=0, pady=11)

texto_amanda = Label(janela, text="Amanda Herculano, 22.00986-8", font=("Calibri", 13), fg="violetred3")
texto_amanda.grid(row=6, column=0, pady=10)

texto_iris = Label(janela, text="Íris Melero, 23.01109-2", font=("Calibri", 13), fg="violetred3")
texto_iris.grid(row=7, column=0, pady=10)

texto_maria= Label(janela, text="Maria Rodrigues, 23.00018-0", font=("Calibri", 13), fg="violetred3")
texto_maria.grid(row=8, column=0, pady=10)

# Manter a janela aberta
janela.mainloop()
