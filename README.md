<h1 align="center" style="font-weight: bold;">Comercial Alegria</h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#started">Introdução</a> • 
</p>

<p align="left">
    <b>Este é um projeto de E-commerce para um pequeno comércio local criado para colocar em prática conhecimentos e conceitos de programação com Django e python.</b>
</p>

<h2 id="technologies">💻 Tecnologias</h2>

- Python
- Django
- Pipenv
- Docker

<h2 id="started">🚀 Como começar</h2>

<h3>Pré-requisitos:</h3>

- [Python](https://python.org.br/instalacao-linux/)
- [Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git)
- [Pipenv](https://blog.rocketseat.com.br/domine-o-pipenv-otimizando-a-criacao-de-ambientes-virtuais-em-python/#:~:text=Instalar%20o%20Pipenv%20%C3%A9%20um,incluindo%20Windows%2C%20macOS%20e%20Linux.)

<h3>Clonando e configurando o projeto localmente:</h3>

A seguir está o passo a passo para clonar localmente e configurar o projeto.

```bash
git clone https://github.com/DerickDevCode/mercado-alegria.git
```

<h3>Configurações de variáveis de ambiente:</h2>

Use o arquivo `env-sample` como referência para criar o seu arquivo `.env` contendo as variáveis de ambiente do projeto

```yaml
DEBUG = False
SECRET_KEY = defina sua chave secreta

# Substituir pelos valores corretos de acordo com o arquivo docker-compose.yml
DATABASE_URL = postgres://postgres:postgres@localhost/testdb

ALLOWED_HOSTS = localhost, 127.0.0.1
SENTRY_DSN=
INTERNAL_IPS=127.0.0.1

# Armazena a URL padrão do site
BASE_URL_COMERCIAL_ALEGRIA=127.0.0.1:8000

# Configurações do AWS
AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY =
AWS_STORAGE_BUCKET_NAME =

# configurações de Email, você deve configurar as variáveis do seu smtp de email aqui
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=25
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=example@gmail.com

# Credenciais mercado pago, você deve configurar o seu token do mercado pago aqui
TOKEN_MERCADO_PAGO=token_de_credenciais_do_mercado_pago
```

<h3>Iniciando</h3>

Comandos para iniciar o projeto

```bash
# Instala o pipenv.
pip install pipenv
```

```bash
# Instala apenas as dependências de produção.
pipenv sync

# Instala as dependências de desenvolvimento (para desenvolvedores).
pipenv sync --dev
```

```bash
# Instala o Docker.
sudo apt remove docker docker-engine docker.io containerd runc

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt update

sudo apt install -y docker-ce
```

```bash
# Sobe o banco de dados através do Docker.
docker-compose up
```

```bash
# Realiza as migrações.
python manage.py migrate

# Realiza a coleta de arquivos estáticos.
python manage.py collectstatic
```

```bash
# Executa o servidor de desenvolvimento local.
python manage.py runserver
```
Agora você já tem o projeto rodando em seu ambiente local.
