print("Helooow World")

def calcular_soma_e_produto(a, b):
    soma = a + b
    produto = a * b
    return soma, produto

# Exemplo de uso da função
resultado_soma, resultado_produto = calcular_soma_e_produto(3, 5)
print(f"Soma: {resultado_soma}, Produto: {resultado_produto}")

# Exemplo de usoi de função para alterar cores ao clicar em um botão

import tkinter as tk
import random

def mudar_cor():
    # Gera uma cor aleatória em formato hexadecimal
    nova_cor = f"#{random.randint(0, 0xFFFFFF):06x}"
    botao.config(bg=nova_cor)

# Criação da janela principal
janela = tk.Tk()
janela.title("Botão que muda de cor")

# Criação do botão
botao = tk.Button(janela, text="Clique em mim!", command=mudar_cor)
botao.pack(pady=20)

# Inicia o loop da interface gráfica
def encontrar_caminho_labirinto(labirinto, inicio, fim):
    """
    Resolve um labirinto usando busca em profundidade (DFS).
    :param labirinto: Lista de listas representando o labirinto (0 = caminho, 1 = parede).
    :param inicio: Tupla (linha, coluna) representando o ponto inicial.
    :param fim: Tupla (linha, coluna) representando o ponto final.
    :return: Lista de tuplas representando o caminho do início ao fim, ou None se não houver caminho.
    """
    def dfs(posicao, caminho):
        if posicao == fim:
            return caminho
        x, y = posicao
        visitados.add(posicao)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimentos: cima, baixo, esquerda, direita
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]) and (nx, ny) not in visitados:
                if labirinto[nx][ny] == 0:  # Verifica se é um caminho válido
                    resultado = dfs((nx, ny), caminho + [(nx, ny)])
                    if resultado:
                        return resultado
        return None

    visitados = set()
    return dfs(inicio, [inicio])

# Exemplo de uso da função
labirinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
inicio = (0, 0)
fim = (4, 4)

caminho = encontrar_caminho_labirinto(labirinto, inicio, fim)
if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Nenhum caminho encontrado.")

janela.mainloop()