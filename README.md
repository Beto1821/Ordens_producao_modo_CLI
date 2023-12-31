# Sistema de Gerenciamento de Ordens de Produção 

Este é um sistema de gerenciamento de ordens de produção desenvolvido em Python que permite o registro de novas ordens de produção, listagem de ordens existentes, atualização de status, listagem de produtos cadastrados e cadastro de novos produtos. O sistema utiliza um banco de dados MySQL para armazenar as informações das ordens e dos produtos.

# Requisitos de Ambiente

Antes de executar o aplicativo, certifique-se de ter o ambiente configurado corretamente:

## 1. Crie o ambiente virtual para o projeto
python3 -m venv .venv && source .venv/bin/activate

## 2. Utilize o Docker para iniciar um servidor MySQL com as configurações necessárias. Certifique-se de ter o Docker instalado e execute o seguinte comando:

docker run --name production-orders-mysql -e MYSQL_ROOT_PASSWORD=senha_root -e MYSQL_DATABASE=production_orders -p 3306:3306 -d mysql:latest

Isso iniciará um contêiner MySQL com as configurações de conexão especificadas no arquivo database.py.

# Execução do Aplicativo

Para executar o aplicativo no modo de linha de comando, siga os passos abaixo:

## 1. Garanta que o ambiente virtual está ativado:

source .venv/bin/activate

## 2. Execute o aplicativo principal main.py:

python3 main.py

Isso iniciará o aplicativo de gerenciamento de ordens de produção. Você poderá escolher entre várias opções no menu, como registrar uma nova ordem, listar ordens existentes, atualizar status, listar produtos cadastrados e cadastrar novos produtos.

Certifique-se de preencher as informações de produtos e ordens conforme necessário.

O sistema utiliza o banco de dados MySQL para armazenar todas as informações das ordens e produtos, de acordo com as configurações definidas no arquivo database.py.

# Exemplos de retorno na execução:

### Exemplo de listagem de produtos cadastrado:

```
Produtos cadastrados:
Produto: bombom, Quantidade em Estoque: 10
Produto: chocolate, Quantidade em Estoque: 20
```

### Exemplo de cadastro de ordem para execução:

```
Nome do produto (ou 'exit' para cancelar): bombom
Quantidade desejada (ou 'exit' para cancelar): 20
Quantidade desejada maior que a disponível.
Quantidade desejada (ou 'exit' para cancelar): 5
Data de entrega (AAAA-MM-DD) (ou 'exit' para cancelar): 2024-01-01
Ordem de produção registrada com sucesso!
```

### Exemplo de listagem de ordens de produção

```
Ordens de produção:
ID Pedido: 1, Produto: bombom, Quantidade: 5, Data de Entrega: 2024-01-01, Status: Em andamento
ID Pedido: 2, Produto: chocolate, Quantidade: 10, Data de Entrega: 2024-02-01, Status: Em andamento
```

# Observações

- Certifique-se de que o servidor MySQL esteja em execução e configurado corretamente, de acordo com as instruções acima. Você pode acessar o banco de dados MySQL usando ferramentas como o MySQL Workbench ou qualquer outro cliente MySQL de sua escolha para visualizar e gerenciar os dados armazenados no banco de dados "production_orders" de acordo com as credenciais especificadas no arquivo database.py.

Print tabelas no Workbench:

![Exemplo de captura de tela](/workbench/Screenshot%202023-10-15%20at%2012.06.06.png)

![Exemplo de captura de tela](/workbench/Screenshot%202023-10-15%20at%2012.06.15.png)


- O sistema também fornece verificações de disponibilidade de produtos e data de entrega para garantir que as ordens possam ser atendidas com base nos materiais disponíveis.

- O arquivo orders.py contém funções para inserir, listar e atualizar ordens, bem como verificar se é possível produzir uma ordem com base na disponibilidade de materiais.

- O arquivo database.py contém as configurações de conexão ao banco de dados e funções relacionadas ao banco de dados, como criação de tabelas, inserção de produtos e verificação de produtos cadastrados.


Aproveite o sistema de gerenciamento de ordens de produção!
