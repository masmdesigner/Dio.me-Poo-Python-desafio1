# 💼 Sistema Bancário em Python — Desafio POO

Este projeto é um sistema bancário simples desenvolvido em Python, utilizando os princípios da **Programação Orientada a Objetos (POO)**. Ele simula operações básicas como depósito, saque e controle de contas, com estrutura modular e extensível.

---

## 🧠 Conceitos Utilizados

- **Encapsulamento**: Protege atributos internos das classes.
- **Herança**: Permite que classes compartilhem comportamentos.
- **Polimorfismo**: Permite que diferentes classes implementem métodos com o mesmo nome.
- **Abstração**: Utiliza classes abstratas para definir contratos de comportamento.

---

## 🏗️ Estrutura do Código

### 1. `Usuario`
Classe base que representa um cliente do banco.

- Atributos:
  - `endereco`: endereço do cliente.
  - `contas`: lista de contas associadas.
- Métodos:
  - `efetuar_operacao(conta, operacao)`: executa uma operação (saque ou depósito).
  - `vincular_conta(conta)`: adiciona uma conta ao cliente.

---

### 2. `PessoaFisica` (herda de `Usuario`)
Representa um cliente pessoa física.

- Atributos adicionais:
  - `nome`
  - `nascimento`
  - `cpf`

---

### 3. `ContaBancaria`
Classe base para contas bancárias.

- Atributos:
  - `_saldo`: saldo atual.
  - `_numero`: número da conta.
  - `_agencia`: código da agência.
  - `_usuario`: cliente associado.
  - `_extrato`: histórico de operações.
- Métodos:
  - `sacar(valor)`: realiza saque.
  - `depositar(valor)`: realiza depósito.
  - `criar_conta(usuario, numero)`: método de classe para instanciar nova conta.

---

### 4. `ContaCorrente` (herda de `ContaBancaria`)
Conta com limite de saque e número máximo de saques por dia.

- Atributos adicionais:
  - `limite`: valor máximo por saque.
  - `max_saques`: número máximo de saques permitidos.
- Sobrescreve:
  - `sacar(valor)`: com regras de limite e quantidade.

---

### 5. `Extrato`
Registra todas as operações realizadas em uma conta.

- Atributos:
  - `_movimentos`: lista de dicionários com tipo, valor e data.
- Métodos:
  - `registrar_movimento(operacao)`: adiciona uma operação ao extrato.

---

### 6. `Operacao` (classe abstrata)
Define a interface para operações bancárias.

- Propriedade abstrata:
  - `valor`
- Método abstrato:
  - `executar(conta)`

---

### 7. `Saque` (herda de `Operacao`)
Implementa a operação de saque.

- Atributos:
  - `_valor`
- Método:
  - `executar(conta)`: realiza o saque e registra no extrato.

---

### 8. `Deposito` (herda de `Operacao`)
Implementa a operação de depósito.

- Atributos:
  - `_valor`
- Método:
  - `executar(conta)`: realiza o depósito e registra no extrato.

---

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio