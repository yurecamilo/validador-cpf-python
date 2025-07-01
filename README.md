# 🧾 Validador de CPF em Python 🐍

Este programa em Python realiza a **validação de CPFs** informados pelo usuário, verificando se são **válidos ou inválidos** de acordo com as regras oficiais do cálculo dos dígitos verificadores. ✅❌

## 🚀 Como funciona

- 📝 O usuário digita um CPF com 11 dígitos (apenas números).  
- ⚠️ O programa checa se o formato está correto (tamanho e somente números).  
- 🔢 Calcula os dois dígitos verificadores usando o algoritmo oficial:  
  - Multiplica os 9 primeiros dígitos por pesos decrescentes (10 a 2) para calcular o 1º dígito.  
  - Multiplica os 9 dígitos + 1º dígito verificador por pesos decrescentes (11 a 2) para o 2º dígito.  
- ✔️ Compara os dígitos calculados com os informados.  
- 🛠️ Informa se o CPF é válido ou inválido.  
- 🔄 Permite validar vários CPFs em sequência.  
- 📊 Ao final, exibe um resumo com quantidades e porcentagens.

## 🎯 Como usar

1. 📂 Clone este repositório.  
2. ▶️ Execute o script Python.  
3. 🔤 Digite os CPFs que deseja validar.  
4. ❓ Após cada CPF, escolha continuar ou sair.  
5. 📈 Confira o resumo das validações feitas.

## Entrada:

- digite um cpf: 12345678909 .
- Deseja continuar? [S/N] S .
- digite um cpf: 11144477735 .
- Deseja continuar? [S/N] N .

## Saída:

- Quantidade de CPFS VÁLIDOS: 1 ✅ .
- Quantidade de CPFS INVÁLIDOS: 1 ❌ . 
- Quantidade total de CPFS testados: 2 .
- Porcentagem de CPFS VÁLIDOS: 50.00% .
- Porcentagem de CPFS INVÁLIDOS: 50.00% .
## ⚙️ Requisitos

- Python 3.x 🐍

## ℹ️ Observações

Este programa valida o CPF conforme o algoritmo oficial, **mas não verifica registros oficiais ou situação cadastral.**

---
