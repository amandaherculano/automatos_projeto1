from tkinter import * 

janela = Tk()
janela.title("Simulador de Máquina de Vendas")
janela.geometry("300x200")

texto_titulo = Label(janela, text="Máquina de Refrigerante")
texto_titulo.grid(row=0, column=0)

texto_orientacao = Label(janela, text="Digite o valor que deseja inserir na máquina:")
texto_orientacao.grid(row=1, column=0, padx=10, pady=10)

def liberar_refrigerante ():
    texto_liberacao["text"] = "Refrigerante liberado!"

botao_1 = Button(janela, text="Liberar Refrigerante", command=liberar_refrigerante)
botao_1.grid(row=2, column=0, padx=10, pady=10)


texto_liberacao = Label(janela, text="")
texto_liberacao.grid(row=3, column=0)
# manter aberta
janela.mainloop() 