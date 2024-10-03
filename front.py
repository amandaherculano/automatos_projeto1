from tkinter import * 

janela = Tk()
janela.title("Simulador de Máquina de Vendas")
janela.geometry("600x500")

texto_titulo = Label(janela, text="Máquina de Refrigerante", font=("", 15))
texto_titulo.grid(row=0, column=0)

texto_orientacao = Label(janela, text="Digite o valor que deseja inserir na máquina:")
texto_orientacao.grid(row=1, column=0, padx=10, pady=10)

entry = Entry(janela)
entry.grid(row=1, column=1, padx=10, pady=10)
saldo = 0
texto_saldo = Label(janela, text="Saldo: R$ " + str(saldo))
texto_saldo.grid(row=0, column=3)

# ARRUMAR EXIBIR SALDO
def confirmar ():
    valor_inserido = entry.get()
    valor = float(valor_inserido)
    print(type(valor))
    # texto_liberacao["text"] = entry.get()
    if valor == 0.25 or valor == 0.50 or valor == 1.00:
        saldo =+ valor
        texto_saldo["text"] = "Saldo: R$ " + str(saldo)
        print(saldo)
        texto_liberacao["text"] = "SALDO ALTERADO!"

botao_2 = Button(janela, text="Confirmar", command=confirmar)
botao_2.grid(row=1, column=2, padx=10, pady=10)

def liberar_refrigerante ():
    if saldo == 2.0:
        texto_liberacao["text"] = "Refrigerante liberado!"
    elif saldo > 2.00:
        troco = saldo - 2.00
        texto_liberacao["text"] = "Refrigerante liberado! Troco: R$ " + str(troco)
    else:
        texto_liberacao["text"] = "Saldo insuficiente!"


botao_1 = Button(janela, text="Liberar Refrigerante", command=liberar_refrigerante)
botao_1.grid(row=2, column=0, padx=10, pady=10)


texto_liberacao = Label(janela, text="")
texto_liberacao.grid(row=3, column=0)
# manter aberta
janela.mainloop() 