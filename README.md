
# DK TECH — Aplicação Web com Docker

Projeto de aplicação web desenvolvido para demonstrar a configuração, conteinerização e execução de um site utilizando Docker e Docker Compose.

## Tecnologias utilizadas

- HTML5
- CSS3
- Nginx
- Docker
- Docker Compose

## Estrutura do projeto

```text
projetoDK/
├── app/
├── website/
│   ├── index.html
│   └── style.css
├── .dockerignore
├── Dockerfile
├── compose.yaml
└── README.md
```

## Executar o projeto

Clone o repositório e acesse a pasta:

```bash
cd projetoDK
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

## Verificar os containers

```bash
docker compose ps
```

## Logs da aplicação

```bash
docker compose logs -f
```

## Objetivo

Demonstrar conhecimentos práticos em desenvolvimento web, conteinerização, configuração de servidores web e gerenciamento de aplicações com Docker Compose.
