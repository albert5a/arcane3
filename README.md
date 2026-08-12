# Arcane3

Aplicação Django em desenvolvimento para gestão jurídica, apresentada na interface como **JURI.AI**. O estado atual oferece uma página institucional, cadastro e login de usuários e uma área inicial para gestão de clientes.

## Funcionalidades

- Página inicial institucional com chamada para criação de conta.
- Cadastro persistido com o sistema de autenticação do Django.
- Validação de confirmação de senha, mínimo de oito caracteres e username duplicado.
- Login com criação de sessão e mensagens para credenciais inválidas.
- Cadastro e listagem de clientes vinculados ao usuário atual.
- Classificação de clientes como pessoa física (`PF`) ou jurídica (`PJ`) e como ativos ou inativos.
- Administração de clientes pelo Django Admin.
- Mensagens visuais de sucesso e erro.
- Testes automatizados da página inicial.

Os botões de Google e GitHub presentes nas telas são apenas elementos visuais; autenticação social ainda não está configurada.

## Stack principal

- Python 3.12.
- Django 6.0.1.
- SQLite para desenvolvimento local.
- Templates do Django.
- Tailwind CSS carregado via CDN.

O `requirements.txt` contém dependências adicionais, mas o núcleo utilizado neste estágio da aplicação é o Django e seus recursos nativos de autenticação, sessões, mensagens, templates, rotas e ORM.

## Estrutura do projeto

```text
.
├── core/
│   ├── settings.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── usuarios/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   ├── cadastro.html
│   │   ├── clientes.html
│   │   └── login.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── static/
│   │   ├── assistente_virtual.png
│   │   ├── banner.jpg
│   │   ├── logo.webp
│   │   └── user.png
│   ├── base.html
│   └── home.html
├── manage.py
├── requirements.txt
└── db.sqlite3
```

O banco `db.sqlite3`, o ambiente virtual e o arquivo `.env` são locais e permanecem ignorados pelo Git.

## Rotas

| Caminho | Nome da rota | Descrição |
| --- | --- | --- |
| `/` | `home` | Página inicial institucional. |
| `/admin/` | `admin` | Painel administrativo do Django. |
| `/usuarios/cadastro/` | `cadastro` | Exibição e processamento do cadastro de usuário. |
| `/usuarios/login/` | `login` | Exibição e processamento da autenticação. |
| `/usuarios/clientes/` | `clientes` | Listagem e cadastro de clientes do usuário atual. |

## Fluxos principais

### Cadastro de usuário

A view `usuarios.views.cadastro` aceita:

- `GET`: renderiza `cadastro.html`.
- `POST`: compara senha e confirmação, exige pelo menos oito caracteres, impede username duplicado e cria o usuário com `User.objects.create_user`.

Após um cadastro válido, o usuário é direcionado ao login. Falhas de validação retornam ao cadastro com uma mensagem explicativa.

### Login

A view `usuarios.views.login` autentica username e senha usando o backend padrão do Django. Credenciais válidas criam a sessão e direcionam para a área de clientes; credenciais inválidas retornam ao login com uma mensagem de erro.

### Gestão de clientes

Cada cliente possui:

- nome;
- e-mail único;
- tipo `PF` ou `PJ`;
- status ativo ou inativo;
- vínculo com um usuário do Django.

A consulta da tela usa `Cliente.objects.filter(user=request.user)`, restringindo a listagem aos registros associados ao usuário atual. O formulário modal cria novos registros e associa automaticamente o usuário da sessão.

## Como executar localmente

1. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Aplique as migrações:

```bash
python manage.py migrate
```

4. Inicie o servidor:

```bash
python manage.py runserver
```

5. Acesse `http://127.0.0.1:8000/`.

Para utilizar o Django Admin, crie antes um superusuário:

```bash
python manage.py createsuperuser
```

## Validação

Execute as verificações do Django e a suíte automatizada:

```bash
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```

A suíte atual contém dois testes para a home: disponibilidade da página e presença do link de cadastro.

## Configurações relevantes

- `LANGUAGE_CODE = "pt-br"`.
- `TIME_ZONE = "UTC"`.
- Templates globais em `BASE_DIR / "templates"`.
- Arquivos estáticos de origem em `templates/static`.
- Banco padrão SQLite em `db.sqlite3`.
- `DEBUG = True` e `ALLOWED_HOSTS = []`, adequados somente ao desenvolvimento local.

Antes de publicar a aplicação, mova a `SECRET_KEY` para uma variável de ambiente e revise `DEBUG`, `ALLOWED_HOSTS`, banco de dados, HTTPS e a entrega dos arquivos estáticos.

## Limitações conhecidas

- A rota `/usuarios/clientes/` ainda não aplica `login_required`; acessos anônimos diretos podem resultar em erro.
- Os cards de totais, a busca e o filtro da tela de clientes ainda são demonstrativos.
- A unicidade do e-mail de cliente é global, não por usuário.
- Ainda não existe fluxo de logout.
- Autenticação social não foi implementada.
- Cadastro, login e gestão de clientes ainda não possuem testes automatizados específicos.

## Próximos passos sugeridos

- Proteger a área de clientes e definir redirecionamentos para usuários anônimos.
- Implementar logout.
- Calcular indicadores e implementar busca e filtros de clientes.
- Ampliar os testes dos fluxos de autenticação e clientes.
- Validar os dados de cliente com formulários Django e tratar e-mails duplicados.
- Externalizar configurações sensíveis para variáveis de ambiente.
