<h1 align="center" style="font-weight: bold;">Comercial Alegria</h1>

<p align="center">
 <a href="#tech">Tecnologias</a> • 
 <a href="#introduction">Introdução</a> • 
 <a href="#starting">Iniciando</a> •
 <a href="#frontend">Front-end</a>
</p>

<p align="left">
    <b>Este é um projeto de E-commerce para um pequeno comércio local criado para colocar em prática conhecimentos e conceitos de programação com Django e python.</b>
</p>

<h2 id="tech">💻 Tecnologias</h2>

- Python
- Django
- Git
- GitHub Actions
- Flake8
- Pipenv
- Docker
- PostgreSQL
- Pytest
- Bootstrap

<h2 id="introduction">🚀 Como começar</h2>

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

# Variáveis do docker-compose
POSTGRES_PASSWORD=
POSTGRES_USER=
POSTGRES_DB=

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

<h3 id="starting">Iniciando:</h3>

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
docker-compose up -d
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

<h2 id="frontend">🎨 Conhecendo o Projeto</h2>

Conheça o visual e as funcionalidades do site para ter uma melhor experiência.

Esta é a página inicial onde iremos começar:
![site-home.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-home.webp)

<h3>Como navegar pelo site?</h3>

Algumas funcionalidades são acessíveis apenas para usuários logados, para isso você precisa fazer o cadastro e criar sua
conta. Por enquanto, vejamos as funcionalidades disponíveis a todos os usuários.

Ao navegar um pouco para baixo você verá os produtos disponíveis para compra. Clicando neles será redirecionado para uma
página com mais detalhes:
![site-produto-detalhe.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-produto-detalhe.webp)

Aqui você verá várias informações sobre o produto, também poderá ser direcionado a uma página com produtos filtrados de
acordo com a marca ao clicar na marca do produto indicada pela seta a direita, assim como uma página de produtos
filtrada pelo departamento, categoria ou subcategoria, indicado pela seta a esquerda.

<h3>Carrinho de compras</h3>

Observe que no canto superior direito há um ícone de carrinho de compras, é lá que você deve adicionar seus produtos
para finalizar sua compra. Você pode adicionar produtos ao carrinho pela página de detalhes do produto mostrada acima ou
nos cards de produtos das outras páginas de exibição.

Esta é a página do seu carrinho de compras, aqui serão exibidos os seus produtos do carrinho e as informações de
quantidades e valores:
![site-carrinho.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-carrinho.webp)

Como você deve ter notado, para efetivamente concluir sua compra, deve realizar o cadastro no site e logar na sua conta.

<h3>Cadastro e funcionalidades restritas</h3>

Como havia dito anteriormente, algumas funcionalidades estão disponíveis apenas para usuários logados, e a finalização
da compra é uma delas. Para realizar o cadastro, clique no ícone "Conecte-se" ao lado do carrinho de compras que você
conheceu anteriormente, ele irá abrir um menu com as opções de login e cadastro.

Na página de cadastro, preencha as informações e crie sua conta, você será logado automaticamente após se cadastrar.
![site-cadastro.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-cadastro.webp)

Caso já possua uma conta, faça login na página de login:
![site-login.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-login.webp)

Agora com um usuário logado, você terá acesso ao perfil de usuário.
![site-perfil.webp](mercado%2Fbase%2Fstatic%2Fimg%2Fsite-perfil.webp)

Nele você pode editar o seu perfil, alterar sua senha e também adicionar e ver seus Favoritos. Para adicionar um produto
aos favoritos você deve clicar no ícone de coração que se localiza no canto superior direito dos cards de produtos, para
remover é só clicar novamente.

Agora que você está logado poderá finalizar sua compra. Clique no botão "Finalizar compra" na sua página do carrinho,
você será redirecionado para a página de pagamentos do Mercado Pago.

Agora você conheceu as principais funcionalidades do site, sinta-se livre para fazer suas compras!
