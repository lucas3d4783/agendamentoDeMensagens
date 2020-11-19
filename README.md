# Sistema de Agendamentos de Mensagens
Esse sistema foi desenvolvido visando realizar o agendamento de mensagens para redes sociais, então fi criado um modelo para rede sociais e um para agendamentos, antes de criar um agendamento você deve criar as "redes sociais", como por exemplo email, sms, push e whatsapp. Com a criação de dois modelos fica mais fácil de adaptar o sistema e adicionar novas opções.

## Primeiro você deve clonar o repositório do github para a sua máquina:
git clone https://github.com/lucas3d4783/agendamentoDeMensagens.git

## Então acesse o diretório do projeto:
cd agendamentoDeMensagens/

## Depois ative o seu ambiente virtual onde você vai trabalhar:
source .venv/bin/activate

## Então você deve instalar o gerenciador de pacotes Python pip3
sudo apt install python3-pip

## Então você pode instalar o framework django:
pip3 install Django==3.1.3

## E depois isntalar o django Rest Framework que e voltado para a criação de APIs
pip3 install djangorestframework==3.12.2

## Instalando as dependências para instalar o mysqlclient:
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

## Instale o mysqlclient:
pip3 install mysqlclient

## Você pode alterar as informações do SGBD e da base de dados no seguinte arquivo:
vim schedulingmessages/settings.py

## Vale ressaltar que se não for feito alterações na configuração da sua base de dados, você deve ter o database com o nome "schedulingmessages" em seu SGBD localizado em sua máquina local com o usuário "lucas" e com a senha "MySQL1999!" na porta padrão do MySQL.

## Faça as migrações dos modelos para a base dados configurada no item anterior:
python3 manage.py migrate

## Chegou o momento da verdade! Execute o seguinte comando para iniciar o servidor:
python3 manage.py runserver
### Ou indicando o IP e a porta que o servidor deve rodar:
python3 manage.py runserver 127.0.0.1:8000

## Depois disso você já pode fazer suas requisições para a API

# Exemplos de requisições para a API
<div align="center" style="padding='3%'">
  <img src="consultandoaapiprints/1.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/2.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/3.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/4.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/5.png" class="img-fluid" style="" width="95%">
</div>

