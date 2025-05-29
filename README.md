# 🐾 Farmina Zendesk Test Application

## 🌐 Live App: https://farminatest.fly.dev

This repository contains two main parts designed for a Zendesk-related test:

1. A web application built with Python (Flask) and styled using Bootstrap, allowing agents to simulate pet characteristics and search for products using Farmina's public API.

2. A dynamic HTML email template test for Zendesk, using conditional logic and variable placeholders to simulate personalized communication based on ticket data.

---

## 🇺🇸 English

### 💡 What does this app do?

The Flask application allows customer support agents to select options such as:

- Type of food (dry or wet)
- Type of pet (dog or cat)
- Life stage (puppy, adult, senior)
- Gestation / Lactation (yes or no)
- Special care conditions (fetched dynamically)

After submitting the form, the app sends a request to the Farmina API and displays matching products. Each result shows the product name, description, ingredients, and a direct link to the Farmina store. The interface is visually styled using Bootstrap and uses the official Farmina logo and color scheme for brand consistency.

The HTML email test (`teste.html`) was built for use within the Zendesk platform. It uses Zendesk template tags like `{{ticket.requester.name}}` and control structures such as `{{#if}}`, `{{else}}`, etc. The content layout is table-based to ensure consistent rendering across email clients. The header image changes dynamically depending on the animal type (dog, cat, or fallback to the Farmina logo).

---

## 🇧🇷 Português

### 💡 O que esse app faz?

A aplicação Flask permite que agentes de atendimento ao cliente selecionem:

- Tipo de alimento (seco ou molhado)
- Tipo de pet (cão ou gato)
- Fase da vida (filhote, adulto, sênior)
- Gestação / Lactação (sim ou não)
- Cuidados especiais (obtidos dinamicamente)

Após o envio do formulário, a aplicação consulta a API da Farmina e exibe os produtos compatíveis com os filtros escolhidos. Cada produto traz informações como nome, descrição, ingredientes e link para a loja oficial. A interface é estilizada com Bootstrap, utilizando o logo e cores da marca Farmina.

O teste de HTML (`teste.html`) foi feito para o Zendesk. Ele utiliza variáveis dinâmicas como `{{ticket.requester.name}}` e estruturas condicionais como `{{#if}}`. O layout é construído com tabelas (`<table>`) para garantir compatibilidade com os principais clientes de e-mail. A imagem do cabeçalho varia de acordo com o tipo de animal informado, com fallback para o logo da marca caso não haja informação.

