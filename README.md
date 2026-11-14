# KILLUA Login

Protótipo de autenticação para contas próprias da plataforma KILLUA.

## O que faz
- Pede número de telefone ou e-mail e senha.
- Na primeira utilização, cria uma conta KILLUA.
- Nas utilizações seguintes, verifica a senha.
- Guarda apenas o hash da senha (não a senha em texto normal).
- Permite terminar sessão.

## Executar no computador
1. Instala Python 3.
2. Abre a pasta do projeto no terminal.
3. Executa: `pip install -r requirements.txt`
4. Executa: `python app.py`
5. Abre `http://127.0.0.1:5000`.

## Antes de publicar na Internet
- Define uma `SECRET_KEY` longa e aleatória nas variáveis de ambiente.
- Usa HTTPS.
- Usa uma base de dados persistente e backups.
- Acrescenta verificação de e-mail/telefone antes de permitir que alguém reivindique esse identificador. Sem verificação, alguém pode registar o e-mail ou número de outra pessoa.
- Não peças nem guardes senhas do Facebook, Google ou de qualquer outro serviço. Este formulário é exclusivamente para contas KILLUA.
- O SQLite local é adequado para demonstração; para um serviço público, configura uma base de dados gerida e armazenamento persistente no alojamento.

Este protótipo não está publicado e ainda não tem um link público.
