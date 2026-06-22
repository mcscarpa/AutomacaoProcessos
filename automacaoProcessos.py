
import webbrowser
import pyautogui
import pyperclip
import requests
import time

chave_API = "SUA_CHAVE_API"

cidade = "Belo Horizonte"
endereco = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_API}&lang=pt_br&units=metric"
requisicao = requests.get(endereco)

cidades = ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Vitória"]
cidades_dic = []
for indice in range(4):
    endereco = f"https://api.openweathermap.org/data/2.5/weather?q={cidades[indice]}&appid={chave_API}&lang=pt_br&units=metric"
    requisicao = requests.get(endereco)
    cidades_dic.append(requisicao.json())

corpo_email = f"""
Prezado Gestor,
Segue abaixo os dados climáticos das cidades solicitadas:

Cidade: {cidades[0]}
Status atual: {cidades_dic[0].get("weather")[0]["description"]}
Temperatura Mínima: {cidades_dic[0].get("main")["temp_min"]}°C
Temperatura Máxima: {cidades_dic[0].get("main")["temp_max"]}°C

Cidade: {cidades[1]}
Status atual: {cidades_dic[1].get("weather")[0]["description"]}
Temperatura Mínima: {cidades_dic[1].get("main")["temp_min"]}°C
Temperatura Máxima: {cidades_dic[1].get("main")["temp_max"]}°C

Cidade: {cidades[2]}
Status atual: {cidades_dic[2].get("weather")[0]["description"]}
Temperatura Mínima: {cidades_dic[2].get("main")["temp_min"]}°C
Temperatura Máxima: {cidades_dic[2].get("main")["temp_max"]}°C

Cidade: {cidades[3]}
Status atual: {cidades_dic[3].get("weather")[0]["description"]}
Temperatura Mínima: {cidades_dic[3].get("main")["temp_min"]}°C
Temperatura Máxima: {cidades_dic[3].get("main")["temp_max"]}°C

Atenciosamente,
Equipe de Desenvolvimento

"""

pyautogui.PAUSE = 5
webbrowser.open("www.gmail.com")
time.sleep(10)
pyautogui.click(x=47, y=218)
pyperclip.copy("EMAIL_GESTOR")
time.sleep(5)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy("Previsão do Tempo")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(corpo_email)
pyautogui.hotkey("ctrl", "v")
pyautogui.click(x=1132, y=1018)

