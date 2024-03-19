import webbrowser
import time
import os
import pyautogui

url = "https://google.com"
firefox_path = "/usr/bin/firefox"  # Caminho para o Firefox no Linux, pode variar dependendo da sua instalação

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
webbrowser.get('firefox').open(url)

# Aguarda 15 segundos
time.sleep(15)

# Comandos para selecionar todo o texto (Ctrl+A) e copiá-lo (Ctrl+C)
os.system("xdotool key ctrl+u")
time.sleep(5)
pyautogui.hotkey('ctrl', 'a')  # Selecionar todo o texto
time.sleep(5)
pyautogui.hotkey('ctrl', 'c')  # Copiar o texto selecionado
time.sleep(3)

# Adiciona o comando "Ctrl + Shift + T" seguido pelo comando "micro /home/sua/pasta destino/pagina.html"
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(2)
pyautogui.typewrite('sudo su')
pyautogui.press('enter')
time.sleep(2)
# Solicita a senha ao usuário e a armazena em uma variável
pyautogui.typewrite('root aqui')
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('micro')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.typewrite('Atualizado!!')
pyautogui.hotkey('ctrl', 's')
pyautogui.typewrite('/home/sua/pasta destino/pagina.html')
time.sleep(1)
pyautogui.press('enter')
pyautogui.typewrite('y')
pyautogui.hotkey('ctrl', 'q')

