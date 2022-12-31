import pyautogui            #biblioteca de métodos para controlar mouse e teclado
from time import sleep      #mecanismo de controle de tempo

# esse comando separa cada passo do programa em 1 segundo
pyautogui.PAUSE = 1

# esperar 3 segundos
sleep(3)

#apertar a tecla windows para abrir o menu iniciar
pyautogui.press('win')

#escrever o nome do programa a ser buscado no menu iniciar
pyautogui.write('brave')
sleep(3)


pyautogui.press('enter')
sleep(5)

#pyautogui.click(x=887, y=251)         #uso esse comando no caso de o navegador não abrir em tela cheia

# escrever endereço do site da universidade
pyautogui.write('https://sigaa.ufpi.br/sigaa')
pyautogui.press('enter')
sleep(5)

# aqui você digita seu login e em seguida a senha
pyautogui.write('*login*')
pyautogui.press('tab')
pyautogui.write('*senha*')
pyautogui.press('enter')


sleep(5)
pyautogui.press('tab')
#sleep(0.3)
pyautogui.press('tab')
#sleep(0.3)
pyautogui.press('tab')
#sleep(1)
pyautogui.press('enter')
sleep(4)

# Sequência de clicks do mouse em posições previamente estabelecidas
pyautogui.click(x=631, y=159)
pyautogui.click(x=861, y=247)
pyautogui.click(x=1028, y=281)
sleep(2.5)
pyautogui.click(x=201, y=351)
pyautogui.click(x=657, y=508)
pyautogui.press('enter')


#código para descobrir a posição do mouse em que efetuará o click
# sleep(5)
# n = pyautogui.position()
# print(n)

