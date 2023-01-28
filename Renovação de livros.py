import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


#Guardar login e senha de acesso
login = input('Login do SIGAA: ')
senha = input('Senha do SIGAA: ')


#iniciar o navegador, acessar o site e faz login no sistema SIGAA
navegador = webdriver.Chrome()
navegador.get('https://sigaa.ufpi.br/sigaa/verTelaLogin.do;jsessionid=D425BF5D3957F6BA33A8E9418617AE15.jb05')
navegador.find_element('xpath', '//*[@id="conteudo"]/div[3]/form/table[1]/tbody/tr[1]/td/input').send_keys(login, Keys.TAB, senha, Keys.ENTER)


#encontrar o caminho para a opção de renovação de empréstimos navegando no menu suspenso
menu_suspenso = navegador.find_element('xpath', '//*[@id="menu_form_menu_discente_j_id_jsp_1325243614_85_menu"]/table/tbody/tr/td[6]/span[2]')
acoes = ActionChains(navegador)
acoes.move_to_element(menu_suspenso).perform()

menu_suspenso = navegador.find_element('xpath', "//*[text() = 'Empréstimos']")
acoes = ActionChains(navegador)
acoes.move_to_element(menu_suspenso).perform()

menu_suspenso = navegador.find_element('xpath', "//*[text() = 'Renovar Meus Empréstimos']")
acoes = ActionChains(navegador)
acoes.move_to_element(menu_suspenso).perform()
menu_suspenso.click()

#clica no botão de selecionar todos, dá uma pausa de 3 segundos e confirma
renovar_todos = navegador.find_element('xpath', '//*[@id="formularioRenovamaMeusEmprestimos"]/table/thead/tr/th[1]/input')
renovar_todos.click()
sleep(3)
renovar_todos = navegador.find_element('xpath', '//*[@id="formularioRenovamaMeusEmprestimos:cmdButtonConfirmarRenovacaoMeusEmprestimos"]')
renovar_todos.click(),sleep(3)
pyautogui.press('ENTER')

sleep(15)

