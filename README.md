# DK TECH — Aplicação Web e API com Docker

Projeto autoral desenvolvido para demonstrar conhecimentos práticos em conteinerização, configuração de servidores web, desenvolvimento de API e gerenciamento de aplicações utilizando Docker e Docker Compose.

O projeto possui dois serviços independentes:

- **Site:** aplicação web estática servida pelo Nginx.
- **API:** serviço desenvolvido em Python, responsável por retornar informações em formato JSON.

## Tecnologias utilizadas

- HTML5 e CSS3
- Python 3.12
- Nginx Alpine
- Docker
- Docker Compose
- Docker Networking
- Git e GitHub
- Docker Hub

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
│   └── style.css
│
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── .gitignore
└── README.md
```

## Serviços da aplicação

| Serviço | Tecnologia | Porta |
|---|---|---|
| Site | Nginx Alpine | 8081 |
| API | Python 3.12 | 5000 |

Os serviços são executados em containers separados e conectados por uma rede Docker externa chamada `minharede`.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/kaelsilva01/dktech-site.git
```

### 2. Acessar a pasta

```bash
cd dktech-site
```

### 3. Criar a rede Docker

```bash
docker network create minharede
```

Caso a rede já exista, não é necessário criá-la novamente.

### 4. Construir e iniciar os serviços

```bash
docker compose up -d --build
```

### 5. Verificar os containers

```bash
docker compose ps
```

## Acessar a aplicação

**Site web:**

http://localhost:8081

**API:**

http://localhost:5000

A API retorna uma resposta JSON semelhante a esta:

```json
{
  "projeto": "DK TECH",
  "status": "online",
  "mensagem": "API funcionando com sucesso!"
}
```

## Construção da imagem Docker do site

A imagem do site utiliza Nginx Alpine como imagem-base.

```bash
docker build -t dktech-site:v1 .
```

## Imagem publicada no Docker Hub

A imagem do site está disponível publicamente no Docker Hub.

**Baixar a imagem:**

```bash
docker pull silvass/dktech-site:v1
```

**Executar a imagem:**

```bash
docker run -d --name dktech-publicado -p 8082:80 silvass/dktech-site:v1
```

A aplicação poderá ser acessada em:

http://localhost:8082

## Gerenciamento e diagnóstico

**Verificar os containers:**

```bash
docker compose ps
```

**Consultar os logs:**

```bash
docker compose logs -f
```

**Parar os serviços:**

```bash
docker compose down
```

## Objetivo e conhecimentos demonstrados

Este projeto demonstra a aplicação prática de conhecimentos em:

- Criação e configuração de Dockerfiles.
- Construção de imagens Docker personalizadas.
- Execução de múltiplos containers.
- Orquestração de serviços com Docker Compose.
- Configuração de redes Docker.
- Hospedagem de aplicação web com Nginx.
- Desenvolvimento e execução de API Python.
- Publicação de imagem Docker no Docker Hub.
- Versionamento de código com Git e GitHub.

## Links do projeto

**GitHub:**  
https://github.com/kaelsilva01/dktech-site

**Docker Hub:**  
https://hub.docker.com/r/silvass/dktech-site

---

*Projeto autoral desenvolvido para fins de demonstração de conhecimentos práticos em tecnologia e infraestrutura de aplicações.*