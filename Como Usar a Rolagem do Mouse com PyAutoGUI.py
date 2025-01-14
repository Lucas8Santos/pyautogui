Como Usar a Rolagem do Mouse com PyAutoGUI
Este script demonstra como automatizar a rolagem do mouse usando a biblioteca PyAutoGUI.
Ideal para cenários em que é necessário percorrer longas páginas ou listas de forma repetitiva.

Descrição do Código
Funcionalidade:
Move o cursor até uma posição específica na tela.
Realiza a rolagem para baixo (-2500) repetidamente, com um intervalo de 2 segundos entre cada iteração.
Exemplo de Código:

# Importando as bibliotecas necessárias
import pyautogui
from time import sleep

# Movendo o cursor para uma coordenada específica
pyautogui.moveTo(1120, 254, duration=2)

# Rolando a tela para baixo repetidamente
for i in range(500):
    pyautogui.scroll(-2500)  # Valor negativo para rolar para baixo
    sleep(2)  # Pausa de 2 segundos entre as rolagens


Dica:

Use valores positivos em pyautogui.scroll() para rolar para cima.
Adicione pausas estratégicas para evitar possíveis problemas de desempenho.
