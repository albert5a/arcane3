# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato mantém uma seção de trabalho atual e registrará entregas por versão quando o projeto passar a usar releases ou tags.

## [Não lançado]

### Adicionado

- Página inicial institucional da JURI.AI na rota `/`, com apresentação do produto e links para o cadastro.
- Testes automatizados para validar a disponibilidade da home e seu link para a tela de cadastro.
- Persistência de usuários por meio do sistema de autenticação do Django.
- Validações no cadastro para confirmação da senha, tamanho mínimo de oito caracteres e username duplicado.
- Mensagens visuais de sucesso e erro nas telas de cadastro e login.
- Tela e fluxo de login com autenticação de credenciais e criação de sessão.
- Modelo `Cliente` com nome, e-mail único, tipo de pessoa, status e vínculo com o usuário responsável.
- Migração inicial do app `usuarios` para criação da tabela de clientes.
- Registro do modelo `Cliente` no Django Admin.
- Tela de clientes com listagem dos registros do usuário atual e formulário modal para novos cadastros.
- Mensagem de confirmação após o cadastro de um cliente.
- Estilos do framework de mensagens do Django configurados em `MESSAGE_TAGS`.

### Alterado

- O cadastro deixou de retornar uma resposta HTTP demonstrativa e agora cria o usuário no banco de dados.
- A tela de cadastro passou a exibir mensagens de validação e a direcionar usuários existentes para o login.
- Usuários autenticados são redirecionados para a tela de clientes após o login.

### Limitações conhecidas

- A rota de clientes ainda não possui proteção explícita com `login_required`; acessos anônimos diretos podem resultar em erro.
- Os indicadores, a busca e o filtro exibidos na tela de clientes ainda são apenas visuais.
- O campo de e-mail de `Cliente` é único globalmente, inclusive entre usuários responsáveis diferentes.
- Os botões de Google e GitHub ainda não executam autenticação social.
- O fluxo de logout ainda não foi implementado.
- A cobertura automatizada atual contempla somente a página inicial; cadastro, login e clientes ainda precisam de testes específicos.

## [0.1.0] - Estado inicial documentado

### Adicionado

- Estrutura inicial do projeto Django com o módulo `core` e o app `usuarios`.
- Painel administrativo padrão do Django em `/admin/`.
- Primeira versão da rota, view e interface de cadastro de usuários.
- Template base com Tailwind CSS via CDN.
- Configuração de templates globais, arquivos estáticos, mídia e banco SQLite local.
- Documentação inicial do projeto em `README.md`.
- Registro inicial do histórico funcional em `CHANGELOG.md`.
