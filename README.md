# Automação de Previsão do Tempo por E-mail

## Sobre o Projeto

Este projeto foi desenvolvido como atividade prática do **Projeto 02 – Automação de Processos**, com o objetivo de automatizar o envio diário de informações climáticas para um gestor. A aplicação consulta dados meteorológicos em tempo real por meio da API OpenWeather, obtendo informações das capitais da Região Sudeste do Brasil: Belo Horizonte, São Paulo, Rio de Janeiro e Vitória. Após coletar os dados, o sistema organiza as informações e gera automaticamente um relatório contendo o status atual do clima, a temperatura mínima e a temperatura máxima de cada cidade.

Para concluir o processo, foi utilizada uma automação de interface gráfica que acessa o Gmail, preenche os campos necessários e envia o e-mail automaticamente. Durante o desenvolvimento foram aplicados conceitos fundamentais da linguagem Python, como listas, dicionários, estruturas de repetição, consumo de APIs e manipulação de dados JSON, além da utilização de bibliotecas voltadas para integração de dados e automação de processos.

---

## Tecnologias Utilizadas

### Linguagem

- Python 3

### Bibliotecas

- Requests
- PyAutoGUI
- Pyperclip
- Webbrowser
- Time

### API

- OpenWeather API

---

## Conceitos Aplicados

O desenvolvimento do projeto envolveu a aplicação dos seguintes conceitos:

- Listas
- Dicionários
- Estruturas de repetição
- Consumo de APIs REST
- Manipulação de dados JSON
- Automação de processos
- Automação de interface gráfica

---

## Funcionamento

O sistema inicia realizando requisições à API OpenWeather para obter informações meteorológicas atualizadas das capitais da Região Sudeste. Os dados retornados são armazenados em uma lista de dicionários e utilizados para montar automaticamente o corpo do e-mail.

Após a geração do relatório, a automação abre o Gmail, preenche o destinatário, o assunto e o conteúdo da mensagem, realizando o envio de forma automática através da biblioteca PyAutoGUI.

---

## Exemplo de E-mail Gerado

```text
Prezado Gestor,

Segue abaixo os dados climáticos das cidades solicitadas:

Cidade: Belo Horizonte
Status atual: céu limpo
Temperatura Mínima: 15°C
Temperatura Máxima: 27°C

Cidade: São Paulo
Status atual: nublado
Temperatura Mínima: 14°C
Temperatura Máxima: 23°C

Cidade: Rio de Janeiro
Status atual: poucas nuvens
Temperatura Mínima: 19°C
Temperatura Máxima: 30°C

Cidade: Vitória
Status atual: chuva leve
Temperatura Mínima: 21°C
Temperatura Máxima: 28°C

Atenciosamente,
Equipe de Desenvolvimento
```

---

## Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/mcscarpa/AutomacaoProcessos.git
```

### 2. Instale as dependências

```bash
pip install requests pyautogui pyperclip
```

### 3. Execute a aplicação

```bash
python main.py
```

---

## ⚠️ Observações

- É necessário possuir uma chave de acesso válida da API OpenWeather.
- O usuário deve estar previamente autenticado em uma conta Gmail.
- As coordenadas utilizadas pelo PyAutoGUI podem variar de acordo com a resolução da tela e a configuração do navegador.
- Caso necessário, ajuste os valores utilizados nos comandos `click()` para o seu ambiente.

---
por @mcscarpa
