# LuizaLabsFavorites
#### Desafio Luiza Labs
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/elzapuppo/LuizaLabsFavorites/blob/main/LICENSE" target="_blank">
    <img alt="License: GPL--3.0" src="https://img.shields.io/badge/License-GPL--3.0-yellow.svg" />
  </a>
</p>

Solução apresentada ao desafio proposto pela LuizaLabs desenvolvida utilizando Django, Python e SQLite.


## Executando a aplicação
1. No seu terminal, baixe o projeto através do comando:
  `git clone https://github.com/ElzaPuppo/LuizaLabsFavorites.git`

2. Entre na pasta do projeto
  `cd challengeapis`

3. Crie um ambiente virtual

- No mac/linux:
  `python3 -m venv venv_challengeapi`

- No windows:
  `python -m venv venv_challengeapi`

4. Ative seu ambiente virtual

- No mac/linux:
`source venv_challengeapi`

- No windows:
  - Se você estiver usando o terminal do Windows PowerShell o comando é:
  `venv_challengeapi\Scripts\activate`

  - No CMD:
  `venv_challengeapi\Scripts\activate.bat`

  - No terminal do VSCode
  `. myvenv\Scripts\activate.ps1`

5. Instale as dependências do projeto
- No mac/linux:
`pip3 install -r requirements.txt`

- No windows e algumas distribuições do linux:
`pip install -r requirements.txt`

6. Faça as migrações do banco de dados
`python manage.py migrate`

7. Crie seu usuário com poderes de administrador/superusuário:
 `python manage.py createsuperuser`
   - Forneça um nome, email e senha para este usuário

8. Entre na pasta api
`cd api`

9. Rode o servidor local
`python manage.py runserver`

Para acessar nossa plataforma de Favoritos, agora basta você abrir seu navegador e acessar através do endereço:
> http://localhost:8000

A página inicial mostra a documentação da API.



## 📝 License

This project is [GPL--3.0](https://github.com/elzapuppo/LuizaLabsFavorites/blob/main/LICENSE) licensed.
