# API Banking - Sistema Bancário com POO

API de controle de contas bancárias desenvolvida com FastAPI, implementando conceitos avançados de Programação Orientada a Objetos.

## 🎯 Funcionalidades

- ✅ Criar contas (Corrente e Poupança)
- ✅ Consultar saldo e informações da conta
- ✅ Realizar depósitos
- ✅ Realizar saques (com validação de saldo)
- ✅ Listar histórico de transações
- ✅ Calcular estatísticas financeiras
- ✅ Sistema de rendimento para poupança
- ✅ Limite especial para conta corrente

## 🧱 Conceitos POO Implementados

### ✨ Abstração
- **Classe `Conta`**: Classe abstrata base com métodos `@abstractmethod`
- **Classe `Transacao`**: Classe abstrata para transações (Deposito, Saque, Rendimento)

### 🔗 Herança
```
Conta (abstrata)
├── ContaCorrente (com limite especial)
└── ContaPoupanca (com rendimento)

Transacao (abstrata)
├── Deposito
├── Saque
└── Rendimento
```

### 🎭 Polimorfismo
- `calcular_rendimento()`: comportamento diferente em cada tipo de conta
- `executar()`: cada tipo de transação executa de forma diferente
- `sacar()`: validação específica por tipo de conta

### 🔒 Encapsulamento
- Atributos privados (`_saldo`, `_titular`)
- Acesso via `@property` (getters/setters)
- Validações internas protegidas

## 📊 Estruturas de Dados e Controle

### Estruturas de Decisão (if/elif/else)
- ✅ Validação de saldo antes de saque
- ✅ Verificação de tipo de conta
- ✅ Validação de valores positivos
- ✅ Cálculo condicional de totais

### Estruturas de Repetição (for)
- ✅ Iteração sobre lista de transações
- ✅ Cálculo de totais com loop
- ✅ Listagem de histórico
- ✅ Consultas no banco de dados

### Estruturas de Dados
- ✅ **Listas**: armazenamento de transações
- ✅ **Dicionários**: retorno de dados estruturados
- ✅ **Objetos**: models SQLAlchemy

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório (ou extraia os arquivos)

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

Execute o seguinte comando na raiz do projeto:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação Interativa

Acesse a documentação interativa (Swagger UI):
- `http://localhost:8000/docs`

## 🔗 Endpoints

### Contas

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/contas` | Criar nova conta |
| GET | `/contas` | Listar todas as contas |
| GET | `/contas/{id}` | Buscar conta por ID |
| DELETE | `/contas/{id}` | Deletar conta |
| POST | `/contas/{id}/deposito` | Realizar depósito |
| POST | `/contas/{id}/saque` | Realizar saque |

### Transações

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/contas/{id}/transacoes` | Listar transações |
| GET | `/contas/{id}/estatisticas` | Obter estatísticas |

## 💡 Exemplos de Uso

### Criar uma conta corrente
```json
POST /contas
{
  "titular": "João Silva",
  "tipo": "corrente",
  "limite_especial": 1000.0
}
```

### Criar uma conta poupança
```json
POST /contas
{
  "titular": "Maria Santos",
  "tipo": "poupanca"
}
```

### Realizar depósito
```json
POST /contas/1/deposito
{
  "valor": 500.0
}
```

### Realizar saque
```json
POST /contas/1/saque
{
  "valor": 100.0
}
```

## 🏗️ Arquitetura

O projeto segue uma arquitetura em 3 camadas:

```
┌─────────────────────┐
│   Camada API        │  ← FastAPI (main.py)
│   (main.py)         │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   Camada Negócio    │  ← Controllers
│   (controllers/)    │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   Camada Dados      │  ← Models + POO
│   (models.py)       │
└─────────────────────┘
```

## 📂 Estrutura de Arquivos

```
api-banco/
├── app/
│   ├── main.py                    # API FastAPI
│   ├── database.py                # Configuração do banco
│   ├── models.py                  # Modelos SQLAlchemy
│   ├── schemas.py                 # Schemas Pydantic
│   ├── controllers/
│   │   ├── contas_controller.py
│   │   └── transacoes_controller.py
│   └── poo/
│       ├── conta.py               # Classe abstrata
│       ├── conta_corrente.py
│       └── conta_poupanca.py
├── requirements.txt
└── README.md
```

## 🧱 Conceitos POO Aplicados

- **Abstração**: Classe `Conta` abstrata
- **Herança**: `ContaCorrente` e `ContaPoupanca` herdam de `Conta`
- **Polimorfismo**: Métodos implementados de forma diferente em cada tipo
- **Encapsulamento**: Atributos protegidos

## 🛠️ Tecnologias

- **FastAPI**: Framework web
- **SQLAlchemy**: ORM
- **Pydantic**: Validação de dados
- **SQLite**: Banco de dados
- **Uvicorn**: Servidor ASGI

## 📝 Licença

Projeto acadêmico - Livre para uso educacional
