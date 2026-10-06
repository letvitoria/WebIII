# Projeto Flask - Desenvolvimento Web III (IFRO)

Repositório acadêmico desenvolvido para a disciplina de **Desenvolvimento Web III** do curso Superior de Tecnologia em Sistemas para Internet do **IFRO Campus Porto Velho Zona Norte**.

---

## 👩‍💻 Aluna
* **Nome:** Letícia Vitória Lima Firmino[cite: 2]

---

## 🚀 Sobre o Projeto
Este projeto consiste no desenvolvimento progressivo de uma aplicação web em **Python** utilizando o microframework **Flask**. O objetivo da atividade é consolidar conceitos de rotas, templates HTML via Jinja2, passagem de parâmetros (via dicionários e URLs), métodos HTTP (GET e POST), mensagens *Flash* e controle de versão profissional utilizando **Git e GitHub**.

---

## 📂 Estrutura de Pastas
O projeto foi organizado para manter a lógica central em um único arquivo principal (`app.py`), isolando os templates e arquivos estáticos:

```text
meu_projeto/
│
├── t_templates/               # Pasta contendo os templates HTML (herança com base.html)
│   ├── base.html
│   ├── t_index.html
│   ├── t_contato.html
│   ├── t_usuario.html
│   └── t_login.html
│
├── static/                    # Arquivos estáticos da aplicação
│   ├── css/
│   │   └── estilo.css
│   ├── js/
│   └── imagens/
│
├── app.py                     # Arquivo principal da aplicação Flask (app_Leticia)
├── requirements.txt           # Dependências do projeto (gerado via pip freeze)
└── .gitignore                 # Arquivos ignorados pelo Git (venv/, __pycache__, etc.)