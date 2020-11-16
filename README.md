# Sistema de Agendamentos de Mensagens
Esse sistema foi desenvolvido visando realizar o agendamento de mensagens para redes sociais, então fi criado um modelo para rede sociais e um para agendamentos, antes de criar um agendamento você deve criar as "redes sociais", como por exemplo email, sms, push e whatsapp. Com a criação de dois modelos fica mais fácil de adaptar o sistema e adicionar novas opções.

Primeiramente você deve configurar o seu ambiente virtual, para isso você pode usar o virtalenv, com isso você vai isolar o seu ambiente do ambiente de outros projetos:
sudo apt install virtualenv
virtualenv .venv
source .venv/bin/activate

### Mas vc também pode deixar seu computador bagunçado instalando diretamente nele

## Instale o django versão 3.1.3:
pip3 install Django==3.1.3

## Executando o servidor (na home do projeto):
python3 manage.py runserver

## Depois disso você já pode fazer suas requisições para a API

Depois instale o mysqlclient em seu ambiente virtual
Para executar o sistema você deve rodar o comando python3 manage.py runserver, depois basta fazer as requisições http para a API

# Exemplos de requisições para a API
<div align="center" style="padding='3%'">
  <img src="consultandoaapiprints/1.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/2.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/3.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/4.png" class="img-fluid" style="" width="95%">
  <img src="consultandoaapiprints/5.png" class="img-fluid" style="" width="95%">
</div>

