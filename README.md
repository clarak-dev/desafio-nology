# Desafio Nology - Estagiário de Dev 2026

Este projeto foi desenvolvido como solução para o desafio técnico do processo seletivo de estágio em desenvolvimento da Nology.

A proposta foi criar uma aplicação para calcular cashback com base nas regras de negócio apresentadas no desafio, além de registrar cada consulta feita pelo usuário em banco de dados PostgreSQL e exibir um histórico de consultas de acordo com o IP de acesso. :contentReference[oaicite:0]{index=0}

## Funcionalidades

- Cálculo de cashback com base no tipo de cliente, valor da compra e percentual de desconto
- Aplicação do bônus para clientes VIP
- Aplicação da promoção para compras acima de R$ 500
- Registro das consultas no banco de dados PostgreSQL
- Exibição do histórico de consultas por IP
- Interface web para preenchimento dos dados e visualização do resultado :contentReference[oaicite:1]{index=1}

## Regras de negócio consideradas

As regras utilizadas neste projeto foram baseadas nos documentos apresentados no desafio:

- o cashback base é de 5% sobre o valor final da compra, após os descontos
- clientes VIP recebem 10% de bônus sobre o cashback base
- em compras acima de R$ 500, o cliente recebe o dobro de cashback
- primeiro é calculado o cashback base e depois o bônus VIP :contentReference[oaicite:2]{index=2}

## Tecnologias utilizadas

- Python
- FastAPI
- HTML
- CSS
- JavaScript
- PostgreSQL

## Estrutura do projeto

```bash
desafio-nology/
├── api.py
├── cashback.py
├── database.py
├── index.html
├── style.css
├── respostas.txt
├── README.md
└── .env

Observação sobre a regra de promoção

Na promoção para compras acima de R$ 500, considerei que o dobro deve ser aplicado sobre o cashback calculado no sistema atual. Essa interpretação foi adotada porque o enunciado informa que a promoção deveria ser aplicada no sistema já existente. Por isso, o fluxo seguido foi: calcular o cashback base, aplicar o bônus VIP quando houver e, ao final, aplicar o dobro do cashback para compras acima de R$ 500.

Entrega

Além dos códigos desenvolvidos, também foi preparado o arquivo respostas.txt com base nas respostas das questões 2, 3 e 4, para organização do documento solicitado na entrega. O acesso à aplicação será disponibilizado por link público, conforme pedido no desafio.