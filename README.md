# 📚 Repositório NIVELAMENTO - Projetos de Desenvolvimento

Este repositório contém uma coleção abrangente de projetos educacionais organizados por níveis de complexidade, cobrindo desde conceitos fundamentais de Python até técnicas avançadas de análise de dados e machine learning.

## 🗂️ Estrutura do Repositório

### 📁 **1-advanced-python-language**
**Sistema de Clientes com Padrões de Projeto**

Um sistema completo em Python que demonstra a aplicação de vários padrões de projeto fundamentais:

- **Factory Pattern** → Criação de diferentes tipos de clientes (Normal, VIP)
- **Strategy Pattern** → Aplicação de diferentes estratégias de desconto
- **Repository Pattern** → Gerenciamento e armazenamento de clientes em memória
- **Adapter Pattern** → Adaptação de biblioteca externa de notificações

**Tecnologias:** Python 3.10+, Orientação a Objetos, Design Patterns

**Funcionalidades:**
- Criação de clientes usando Factory
- Armazenamento no Repository
- Aplicação de estratégias de desconto
- Sistema de notificações via Adapter

---

### 📁 **1-profissional-github**
**Guia de Versionamento e Fluxo de Trabalho (GitFlow)**

Documentação completa sobre controle de versionamento seguindo o padrão GitFlow:

- Convenções de nomenclatura de branches
- Fluxo de trabalho para desenvolvimento
- Resolução de conflitos
- Boas práticas de desenvolvimento

**Conteúdo:**
- Estratégias de branching (main, dev, feature, bugfix, hotfix)
- Processo de Pull Requests
- Resolução de conflitos
- Convenções de commit

---

### 📁 **1-python-and-postgresql-integration**
**Integração Python + PostgreSQL**

Projeto completo de integração entre Python e PostgreSQL com foco em sistemas de saúde:

**Tecnologias:** Python, PostgreSQL, psycopg2, SQL

**Funcionalidades:**
- Configuração segura do PostgreSQL
- Criação de banco de dados e usuários
- Modelagem de entidades e relacionamentos
- Operações CRUD completas
- Queries complexas com JOINs
- Sistema de permissões e segurança

**Estrutura do Banco:**
- Tabelas de dimensão (tipos de unidade, sexo)
- Tabelas principais (unidades de saúde, pacientes, atendimentos)
- Relacionamentos 1:N e N:N
- Sistema de chaves estrangeiras

**Scripts Incluídos:**
- `postgresql_bd.py` - Script principal de demonstração
- Configuração via variáveis de ambiente
- Exemplos de diferentes tipos de dados SQL
- Operações de INSERT, UPDATE, DELETE, SELECT

---

### 📁 **2-data-analysing**
**Introdução à Análise de Dados com Python**

Projeto focado em análise exploratória de dados usando NumPy e Pandas:

**Tecnologias:** Python, NumPy, Pandas, Matplotlib, Seaborn

**Conteúdo:**
- Fundamentos do NumPy (arrays, operações vetorizadas, matrizes)
- Manipulação de dados com Pandas
- Análise do dataset Diabetes
- Limpeza e tratamento de dados
- Estatísticas descritivas
- Análise de correlações

**Tópicos Abordados:**
- Importação e exploração de dados
- Tratamento de valores faltantes
- Normalização e padronização
- Análise estatística
- Visualização de dados

---

### 📁 **2-data-mining**
**Machine Learning com Scikit-learn**

Projeto abrangente de machine learning dividido em três áreas principais:

#### **Pré-Processamento**
- Preparação de datasets para ML
- Tratamento de dados faltantes
- Normalização e padronização
- Divisão treino/teste
- Codificação de variáveis categóricas

#### **Classificação**
- Algoritmos de classificação (KNN, Logistic Regression, SVM, Decision Tree, Random Forest, etc.)
- Avaliação de performance (acurácia, matriz de confusão, F1-score)
- Dataset Iris como exemplo prático
- Comparação de algoritmos

#### **Regressão**
- Algoritmos de regressão (Linear, Ridge, Lasso, Random Forest, Gradient Boosting, etc.)
- Métricas de avaliação (MAE, RMSE, R²)
- Dataset Diabetes como exemplo
- Análise de performance

**Tecnologias:** Python, Scikit-learn, NumPy, Pandas, Matplotlib

---

### 📁 **2-data-visualization**
**Visualização de Dados**

Projeto dedicado à criação de visualizações eficazes para análise de dados:

**Tecnologias:** Python, Matplotlib, Seaborn, Plotly

**Conteúdo:**
- Gráficos básicos (linha, barra, dispersão)
- Visualizações estatísticas (histogramas, box plots)
- Gráficos avançados (heatmaps, pair plots)
- Dashboards interativos
- Boas práticas de visualização

## 🚀 Como Usar Este Repositório

### Pré-requisitos
- Python 3.8+
- PostgreSQL (para projetos de banco de dados)
- Git (para controle de versão)

### Instalação
```bash
# Clone o repositório
git clone <url-do-repositorio>

# Navegue para o diretório desejado
cd nivelamento/[pasta-do-projeto]

# Instale as dependências (quando aplicável)
pip install -r requirements.txt
```

### Estrutura de Aprendizado Recomendada

1. **Iniciantes:** Comece com `1-advanced-python-language`
2. **Controle de Versão:** Estude `1-profissional-github`
3. **Banco de Dados:** Explore `1-python-and-postgresql-integration`
4. **Análise de Dados:** Pratique `2-data-analysing`
5. **Machine Learning:** Avance para `2-data-mining`
6. **Visualização:** Complete com `2-data-visualization`

## 📋 Projetos por Nível

### 🟡 **Nível 1 - Intermediário**
- **Python Avançado:** Padrões de projeto, OOP
- **Git/GitHub:** Controle de versão profissional
- **PostgreSQL:** Banco de dados relacional

### 🔴 **Nível 2 - Avançado**
- **Análise de Dados:** NumPy, Pandas, estatísticas
- **Machine Learning:** Scikit-learn, algoritmos
- **Visualização:** Gráficos e dashboards


## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **PostgreSQL**
- **NumPy & Pandas**
- **Scikit-learn**
- **Matplotlib & Seaborn**
- **Git & GitHub**

## 📚 Recursos Adicionais

### Documentação
- Cada pasta contém READMEs detalhados
- Exemplos de código comentados
- Guias de instalação e configuração

### Datasets
- Iris (classificação)
- Diabetes (regressão)
- Dados de saúde simulados

### Ferramentas Recomendadas
- **IDEs:** VS Code, PyCharm, Jupyter Notebook
- **Banco de Dados:** pgAdmin, DBeaver
- **Visualização:** Jupyter Lab, Google Colab

## 🤝 Contribuição

Este repositório é educacional e está aberto para:
- Sugestões de melhorias
- Correções de bugs
- Adição de novos exemplos
- Melhoria da documentação

## 📄 Licença

Este projeto é destinado a fins educacionais e de aprendizado.

---

**🎯 Objetivo:** Fornecer uma base sólida em desenvolvimento Python, desde conceitos fundamentais até técnicas avançadas de análise de dados e machine learning, com foco prático e aplicações reais.
