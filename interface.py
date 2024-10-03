from tkinter import * 

janela = Tk()
janela.title("Simulador de Máquina de Vendas")
janela.geometry("600x500")


texto_titulo = Label(janela, text="Máquina de Refrigerante", font=("Calibri", 15))
texto_titulo.grid(row=0, column=0, pady=20, padx=10)

saldo = 0
texto_saldo = Label(janela, text="Saldo: R$ " + str(saldo))
texto_saldo.grid(row=0, column=4, pady=20, padx=10)

texto_orientacao = Label(janela, text="Selecione valor para inserir:")
texto_orientacao.grid(row=2, column=0)

def alterar_saldo25 ():
    global saldo
    saldo = saldo + 0.25
    texto_saldo["text"] = "Saldo: R$ " + str(saldo)

def alterar_saldo50 ():
    global saldo
    saldo = saldo + 0.50
    texto_saldo["text"] = "Saldo: R$ " + str(saldo)

def alterar_saldo100 ():
    global saldo
    saldo = saldo + 1.00
    texto_saldo["text"] = "Saldo: R$ " + str(saldo)

botao_25 = Button(janela, text="R$ 0.25", command=alterar_saldo25)
botao_25.grid(row=2, column=1, padx=10, pady=10)
botao_50 = Button(janela, text="R$ 0.50", command=alterar_saldo50)
botao_50.grid(row=2, column=2, padx=10, pady=10)
botao_100 = Button(janela, text="R$ 1.00", command=alterar_saldo100)
botao_100.grid(row=2,column=3, padx=10, pady=10)


def liberar_refrigerante ():
    global saldo
    if saldo == 2.0:
        saldo = 0
        texto_saldo["text"] = "Saldo: R$ " + str(saldo)
        texto_liberacao["text"] = "Refrigerante liberado!"
    elif saldo > 2.00:
        troco = saldo - 2.00
        saldo = 0
        texto_saldo["text"] = "Saldo: R$ " + str(saldo)
        texto_liberacao["text"] = "Refrigerante liberado! Troco: R$ " + str(troco)
    else:
        texto_liberacao["text"] = "Saldo insuficiente!"


botao_1 = Button(janela, text="Liberar Refrigerante", command=liberar_refrigerante)
botao_1.grid(row=3, columnspan=5, pady=20)


texto_liberacao = Label(janela, text="")
texto_liberacao.grid(row=4, column=0)
# manter aberta
janela.mainloop() 