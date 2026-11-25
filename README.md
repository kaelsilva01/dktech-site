
# DK TECH — Aplicação Web com Docker

Projeto de aplicação web desenvolvido para demonstrar conhecimentos práticos em desenvolvimento web, conteinerização, configuração de servidores e gerenciamento de aplicações utilizando Docker e Docker Compose.

## Tecnologias utilizadas

- HTML5
- CSS3
- Nginx Alpine
- Docker
- Docker Compose
- Git
- GitHub
- Docker Hub

## Estrutura do projeto

```text
projetoDK/
├── app/
│   └── index.html
├── website/
│   ├── index.html
│   └── style.css
├── .dockerignore
├── .gitignore
├── Dockerfile
├── compose.yaml
└── README.md
```

## Executar o projeto com Docker Compose

Clone o repositório:

```bash
git clone https://github.com/kaelsilva01/dktech-site.git
```

Acesse a pasta:

```bash
cd dktech-site
```

Crie a rede Docker utilizada pelo Compose:

```bash
docker network create minharede
```

Construa e inicie a aplicação:

```bash
docker compose up -d --build
```

Acesse no navegador:

http://localhost:8081

## Construção da imagem Docker

A imagem personalizada utiliza Nginx Alpine como imagem-base.

```bash
docker build -t dktech-site:v1 .
```

## Executar diretamente pelo Docker Hub

Também é possível baixar e executar a imagem já publicada:

```bash
docker pull silvass/dktech-site:v1
```

```bash
docker run -d --name dktech-publicado -p 8081:80 silvass/dktech-site:v1
```

Acesse:

http://localhost:8081

Imagem publicada:

https://hub.docker.com/r/silvass/dktech-site

## Verificar os containers

```bash
docker compose ps
```

## Consultar logs da aplicação

```bash
docker compose logs -f
```

## Objetivo do projeto

Demonstrar conhecimentos práticos em desenvolvimento web, conteinerização de aplicações, configuração de servidores web com Nginx, criação de imagens Docker, gerenciamento de containers e publicação de imagens no Docker Hub.

## Repositório

GitHub: https://github.com/kaelsilva01/dktech-site

Docker Hub: https://hub.docker.com/r/silvass/dktech-site