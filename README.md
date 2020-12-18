# LuizaLabsFavorites
#### Desafio Luiza Labs
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/elzapuppo/LuizaLabsFavorites/blob/main/LICENSE" target="_blank">
    <img alt="License: GPL--3.0" src="https://img.shields.io/badge/License-GPL--3.0-yellow.svg" />
  </a>
</p>

Solução apresentada ao desafio proposto pela LuizaLabs desenvolvida utilizando Django, Python e SQLite.


https://documenter.getpostman.com/view/7914516/TVssj8dV


### Parâmetros de execução
| Parâmetro  | Propósito | Valor default |
|---|---|---|
| memory  | Define se as informações serão armazenadas em memória (SQLite) ou em um banco MySql | False |
| mysql_host  | Ip e porta do MySql | localhost:3306 |
| mysql_user  | Usuário de acesso ao MySql  | root |
| mysql_passwd  | Senha de acesso ao MySql  | admin |
| mysql_db | Schema do MySql utilizado pela aplicação | luizalabs |
| http_port | Porta que o servidor ficará ouvindo | 8888 |
| logging | Nível de apresentação de log (_debug_, _info_, _warning_, _error_ ou _none_) | info |
| log_file_prefix | Define o caminho do arquivo de log (sem informar esse parâmetro os logs serão exibidos no terminal) |  | 


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

Para acessar nossa plataforma de Marketplace da Lu, agora basta você abrir seu navegador e acessar através do endereço:
> http://localhost:8000

A página inicial mostra a documentação da API.

<ul>
        <li><code>client</code> <em>foreign key </em>
        -- Referência ao produto</li>
        <li><code>product</code> <em>foreign key </em>
        -- Referência ao  cliente </li>   
        <li><code>text</code> <em>string</em>
            -- Comentário sobre o produto</li> 
        <li><code>score</code> <em>decimal </em>
            -- Nota </li>           
        </ul>
        

        <h3>API Requests</h3>
        <p>Utilizando o Postman foi possível realizar os testes na API com a finalidade de verificação das urls fornecidas, como seguem os exemplos:</p>
        
        <h3>Brand</h3>
        <pre>POST <code>http://127.0.0.1/api/brands/</code></pre>
        {
            


## 📝 License

This project is [GPL--3.0](https://github.com/elzapuppo/LuizaLabsFavorites/blob/main/LICENSE) licensed.
