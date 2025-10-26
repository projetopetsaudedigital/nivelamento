# Sistema de Clientes com Padrões de Projeto

Este é um **mini sistema em Python** que demonstra a aplicação de vários **padrões de projeto**:  

- **Factory** → criação de diferentes tipos de clientes (Normal, VIP).  
- **Strategy** → aplicação de diferentes estratégias de desconto.  
- **Repository** → gerenciamento e armazenamento de clientes em memória.  
- **Adapter** → adaptação de uma biblioteca externa de envio de notificações para a interface do sistema.  

---

## Funcionalidades

1. Criar clientes de tipos diferentes usando a **Factory**.  
2. Armazenar clientes no **Repository**.  
3. Aplicar **estratégias de desconto** diferentes para cada tipo de cliente.  
4. Enviar notificações para clientes usando o **Adapter**.  

---

## Pré-requisitos

Para executar o sistema, é necessário ter o **Python 3.10 ou superior** instalado em sua máquina.

Você pode baixar e instalar o Python no site oficial:  
[https://www.python.org/downloads/](https://www.python.org/downloads/)

Após a instalação, certifique-se de que o comando `python` funciona no terminal:

```bash
python --version
```

---

## Como executar

1. Executar o fluxo principal
```bash
cd src
python main.py
```

2. Executar testes automáticos
```bash
cd src
python test.py
```