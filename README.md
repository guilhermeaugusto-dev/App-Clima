# App do Clima

Uma aplicação Django para consulta de informações climáticas com sistema de autenticação.

## Funcionalidades

- Sistema de login e cadastro de usuários
- Dashboard para visualização de dados climáticos
- Interface moderna com design responsivo
- Autenticação personalizada

## Tecnologias Utilizadas

- Python 3.x
- Django 5.2.7
- SQLite (desenvolvimento)
- HTML5/CSS3
- Bootstrap (opcional)

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/SEU_USUARIO/app-do-clima.git
cd app-do-clima
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install django
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

6. Acesse http://127.0.0.1:8000/ no seu navegador

## Estrutura do Projeto

```
Projeto/
├── Clima/              # Configurações principais do Django
├── login/              # App de autenticação
├── cadastro/           # App de cadastro de usuários
├── dashboard/          # App do painel principal
├── templates/          # Templates HTML
├── static/            # Arquivos estáticos (CSS, JS, imagens)
├── manage.py          # Script de gerenciamento do Django
└── db.sqlite3         # Banco de dados SQLite
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.