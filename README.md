# Prova 1 - Módulo 10 - Luana Dinamarca Parra 

A questão prática contempla a entrega de uma API de nível de maturidade 2 no modelo de maturidade de richardson.

Dessa maneira, os recursos permitem o usuário realizar um cadastro de um pedido, com o nome do usuário, email do usuário e a descrição do pedido, enviado como um json.

●      /pedidos: cadastrar um novo pedido, recebe um JSON e retorna um ID e retorna todos os pedidos cadastrados

●      /pedidos/<id>: retorna o pedido do ID fornecido. Se esse pedido não existir, retornar que não foi possível locallizar ele, da forma mais apropriada para atender as questões do problema proposto.

O recurso /pedidos/<id> ainda deve possibilitar editar o pedido e excluir ele, implementados em recursos distintos.

## Como executar?

Em primeiro lugar é necessário clonar o repositório com o seguinte comando:

```
git clone https://github.com/luanaparra/prova1_modulo9
```

Dessa maneira, é possível entrar na pasta `/src` e instalar as dependências:

```
python -m pip install -r requirements.txt
```

Por conseguinte, para rodar a implementação na pasta `/src`, execute o comando:
```
docker compose up
```