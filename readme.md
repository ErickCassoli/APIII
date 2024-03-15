# Projeto Django de Manipulação de Dados

Este é um projeto Django simples que demonstra como manipular dados através de requisições POST e GET usando uma API RESTful e renderização de template.

## Funcionalidades

- Aceita requisições POST com dados em formato JSON para atualizar o banco de dados.
- Responde a requisições GET para exibir os dados mais recentes em uma template HTML.

## Instalação

1. Clone o repositório para sua máquina local:

```
git clone https://github.com/ErickCassoli/APIII.git
```

2. Navegue até o diretório do projeto:

```
cd APIII
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```
python -m venv .env
```
```
source .env/bin/activate
```
ou
```
.env\Scripts\activate
```

4. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

5. Execute as migrações do banco de dados:

```
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```
python manage.py runserver
```

O servidor estará disponível em `http://127.0.0.1:8000/`.

## Uso

Você pode usar o Postman ou fazer solicitações HTTP para interagir com o endpoint `http://127.0.0.1:8000/` via metodo POST.

### Requisição POST:

Faça uma solicitação POST para `http://127.0.0.1:8000/` com os dados em formato JSON no corpo da solicitação.

Exemplo de dados:

```json
{
    "Sensor": true,
    "Botao": false,
    "LigaRobo": true,
    "ResetContador": false,
    "ValorContagem": 10
}
```

### Requisição GET:

Faça uma solicitação GET para `http://127.0.0.1:8000/` para exibir os dados mais recentes em uma template HTML.