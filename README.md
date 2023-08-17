# DIO: Sistema Bancário Python Otimizado

App simples de um sistema bancário para um ou mais usuários.

### NOTA: O app não armazena dados entre as sessões.

## Como executar?

**Passo 1:** Clone este repositório;

**Passo 2:** Execute o comando:
```bash
python -i desafio.py
```

## Como usar?

Há seis opções. Digite qualquer uma destas letras para executar a devida ação:
  - [u] (Criar usuário);
  - [a] (Criar conta corrente);
  - [d] ("Depositar");
  - [s] ("Sacar");
  - [e] ("Extrato"); e
  - [q] ("Sair").

### Criar usuário
- Digite os números do CPF que você quer cadastrar.
  - _Só pode existir um usuário por CPF!_
  - Não utilize os pontos e traços!
- Depois digite o nome do usuário, a data de nascimento, e o endereço.
  - Data no formato dd/mm/aaaa.
  - Endereço no formato:
    - Logradouro, Nº - Bairro - Cidade/Sigla do estado

### Criar conta
- Digite os números do CPF que você quer cadastrar.
  - Não utilize os pontos e traços!
- Caso o CPF exista no sistema, uma conta será criada automaticamente, com as seguintes informações:
  - Agência;
    - O número é fixo, 0001.
  - Número da conta; e
    - Sequencial, começando em 1.
  - Usuário.
    - Usuário do mesmo CPF passado no início da função.

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