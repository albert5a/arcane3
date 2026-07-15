# Arcane3

Aplicacao Django em desenvolvimento com uma primeira interface de cadastro de usuarios. O projeto esta organizado em torno do projeto Django `core` e do app `usuarios`.

## Estado atual

- Projeto Django criado com `manage.py` e configuracoes em `core/`.
- App `usuarios` registrado em `INSTALLED_APPS`.
- Rota administrativa padrao do Django em `/admin/`.
- Rota de cadastro em `/usuarios/cadastro/`.
- Template base global em `templates/base.html`.
- Tela de cadastro em `usuarios/templates/cadastro.html`.
- Arquivos estaticos em `templates/static/`.
- Banco SQLite local configurado em `db.sqlite3`.

## Stack principal

- Python 3.12, conforme ambiente virtual local.
- Django 6.0.1.
- SQLite para desenvolvimento local.
- Tailwind CSS carregado via CDN no template base.

O arquivo `requirements.txt` contem varias dependencias alem do Django. Para esta aplicacao, o nucleo usado ate aqui e o Django com seus recursos padrao de templates, rotas, arquivos estaticos e views.

## Estrutura do projeto

```text
.
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── usuarios/
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   └── templates/
│       └── cadastro.html
├── templates/
│   ├── base.html
│   └── static/
│       ├── assistente_virtual.png
│       ├── banner.jpg
│       ├── logo.webp
│       └── user.png
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Rotas

| Caminho | Origem | Descricao |
| --- | --- | --- |
| `/admin/` | `core.urls` | Painel administrativo padrao do Django. |
| `/usuarios/cadastro/` | `usuarios.urls` | Tela e envio do formulario de cadastro. |

## Funcionalidades implementadas

### Cadastro de usuario

A view `usuarios.views.cadastro` trata dois fluxos:

- `GET`: renderiza o template `cadastro.html`.
- `POST`: le dados enviados pelo formulario e retorna uma resposta HTTP de sucesso.

No estado atual, o cadastro ainda nao salva dados no banco. A view possui comentario indicando que a logica de persistencia ainda deve ser adicionada.

### Interface de cadastro

A tela de cadastro inclui:

- Logo da aplicacao.
- Campo `username`.
- Campo de senha.
- Campo de confirmacao de senha.
- Botao de envio.
- Link visual para usuarios que ja possuem conta.
- Botoes visuais de continuidade com Google e GitHub.
- Banner lateral exibido em telas grandes.

### Templates e arquivos estaticos

O template base carrega Tailwind CSS via CDN e expoe blocos Django para `head` e `body`.

Os arquivos estaticos estao configurados por `STATICFILES_DIRS` apontando para `templates/static`, com `STATIC_ROOT` em `staticfiles`. Tambem ha configuracao de media:

- `MEDIA_ROOT = BASE_DIR / "media"`
- `MEDIA_URL = "/media/"`

## Configuracoes relevantes

- `LANGUAGE_CODE = "pt-br"`
- `TIME_ZONE = "UTC"`
- `DEBUG = True`
- `ALLOWED_HOSTS = []`
- Banco padrao: SQLite em `db.sqlite3`
- Templates globais: `BASE_DIR / "templates"`

Estas configuracoes estao adequadas para desenvolvimento local. Antes de publicar a aplicacao, revise `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, arquivos estaticos e configuracoes de banco.

## Como executar localmente

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Aplique migracoes:

```bash
python manage.py migrate
```

4. Inicie o servidor:

```bash
python manage.py runserver
```

5. Acesse:

```text
http://127.0.0.1:8000/usuarios/cadastro/
```

## Pontos de atencao

- O app `usuarios` ainda nao possui modelos definidos.
- O formulario usa os campos `username`, `senha` e `confirmar_senha`, mas a view atualmente tenta ler `password`; isso precisa ser alinhado quando a persistencia for implementada.
- Os botoes de Google e GitHub sao apenas elementos visuais e ainda nao possuem autenticacao social configurada.
- Ainda nao existem testes automatizados implementados.
- O projeto nao esta com Git inicializado neste diretorio, entao este README foi criado a partir da leitura do estado atual dos arquivos.

## Proximos passos sugeridos

- Criar a persistencia de usuarios usando o sistema de autenticacao do Django.
- Validar senha e confirmacao de senha.
- Exibir mensagens de erro e sucesso no template.
- Implementar login/logout.
- Adicionar testes para a view de cadastro.
- Separar configuracoes sensiveis em variaveis de ambiente.
