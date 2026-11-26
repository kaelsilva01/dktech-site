# DK TECH — Aplicação Web e API com Docker

Projeto autoral desenvolvido para demonstrar conhecimentos práticos em conteinerização, configuração de servidores web, desenvolvimento de API e gerenciamento de aplicações utilizando Docker e Docker Compose.

O projeto reúne um site institucional, uma API desenvolvida em Python e um servidor Nginx configurado como Reverse Proxy.

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- Python 3
- Nginx
- Docker
- Docker Compose
- Docker Networking
- Healthchecks
- Git e GitHub

## Arquitetura do projeto

```text
projetoDK/
│
├── api/
│   ├── Dockerfile
│   └── app.py
│
├── website/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Dockerfile
├── nginx.conf
└── compose.yaml
```

## Serviços da aplicação

| Serviço | Tecnologia | Porta |
|---|---|---|
| Site | Nginx Alpine | 8081 |
| API | Python | 5000 |

### Site — Nginx

O Nginx é responsável por disponibilizar o site e encaminhar as requisições destinadas à API.

### API — Python

A API foi desenvolvida utilizando o módulo `http.server` da biblioteca padrão do Python.

Endpoints disponíveis:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Retorna informações da API |
| GET | `/health` | Verifica a saúde da API |
| GET | `/api/` | Acessa a API pelo Nginx |
| GET | `/api/health` | Verifica a API pelo Nginx |

### Reverse Proxy

O Nginx encaminha as requisições recebidas em `/api/` para o serviço Python, utilizando a rede interna do Docker.

Isso permite que o navegador acesse a API por meio do mesmo endereço do site.

### Healthchecks

Foram configurados Healthchecks nos dois serviços:

- Nginx: verifica se a página inicial está respondendo.
- API Python: verifica se o endpoint `/health` está disponível.

Os containers utilizam `restart: unless-stopped`.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/kaelsilva01/dktech-site.git
cd dktech-site
```

### 2. Criar a rede Docker

```bash
docker network create minharede
```

A rede é externa e compartilhada pelos serviços da aplicação.

### 3. Construir e iniciar os containers

```bash
docker compose up -d --build
```

### 4. Verificar os containers

```bash
docker compose ps
```

Os serviços devem aparecer com status `healthy` após os Healthchecks serem executados com sucesso.

## Acessar a aplicação

- Site: http://localhost:8081
- API direta: http://localhost:5000
- API pelo Nginx: http://localhost:8081/api/
- Healthcheck da API: http://localhost:8081/api/health

## Exemplo de resposta da API

```json
{
  "projeto": "DK TECH",
  "status": "online",
  "mensagem": "API funcionando com sucesso!"
}
```

## Comandos úteis

Verificar os containers:

```bash
docker compose ps
```

Visualizar os logs:

```bash
docker compose logs -f
```

Visualizar os logs da API:

```bash
docker compose logs -f api
```

Verificar a saúde dos containers:

```bash
docker inspect app-compose --format '{{.State.Health.Status}}'
docker inspect dktech-api --format '{{.State.Health.Status}}'
```

Parar os serviços:

```bash
docker compose down
```

## Docker Hub

Imagem do site disponível no Docker Hub:

https://hub.docker