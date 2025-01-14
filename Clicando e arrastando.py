Automação de Tarefas com PyAutoGUI
Este script em Python utiliza a biblioteca PyAutoGUI para automatizar tarefas de arrastar e soltar arquivos,
além de criar pastas automaticamente em um ambiente de trabalho. Ele é uma solução simples, mas poderosa, para lidar com tarefas repetitivas.

Funcionalidades:
Movimentação do cursor até coordenadas específicas.
Arrastar e soltar itens de uma pasta para outra.
Criação de pastas por meio de cliques simulados.
Como funciona:
O script posiciona o cursor no ponto inicial definido.
Arrasta e solta os arquivos um por um.
Ao final, simula cliques para criar uma nova pasta.

import pyautogui

# Mover para a coordenada inicial
pyautogui.moveTo(923, 129, duration=2)

for i in range(6):
    # Clicar, arrastar até outra coordenada e soltar
    pyautogui.moveTo(923, 129, duration=2)
    pyautogui.dragTo(904, 498, button='left', duration=1)

# Criar uma nova pasta
pyautogui.rightClick(902, 132, duration=2)
pyautogui.move(20, 280, duration=2)
pyautogui.move(-90, 0, duration=2)
pyautogui.click()
