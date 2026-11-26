# DK TECH — Aplicação Web, API e Automação CI/CD

**Projeto de portfólio DevOps | Docker | Python | Nginx | GitHub Actions**

## Sobre o projeto

A DK TECH é uma aplicação web desenvolvida como projeto prático de portfólio para demonstrar conhecimentos em conteinerização, infraestrutura, integração entre serviços e automação de pipelines CI/CD.

A solução integra um site institucional, uma API desenvolvida em Python e um servidor Nginx configurado como Reverse Proxy.

A aplicação utiliza Docker Compose para orquestrar os serviços e GitHub Actions para automatizar a construção e publicação das imagens no Docker Hub.

## Tecnologias utilizadas

- HTML5, CSS3 e JavaScript
- Python 3
- Nginx Alpine
- Docker
- Docker Compose
- Docker Networking
- Docker Healthchecks
- Git e GitHub
- GitHub Actions
- Docker Hub
- YAML

## Arquitetura do projeto

```text
projetoDK/
│
├── .github/
│   └── workflows/
│       └── docker-publish.yml
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
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## Arquitetura da aplicação

A aplicação é composta por dois serviços principais:

| Serviço | Tecnologia | Porta |
|---|---|---|
| Site e Reverse Proxy | Nginx Alpine | 8081 |
| API | Python | 5000 |

### 1. Site e servidor Nginx

O Nginx é responsável por servir os arquivos estáticos do site e encaminhar as requisições destinadas à API.

### 2. API Python

A API foi desenvolvida utilizando o módulo `http.server` da biblioteca padrão do Python.

Endpoints disponíveis:

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Informações da API |
| GET | `/health` | Verificação de saúde |
| GET | `/api/` | API acessada pelo Nginx |
| GET | `/api/health` | Healthcheck acessado pelo Nginx |

### 3. Reverse Proxy

O Nginx encaminha as requisições recebidas em `/api/` para o serviço Python por meio da rede Docker.

Essa configuração permite que o navegador acesse a API pelo mesmo endereço utilizado pelo site.

### 4. Docker Compose e Networking

O Docker Compose gerencia os dois serviços, suas portas, imagens, políticas de reinicialização e verificações de saúde.

Os containers utilizam uma rede Docker externa chamada `minharede`.

### 5. Healthchecks

Foram configurados Healthchecks independentes:

- Nginx: verifica a disponibilidade da página inicial.
- API Python: verifica o endpoint `/health`.

Os serviços utilizam a política de reinicialização `unless-stopped`.

## Pipeline CI/CD

O projeto possui um pipeline automatizado utilizando GitHub Actions.

Quando alterações são enviadas para a branch `main`, nos caminhos configurados no workflow, o pipeline executa:

1. Checkout do código-fonte.
2. Configuração do Docker Buildx.
3. Autenticação no Docker Hub por meio de GitHub Secrets.
4. Construção da imagem Docker do site.
5. Publicação da imagem do site.
6. Construção da imagem Docker da API.
7. Publicação da imagem da API.

As imagens são publicadas com as tags `latest` e o identificador do commit.

### Imagens publicadas

**Site:**

https://hub.docker.com/r/silvass/dktech-site

**API:**

https://hub.docker.com/r/silvass/dktech-api

### Workflow

Arquivo responsável pela automação:

`.github/workflows/docker-publish.yml`

O pipeline também pode ser iniciado manualmente pelo GitHub Actions.

## Como executar o projeto localmente

### Pré-requisitos

- Docker Desktop instalado.
- Git instalado.
- Docker Compose disponível.

### 1. Clonar o repositório

```bash
git clone https://github.com/kaelsilva01/dktech-site.git
cd dktech-site
```

### 2. Criar a rede Docker

```bash
docker network create minharede
```

A rede é externa e compartilhada pelos serviços.

### 3. Construir e iniciar a aplicação

```bash
docker compose up -d --build
```

### 4. Verificar os containers

```bash
docker compose ps
```

Os serviços devem apresentar o estado `healthy` após a execução bem-sucedida dos Healthchecks.

## Acessar a aplicação

| Recurso | Endereço |
|---|---|
| Site | http://localhost:8081 |
| API direta | http://localhost:5000 |
| API pelo Nginx | http://localhost:8081/api/ |
| Healthcheck da API | http://localhost:8081/api/health |

## Exemplo de resposta da API

```json
{
  "projeto": "DK TECH",
  "status": "online",
  "mensagem": "API funcionando com sucesso!"
}
```

## Comandos úteis

Verificar os serviços:

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

## Competências demonstradas

- Criação e configuração de Dockerfiles.
- Conteinerização de aplicações.
- Orquestração com Docker Compose.
- Comunicação entre containers.
- Configuração de redes Docker.
- Configuração de Nginx como Reverse Proxy.
- Desenvolvimento de API com Python.
- Implementação de Healthchecks.
- Versionamento com Git.
- Automação CI/CD com GitHub Actions.
- Publicação de imagens no Docker Hub.
- Gerenciamento de Secrets para autenticação.

## Limitações e escopo

Este projeto tem finalidade educacional e de demonstração de competências DevOps.

A API utiliza o módulo `http.server` do Python para simplificar o aprendizado. Não é uma implementação destinada diretamente a ambientes de produção.

O projeto contempla integração contínua, construção e publicação de imagens. Não inclui deploy automatizado em servidor remoto.

## Repositório

GitHub:

https://github.com/kaelsilva01/dktech-site

Docker Hub:

https://hub.docker.com/u/silvass

---

# DK TECH — English Overview

DK TECH is a practical DevOps portfolio project featuring a web application, a Python API, Docker containerization, Nginx Reverse Proxy and automated CI/CD using GitHub Actions.

The project demonstrates:

- Docker and Docker Compose orchestration.
- Container networking and health checks.
- Python API development.
- Nginx Reverse Proxy configuration.
- Git and GitHub version control.
- Automated Docker image builds and publishing.
- GitHub Actions CI/CD pipelines.
- Docker Hub integration.

**Repository:** https://github.com/kaelsilva01/dktech-site

**Docker Hub:** https://hub.docker.com/u/silvass