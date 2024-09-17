import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuário
pyautogui.click(642,398,duration=2)
pyautogui.write('Tiago')
# 2 - Clicar e digitar minha senha
pyautogui.click(639,427,duration=2)
pyautogui.write('1234')
# 3 - Clicar em "Entrar"
pyautogui.click(551,456,duration=2)
# 4 - Extrair cada prodTiagouto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #   1 - clicar e digitar produto
        pyautogui.click(353,388,duration=2)
        pyautogui.write(produto)
        #   2 - clicar e digitar quantidade
        pyautogui.click(348,413,duration=2)
        pyautogui.write(quantidade)
        #   3 - clicar e digitar preço
        pyautogui.click(352,442,duration=2)
        pyautogui.write(preco)
        #   4 - clicar em registrar
        pyautogui.click(278,596,duration=1)
        sleep(1)

