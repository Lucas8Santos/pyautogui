Descrição do Código
Funcionalidades:
Move o cursor até o campo de texto.
Digita a mensagem usando Ctrl+V para evitar problemas de codificação.
Clica no botão de envio.
Exemplo de Código:

# Importando bibliotecas necessárias
import pyautogui
import pyperclip

# Função para copiar e colar a mensagem com caracteres especiais do teclado brasileiro
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')

# Movendo o cursor até o campo de digitação
pyautogui.moveTo(772, 690, duration=3)
pyautogui.click()

# Digitando a mensagem
escrever_frase('Olá, bom dia, como você está?')

# Clicando no botão enviar
pyautogui.click(1316, 690, duration=3)


Aplicações:
Automação de envio em massa de mensagens no WhatsApp.
Respostas rápidas em plataformas de atendimento ao cliente.
Execução de tarefas repetitivas em interfaces gráficas.
💡 Dica: Adicione controles e verificações para tornar o bot ainda mais robusto e seguro.
