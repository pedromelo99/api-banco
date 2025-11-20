# API Banking - Sistema Bancário

API RESTful de sistema bancário desenvolvida com FastAPI, SQLAlchemy e conceitos de Programação Orientada a Objetos (POO).

## 🚀 Funcionalidades

- ✅ Criar conta corrente ou poupança
- ✅ Realizar depósitos
- ✅ Realizar saques (com validação de saldo)
- ✅ Consultar saldo
- ✅ Listar transações
- ✅ Obter estatísticas da conta
- ✅ Deletar conta

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
