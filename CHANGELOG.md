# Changelog

Todas as mudancas relevantes deste projeto serao documentadas neste arquivo.

O formato segue a ideia de manter uma secao de trabalho atual e registrar entregas por versao quando o projeto passar a usar releases/tags.

## [Nao lancado]

### Adicionado

- Estrutura inicial de projeto Django com modulo principal `core`.
- Arquivo `manage.py` para comandos administrativos do Django.
- Configuracao de URL principal em `core/urls.py`.
- Rota do painel administrativo em `/admin/`.
- App `usuarios` criado e registrado em `INSTALLED_APPS`.
- Arquivo de rotas do app `usuarios`.
- Rota `/usuarios/cadastro/` apontando para a view de cadastro.
- View `cadastro` com suporte a requisicoes `GET` e `POST`.
- Renderizacao do template de cadastro em requisicoes `GET`.
- Resposta HTTP simples de sucesso apos envio `POST` do formulario.
- Template global `templates/base.html` com carregamento de Tailwind CSS via CDN.
- Tela de cadastro em `usuarios/templates/cadastro.html`.
- Formulario visual com campos de username, senha e confirmacao de senha.
- Botao principal de cadastro.
- Link visual para usuario que ja possui conta.
- Botoes visuais para continuidade com Google e GitHub.
- Uso de logo e banner por meio do sistema de arquivos estaticos do Django.
- Pasta `templates/static` com imagens da interface.
- Configuracao de templates globais em `BASE_DIR / "templates"`.
- Configuracao de arquivos estaticos com `STATICFILES_DIRS` e `STATIC_ROOT`.
- Configuracao inicial de arquivos de media com `MEDIA_ROOT` e `MEDIA_URL`.
- Banco SQLite local configurado em `db.sqlite3`.
- Internacionalizacao configurada com `LANGUAGE_CODE = "pt-br"`.

### Estado atual conhecido

- O cadastro ainda nao persiste usuarios no banco de dados.
- O app `usuarios` ainda nao possui modelos.
- Os botoes de Google e GitHub ainda nao executam autenticacao social.
- A view le `password`, enquanto o template envia `senha`; esse alinhamento ainda precisa ser corrigido.
- Ainda nao ha testes automatizados alem do arquivo padrao `usuarios/tests.py`.

## [0.1.0] - Estado inicial documentado

### Adicionado

- Documentacao inicial do projeto em `README.md`.
- Registro inicial do historico funcional em `CHANGELOG.md`.
