# DIO: Sistema Bancário Python

App simples de um sistema bancário para um usuário.

### NOTA: O app não armazena dados entre as sessões.

## Como executar?

**Passo 1:** Clone este repositório;

**Passo 2:** Execute o comando:
```bash
python desafio.py
```

## Como usar?

Há quatro opções. Digite qualquer uma destas letras para executar a devida ação:
  - [d] ("Depositar");
  - [s] ("Sacar");
  - [e] ("Extrato"); e
  - [q] ("Sair").

### Depositar:
- Insira qualquer valor maior do que 0 para armazená-lo.

### Sacar:
- Digite qualquer valor maior do que 0 para retirá-lo.
  - Os valores devem ser menores do que o saldo atual, e há um limite de R$500.00 por transação.
  - Não é possível realizar mais de 3 saques por execução.

### Extrato:
- Exibe todas as transações realizadas até o momento, assim como o saldo atual.

### Sair:
- Encerra a aplicação.