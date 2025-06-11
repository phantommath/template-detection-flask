# Desafio Técnico: Detecção de Template em Vídeo

**Vaga:** Analista de Testes / QA  
**Autor:** Matheus Dorneles de Castro

---

## 📝 Descrição do Projeto

Este repositório contém uma aplicação web desenvolvida como parte de um desafio técnico para vaga de **Analista de Testes / QA**. O objetivo foi criar uma ferramenta capaz de:

1. Receber o upload de um vídeo (`video.mp4`) e de uma imagem-template (`template.jpg`).  
2. Processar o vídeo frame a frame usando **OpenCV** para localizar o template.  
3. Enviar em tempo real, via **WebSocket** (Flask-SocketIO), uma notificação ao frontend assim que o template for encontrado.  
4. Containerizar toda a solução com **Docker**.

Apesar de minha experiência prévia ter sido focada em automação de testes com **Selenium**, **Cypress** e **Appium**, aceitei este desafio técnico mesmo sabendo que teria de explorar novas bibliotecas e conceitos. Foi um aprendizado intenso — desde trabalhar com processamento de vídeo no backend até sincronizar eventos em tempo real no frontend — e estou muito orgulhoso do resultado entregue.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.9**  
- **Flask** + **Flask-SocketIO** (WebSocket)  
- **OpenCV** (processamento de frames)  
- **Threading** / **Background Tasks**  
- **HTML**, **JavaScript** (frontend leve)  
- **Docker** (Dockerfile otimizado sobre imagem `python:3.9-slim`)

---

## 📦 Estrutura do Repositório

    /
    ├─ app.py                  # Aplicação Flask + SocketIO + OpenCV
    ├─ Dockerfile              # Containerização da aplicação
    ├─ requirements.txt        # Dependências Python
    ├─ static/
    │  ├─ index.html           # Página de upload e status
    │  └─ script.js            # Lógica de WebSocket no cliente
    ├─ templates/
    │  └─ layout.html          # Layout base (se usado)
    ├─ tests/
    │  └─ test_app.py          # Testes unitários / de integração
    ├─ uploads/                # Pasta para armazenamento temporário
    │  └─ .gitkeep             # Placeholder (conteúdo ignorado)
    ├─ README.md               # Este arquivo
    └─ .gitignore              # Padrões de arquivos a ignorar

---

## ⚙️ Instruções de Uso

1. **Build da imagem Docker**

    docker build -t template-app .

2. **Executar o container**

    docker run --rm -p 5000:5000 template-app

    - Acesse em `http://localhost:5000`.

3. **Workflow de upload**

    - Selecione o arquivo de vídeo (`.mp4`) e a imagem-template (`.jpg`).  
    - Clique em **Enviar**.  
    - O frontend exibirá “Procurando…”.  
    - Ao encontrar o template, receberá:

        Template encontrado no frame X

    - Se não for detectado até o fim do vídeo, exibirá “Não encontrado”.

---

## 📣 Agradecimentos

Este projeto me desafiou a sair do meu conforto em automação de testes tradicionais e explorar processamento de vídeo e comunicação em tempo real. Estou muito satisfeito com o que entreguei e ansioso para discutir os detalhes em uma entrevista!  
— Matheus Dorneles de Castro
