from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pyautogui
import time

options = Options()
# options.add_argument("--headless")
navegador = webdriver.Chrome(options=options)
navegador.maximize_window()


# Declaração de variáveis globais (login, senha e link)
login = "2255310@light.com.br"
senha = "Psiec@350"
link = "https://lightsa.etadirect.com/"

# Usando o selenium para entrar no link que precisa
navegador.get(url=link)

sleep(3)

# Colocando usuário, senha e clicando em continuar
user = navegador.find_element(by=By.ID, value='username')
user.send_keys(login)

password = navegador.find_element(by=By.ID, value="password")
password.send_keys(senha)

conectar = navegador.find_element(by=By.ID, value="sign-in")
conectar.click()

sleep(3)

# Novamente colocando usuário e senha e colocando em continuar
elemento1 = navegador.find_element(by=By.ID, value="i0116")
elemento1.send_keys(login)
navegador.find_element(by=By.ID, value="idSIButton9").click()

sleep(3)

elemento2 = navegador.find_element(by=By.ID, value="i0118")
elemento2.send_keys(senha)
navegador.find_element(by=By.ID, value="idSIButton9").click()

sleep(3)

# Clicando em continuar
navegador.find_element(by=By.ID, value="idSIButton9").click()

sleep(20)
# Caminho para a imagem que você deseja usar como referência (divisor)
image_path = 'img.png'

# Caminho para a imagem que você deseja usar como referência (O campo antes de dividir a tela)
img_1 = "img1.png"

# Caminho para a imagem que você deseja usar como referência (agendado)
img_2 = "img2.png"

# Caminho para a imagem que você deseja usar como referência (clicar em não agendado)
img_3 = "img3.png"

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"

# Caminho para a imagem que você deseja usar como referência (aplicar) 
img_5 = "img5.png"


# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_1, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2

        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()
        
except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")

# Procura a posição da imagem na tela durante o tempo limite definido
try:
    location = pyautogui.locateOnScreen(image_path, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2

        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()
        
except Exception as e:
        print(f"Erro ao localizar a imagem: {e}")
sleep(4)
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    location = pyautogui.locateOnScreen(img_2, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2

        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()
        
except Exception as e:
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_3, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2

        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()
        
except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")  

sleep(2)
#Selecionar aba dos agentes da negociação e pré-corte 
selecao_aba_agentes = navegador.find_element(by=By.XPATH, value ='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[1]/button[1]').click()
sleep(2)
#NEGOCIAÇÃO:
selecão_aba_negociacao = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[1]/button[1]').click()
sleep(2)


#AGENTES DA NEGOCIAÇÃO(34 AGENTES)
#CNL1
cnl001 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]').click()
sleep(1)
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")

sleep(2)      

#Apagar o "*" e inserir as notas
for _ in range(1):
        pyautogui.press("backspace")
        sleep(1)
        pyautogui.write('Ordem de Ser', interval=0.25)  
        sleep(1)
        pyautogui.press('tab')  
        sleep(1)
        pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")

#Selecionar notas        
selecao_notas_de_servico = navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[4]/div/div/div[1]/div[1]/table/tbody/tr/td[1]/input').click()
sleep(2)
#Arrastar notas para o campo de cima(FALTA)




#CNL2
cnl002 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]').click()
sleep(1)
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        
selecao_notas_de_servico = navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[4]/div/div/div[1]/div[1]/table/tbody/tr/td[1]/input').click()
sleep(2)




#CNL3
cnl003 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[3]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        
selecao_notas_de_servico = navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[4]/div/div/div[1]/div[1]/table/tbody/tr/td[1]/input').click()
sleep(2)




#CNL4
cnl004 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[4]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")

sleep(2)
#Selecionar notas        
selecao_notas_de_servico = navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[4]/div/div/div[1]/div[1]/table/tbody/tr/td[1]/input').click()
sleep(2)




#CNL5
cnl005 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[5]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        





#CNL6
cnl006 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[6]').click()

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        

#CNL7
cnl007 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[7]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        




#CNL8
cnl008 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[8]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
#Selecionar notas        



#CNL9
cnl009 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[9]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL10
cnl0010 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[10]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)


#CNL11
cnl0011 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[11]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL12
cnl0012 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[12]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL13
cnl0013 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[13]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL14
cnl0014 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[14]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL15
cnl0015 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[15]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL16
cnl0016 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[16]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL18
cnl0018 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[18]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL19
cnl0019 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[19]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL20
cnl0020 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[20]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL21
cnl0021 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[21]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL22
cnl0022 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[22]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL23
cnl0023 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[23]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")  
sleep(2)

#CNL24
cnl0024 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[24]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL25
cnl0025 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[25]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL26
cnl0026 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[26]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL27
cnl0027 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[27]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL28
cnl0028 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[28]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL29
cnl0029 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[29]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL30
cnl0030 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[30]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL31
cnl0031 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[31]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")      
sleep(2)

#CNL32
cnl0032 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[32]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL33
cnl0033 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[33]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL34
cnl0034 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[34]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL35
cnl0035 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[2]/div[35]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#Finalizar negociação
finalizar_negociacao = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[1]/div[1]/button[1]').click()
sleep(2)

#Abrir aba pré corte
abrir_precorte = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[1]/button[1]').click()
sleep(2)

#AGENTES DO PRÉ-CORTE
#CNL36
cnl0036 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL37
cnl0037 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL38
cnl0038 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[3]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL39
cnl0039 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[4]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL40
cnl0040 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[5]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL41
cnl0041 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[6]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL42
cnl0042 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[7]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL43
cnl0043 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[8]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL44
cnl0044 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[9]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL45
cnl0045 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[10]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)

#CNL46
cnl0046 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[11]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL47
cnl0047 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[12]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL48
cnl0048 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[13]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL49
cnl0049 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[14]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL50
cnl0050 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[15]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL51
cnl0051 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[16]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL52
cnl0052 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[17]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL53
cnl0053 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[18]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL54
cnl0054 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[19]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL55
cnl0055 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[20]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL56
cnl0056 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[21]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL57
cnl0057 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[22]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL58
cnl0058 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[23]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL59
cnl0059 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[24]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL60
cnl0060 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[25]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL61
cnl0061 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[26]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL62
cnl0062 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[27]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL63
cnl0063 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[28]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL64
cnl0064 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[29]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL65
cnl0065 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[30]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL66
cnl0066 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[31]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL67
cnl0067 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[32]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL68
cnl0068 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[33]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL69
cnl0069 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[34]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL70
cnl0070 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[35]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL71
cnl0071 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[36]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL72
cnl0072 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[37]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL73
cnl0073 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[38]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL74
cnl0074 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[39]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL75
cnl0075 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[40]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL76
cnl0076 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[41]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL77
cnl0077 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[42]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL78
cnl0078 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[43]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL79
cnl0079 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[44]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL80
cnl0080 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[45]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL81
cnl0081 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[46]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNNL82
cnl0082 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[47]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
#CNL83
cnl0083 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[48]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
        
sleep(2)
cnl0084 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[49]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

cnl0085 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[50]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

cnl0086 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[51]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
cnl0087 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[52]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)
cnl0088 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[53]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)     

cnl0089 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[54]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)    

cnl0090 = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div[55]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)        


#Finalizar pré corte
finalizar_precorte = navegador.find_element(by=By.XPATH, value ='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[1]/button[1]')
finalizar_precorte.click()
sleep(2)

#Selecionar agentes do corte:
selecao_balde_corte = navegador.find_element(by=By.XPATH, value='//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/button[1]')
selecao_balde_corte.click() 
sleep(2)

#Selecionar balce do corte:
corte = navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[3]/div/div[2]/div[3]/div[2]')
corte.click()
sleep(2)

#AGENTES DO CORTE (CDJL)
#CDJL1
cdjl001=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[1]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL2
cdjl002=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[2]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL3
cdjl003=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[3]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL4
cdjl004=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[4]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL5
cdjl005=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[5]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL6
cdjl006=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[6]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL7
cdjl007=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[7]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL8
cdjl008=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[8]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#CDJL9
cdjl009=navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div[9]').click()
# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_4 = "img4.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_4, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)      
#Apertar "tab" e digitar notas de serviços
pyautogui.press('tab')  
sleep(1)
pyautogui.write('', interval=0.25) 

# Caminho para a imagem que você deseja usar como referência (clicar em exibir) 
img_5 = "img5.png"
# Procura a posição da imagem na tela durante o tempo limite definido
try:
    # Variavel location irá armazenar as informações de altura, largura, eixo x e eixo y, com uma precisão de 90%
    location = pyautogui.locateOnScreen(img_5, confidence=0.9)
    if location:
        # Se a imagem for encontrada, obtém as coordenadas do centro da imagem
        center_x = location.left + location.width / 2
        center_y = location.top + location.height / 2
        # Movendo o mouse para as coordenadas da imagem e depois clicando
        pyautogui.moveTo(center_x, center_y, duration=1)
        pyautogui.click()      

except Exception as e:
        # Mensagem de erro para salvar caso alguma coisa dê errado
        print(f"Erro ao localizar a imagem: {e}")
sleep(2)

#Finalizar corte
finalizar_corte =navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[2]/div[2]/div/div[2]/div[3]/div[2]/div[1]/button[1]')
finalizar_corte.click()
sleep(2)

#Finalizar balde corte
finalizar_balde_corte =navegador.find_element(by=By.XPATH, value = '//*[@id="manage-content"]/div/div[3]/div[3]/div/div[2]/div[3]/div[2]/div[1]/button[1]')
finalizar_balde_corte.click()

sleep(50000)

