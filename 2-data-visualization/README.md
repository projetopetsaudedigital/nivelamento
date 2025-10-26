


# 🐍📊 How-To-Do: Visualização de Dados com Python, Matplotlib, Streamlit e Plotly

-----

## 📖 Sobre o Projeto

Este repositório é um guia prático para desenvolvedores que desejam iniciar na visualização de dados. O objetivo é demonstrar como criar gráficos simples e informativos usando as bibliotecas **Matplotlib**, **Streamlit** e **Plotly**   em Python, a partir de um conjunto de dados real, para identificar padrões e tendências.

-----

## 🎨 O que é Matplotlib?

O **Matplotlib** é a biblioteca fundamental para a criação de gráficos e visualizações em Python. É considerado o "canivete suíço" da plotagem, permitindo um controle detalhado sobre cada aspecto de uma figura.

👉 Imagine ter uma caixa de ferramentas completa para desenhar, com lápis de todas as cores, réguas, compassos e papéis milimetrados. Isso é o Matplotlib para um cientista de dados.

### 🌟 Principais características:

  - 🎯 **Poderoso:** Capaz de criar desde os gráficos mais simples (barras, linhas, pizza) até visualizações complexas.
  - ⚙️ **Customizável:** Permite controlar cada detalhe de um gráfico: cores, fontes, títulos, legendas, eixos, etc.
  - 🤝 **Integrado:** Funciona perfeitamente com as estruturas de dados nativas do Python, como listas e dicionários.
  - 📚 **Comunidade:** Por ser uma das bibliotecas mais antigas e populares, possui uma vasta documentação e incontáveis exemplos online.

-----

## 🔬 Nosso Estudo de Caso: Análise de Dados de Diabetes

Para este guia, vamos utilizar uma pequena amostra de dados do dataset **Pima Indians Diabetes Database**. Para focar exclusivamente no Matplotlib, vamos definir esses dados diretamente em nosso código Python usando listas, baseados nos exemplos realistas que vimos anteriormente.

-----

## 🚀 Passo a Passo: Da Análise à Visualização

### 1\. Preparando o Ambiente

Primeiro, vamos instalar a única biblioteca que precisaremos. Com seu ambiente virtual (`venv`) ativado, execute no terminal:

```bash
pip install matplotlib
```

### 2\. Criando Gráficos Simples com Matplotlib

Agora, vamos direto para a criação das visualizações. Cada exemplo abaixo é um script completo e autônomo.

Excelente observação\! Você está certíssimo, eu realmente simplifiquei os comentários na última versão e não deveria ter feito isso. Peço desculpas.

A minha intenção foi seguir sua orientação de simplificar o código ao máximo, tirando o Pandas, e no processo acabei enxugando os comentários também. Mas você tem toda a razão: para um material didático, especialmente para quem não conhece a biblioteca, ter cada linha comentada é muito mais importante.

Vamos corrigir isso agora. Aqui estão os mesmos três blocos de código para o `README.md`, agora com **comentários detalhados em cada linha de plotagem**, explicando o que cada método e parâmetro faz.

Pode substituir os blocos de código anteriores por estes.

-----

### **A. Gráfico de Linhas - Analisando Tendências**

**Pergunta:** Em nossa amostra, existe uma tendência na predisposição genética ao diabetes conforme a idade das pacientes aumenta?

```python
# Importa a biblioteca principal de plotagem e a apelida de 'plt'
import matplotlib.pyplot as plt

# --- Dados ---
# Definimos os dados diretamente em listas Python para focar no Matplotlib.
idades = [21, 26, 30, 31, 32, 33, 50, 51, 53, 59]
pedigree = [0.167, 0.248, 0.201, 0.351, 0.672, 2.288, 0.627, 0.587, 0.158, 0.398]

# --- Visualização ---
# plt.figure() cria a "tela" (figura) onde vamos desenhar o gráfico.
# figsize=(10, 6) define o tamanho da figura em polegadas (10 de largura, 6 de altura).
plt.figure(figsize=(10, 6))

# plt.plot() é o comando que desenha o gráfico de linhas.
# O primeiro argumento (idades) é o eixo X, o segundo (pedigree) é o eixo Y.
# marker='o'       -> Adiciona um marcador de círculo em cada ponto de dado.
# linestyle='--'   -> Define o estilo da linha como tracejada.
# color='purple'   -> Define a cor da linha e dos marcadores.
# label='...'      -> Define o texto que aparecerá na legenda do gráfico.
plt.plot(idades, pedigree, marker='o', linestyle='--', color='purple', label='Predisposição Genética')

# plt.title() define o título principal do gráfico.
plt.title('Tendência da Predisposição Genética por Idade (Amostra)', fontsize=16)

# plt.xlabel() e plt.ylabel() definem os rótulos dos eixos X e Y, respectivamente.
plt.xlabel('Idade (anos)', fontsize=12)
plt.ylabel('Diabetes Pedigree Function', fontsize=12)

# plt.grid(True) adiciona uma grade ao fundo para facilitar a leitura dos valores.
plt.grid(True, alpha=0.5)

# plt.legend() ativa a exibição da legenda, usando os 'labels' definidos nos plots.
plt.legend()

# plt.savefig() salva a figura gerada como um arquivo de imagem.
plt.savefig('grafico_de_linhas_idade_pedigree.png')

# plt.show() abre uma janela para exibir o gráfico na tela.
plt.show()
```

### **B. Gráfico de Pizza - Visualizando Proporções**

**Pergunta:** Qual a proporção de pacientes com e sem diabetes em nossa amostra?

```python
# Importa a biblioteca de plotagem
import matplotlib.pyplot as plt

# --- Dados ---
# labels -> Rótulos de texto para cada "fatia" da pizza.
labels = ['Sem Diabetes', 'Com Diabetes']
# sizes -> Os valores numéricos de cada fatia. Matplotlib calcula a porcentagem automaticamente.
sizes = [12, 8]
# colors -> Uma lista de cores para cada fatia.
colors = ['#66b3ff', '#ff9999']
# explode -> Afasta uma fatia do centro para dar destaque. O valor indica a fração do raio.
explode = (0.05, 0)

# --- Visualização ---
# Cria a "tela" para o nosso gráfico.
plt.figure(figsize=(8, 8))

# plt.pie() é o comando que desenha o gráfico de pizza.
# sizes     -> Passa os valores de cada fatia.
# explode   -> Aplica o destaque que definimos.
# labels    -> Define os nomes de cada fatia.
# colors    -> Define as cores de cada fatia.
# autopct   -> Formata como o texto da porcentagem deve aparecer. '%1.1f%%' significa um número float com 1 casa decimal.
# shadow    -> Adiciona uma sombra para um leve efeito de profundidade.
# startangle-> Define o ângulo inicial da primeira fatia (gira o gráfico).
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Adiciona o título principal ao gráfico.
plt.title('Proporção de Diagnósticos de Diabetes (Amostra)', fontsize=16)

# plt.axis('equal') garante que a pizza seja um círculo perfeito.
plt.axis('equal')

# Salva e exibe o gráfico.
plt.savefig('grafico_de_pizza_diagnostico.png')
plt.show()
```

### **C. Gráfico de Barras - Comparando Categorias**

**Pergunta:** Qual a média de glicose para pacientes com e sem diabetes em nossa amostra?

```python
# Importa a biblioteca de plotagem
import matplotlib.pyplot as plt

# --- Dados ---
# categorias -> Rótulos de texto para cada barra no eixo X.
categorias = ['Sem Diabetes', 'Com Diabetes']
# media_glicose -> Lista com a altura de cada barra, correspondendo a cada categoria.
media_glicose = [99.7, 155.0]

# --- Visualização ---
# Cria a "tela" para o gráfico.
plt.figure(figsize=(8, 6))

# plt.bar() é o comando que desenha o gráfico de barras.
# categorias    -> Os rótulos do eixo X.
# media_glicose -> As alturas das barras no eixo Y.
# color         -> Uma lista de cores, uma para cada barra.
# edgecolor     -> Cor da borda das barras para um melhor acabamento visual.
# label         -> Texto para a legenda do gráfico.
plt.bar(categorias, media_glicose, color=['skyblue', 'salmon'], edgecolor='black', label='Média de Glicose')

# Adiciona o título principal ao gráfico.
plt.title('Média de Glicose por Diagnóstico (Amostra)', fontsize=16)

# Adiciona os rótulos dos eixos.
plt.xlabel('Diagnóstico', fontsize=12)
plt.ylabel('Nível Médio de Glicose', fontsize=12)

# Adiciona uma grade horizontal tracejada para facilitar a comparação visual dos valores.
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ativa a exibição da legenda.
plt.legend()

# Salva e exibe o gráfico.
plt.savefig('barras_media_glicose.png')
plt.show()
```
-----

### ✨ Personalizando seus Gráficos (Estilos e Cores)

Uma das maiores vantagens do Matplotlib é a sua capacidade de personalização.

#### Estilos Prontos (`plt.style.use()`)

A biblioteca já vem com vários **estilos visuais prontos** que mudam completamente a aparência de todos os seus gráficos com uma única linha de código. É como aplicar um "tema". Basta adicionar `plt.style.use('nome_do_estilo')` no início do seu script.

**Exemplo:**

```python
import matplotlib.pyplot as plt

# Esta linha muda o visual de TODOS os gráficos feitos depois dela.
plt.style.use('ggplot')

# (Resto do seu código de gráfico de barras aqui...)
```

> **💡 Outros estilos populares para testar:** `'seaborn-v0_8-pastel'`, `'fivethirtyeight'`, `'dark_background'`.

-----

### 🛠️ Principais Métodos do Matplotlib: Um Guia Rápido

Para fixar o conhecimento e mostrar o poder da biblioteca, aqui está uma lista de alguns dos métodos mais utilizados e o que eles fazem.

#### **Configuração da Figura e Eixos**

  - `plt.figure(figsize=(w, h))`: Cria a "tela" em branco para o seu gráfico, com uma largura (`w`) e altura (`h`) definidas.
  - `plt.subplots(rows, cols)`: Cria uma figura com múltiplos sub-gráficos organizados em `rows` linhas e `cols` colunas. É extremamente poderoso para criar dashboards.
  - `plt.title('Texto')`: Adiciona um título principal ao gráfico.
  - `plt.xlabel('Texto')`: Adiciona um rótulo ao eixo X (horizontal).
  - `plt.ylabel('Texto')`: Adiciona um rótulo ao eixo Y (vertical).
  - `plt.xticks()` e `plt.yticks()`: Permitem customizar as marcações e os rótulos nos eixos X e Y.

#### **Comandos de Plotagem (Tipos de Gráfico)**

  - `plt.plot(x, y)`: O comando principal para **gráficos de linhas**.
  - `plt.scatter(x, y)`: Cria **gráficos de dispersão**, mostrando a relação entre duas variáveis.
  - `plt.bar(categorias, valores)`: Cria **gráficos de barras** verticais.
  - `plt.barh(categorias, valores)`: Cria **gráficos de barras** horizontais.
  - `plt.hist(dados)`: Cria um **histograma** para visualizar a distribuição de uma única variável.
  - `plt.pie(valores)`: Cria um **gráfico de pizza** para mostrar proporções.
  - `plt.boxplot(dados)`: Cria um **boxplot**, ótimo para visualizar a distribuição de dados e identificar outliers.

#### **Customização e Finalização**

  - `plt.grid(True)`: Adiciona uma grade de fundo ao gráfico.
  - `plt.legend()`: Exibe a legenda do gráfico (requer que você tenha definido `label` nos seus comandos de plotagem).
  - `plt.text(x, y, 'Texto')`: Adiciona um texto qualquer em uma coordenada `(x, y)` específica do gráfico.
  - `plt.savefig('nome_arquivo.png')`: Salva o gráfico gerado como um arquivo de imagem.
  - `plt.show()`: Exibe a janela com o gráfico finalizado. É um comando essencial no final de cada script.
  - `plt.close()`: Fecha a janela do gráfico, útil para liberar memória em scripts que geram muitas figuras.

-----

# 🚀 Guia Completo: Instalação do Streamlit no PyCharm

Este guia mostra o passo a passo para configurar e rodar sua primeira aplicação web de dados com Streamlit, utilizando o ambiente de desenvolvimento PyCharm.

-----

## ⚙️ Configuração Inicial

### 1\. Pré-Requisito: Instalar o PyCharm

Se você ainda não tem, baixe e instale a versão **Community** (gratuita) do PyCharm diretamente do site da JetBrains.
👉 [Download PyCharm](https://www.jetbrains.com/pycharm/download/)

### 2\. Criar um Projeto Python com Ambiente Virtual

O ideal é criar um ambiente isolado (`venv`) para cada projeto, evitando conflitos de bibliotecas. O PyCharm facilita muito isso.

1.  Abra o PyCharm e clique em **"New Project"**.
2.  Defina o local e o nome do seu projeto (ex: `C:/Projetos/StreamlitSaude`).
3.  Na seção **"Python Interpreter"**:
      - Verifique se a opção **"New environment using"** está selecionada.
      - O tipo deve ser **Virtualenv**.
4.  Clique em **"Create"**.

### 3\. Instalar o Streamlit

Com o projeto criado e aberto no PyCharm:

1.  Abra o **Terminal** do PyCharm (geralmente fica na barra inferior da tela).
2.  Certifique-se de que o ambiente virtual está ativo (você deve ver o nome `(.venv)` no início da linha do terminal).
3.  Execute o comando `pip` para instalar o Streamlit e a biblioteca Pandas (que é essencial para manipular dados):
    ```bash
    pip install streamlit pandas
    ```

### 4\. Criar e Rodar seu Primeiro App

Agora que o ambiente está pronto, vamos criar e rodar a aplicação.

1.  Na árvore de arquivos do seu projeto (à esquerda), clique com o botão direito e selecione **"New" \> "Python File"**.
2.  Dê um nome para o arquivo, por exemplo: `dashboard_saude.py`.
3.  Insira o código Streamlit no arquivo (veja os exemplos abaixo).
4.  Para rodar, volte ao **Terminal** do PyCharm e execute o comando:
    ```bash
    streamlit run dashboard_saude.py
    ```

> **💡 O que acontece agora?** O Streamlit iniciará um pequeno servidor web e abrirá automaticamente uma aba no seu navegador no endereço `http://localhost:8501`, exibindo sua aplicação. A cada vez que você salvar o arquivo `.py`, a página no navegador se atualizará automaticamente\!

-----

## 📈 Exemplos de Código para um Dashboard de Saúde

O Streamlit usa a biblioteca Pandas por trás dos panos para manipular os dados. Abaixo estão exemplos de como exibir dados médicos de forma clara.

### Exemplo 1: Tabela Estática com `st.table`

A função `st.table` é ideal para exibir pequenos conjuntos de dados de forma simples e direta, sem interatividade.

```python
# dashboard_saude.py

import streamlit as st
import pandas as pd

st.title("👨‍⚕️ Resumo de Casos Ativos (st.table)")

# Criação de um DataFrame (tabela) de exemplo com dados de saúde
data = {
    'ID Paciente': [101, 102, 103, 104],
    'Idade': [45, 62, 33, 78],
    'Comorbidade': ['Diabetes', 'Hipertensão', 'Nenhuma', 'Cardíaca'],
    'Status': ['Estável', 'Monitoramento', 'Estável', 'Crítico']
}
df_resumo = pd.DataFrame(data)

st.header("Casos de Alto Risco em Monitoramento")
# Usamos o Pandas para filtrar os dados antes de exibi-los com o Streamlit
st.table(df_resumo[df_resumo['Status'] != 'Estável'])
```

### Exemplo 2: Tabela Interativa com `st.dataframe`

A função `st.dataframe` é muito mais poderosa. Ela cria uma tabela interativa que permite ao usuário rolar, ordenar por colunas e até expandir a visualização. É a escolha ideal para datasets maiores.

```python
# Continuação do arquivo: dashboard_saude.py

st.header("💉 Tabela Completa de Resultados de Exames (st.dataframe)")

# Criando um DataFrame maior de exemplo
dados_exames = {
    'Nome': ['A. Silva', 'B. Souza', 'C. Costa', 'D. Santos', 'E. Oliveira'],
    'Glicose (mg/dL)': [95, 150, 88, 110, 140],
    'Colesterol (mg/dL)': [180, 220, 195, 175, 250],
    'Hemoglobina (g/dL)': [14.2, 12.5, 15.1, 13.8, 11.9],
    'Risco Diabetes': ['Baixo', 'Alto', 'Baixo', 'Médio', 'Alto']
}
df_exames = pd.DataFrame(dados_exames)

# O comando para exibir a tabela interativa é simplesmente este:
st.dataframe(df_exames)
```

### Bônus: Adicionando Gráficos Simples

O Streamlit possui comandos nativos para criar gráficos de forma muito fácil a partir dos seus dados.

```python
# Continuação do arquivo: dashboard_saude.py

# Adicionando uma visualização simples de dados
st.subheader("Visualização Rápida da Glicose")

# st.line_chart pega o DataFrame e plota um gráfico de linhas automaticamente
# Aqui, definimos 'Nome' como o índice (eixo X) para o gráfico
st.line_chart(df_exames.set_index('Nome')['Glicose (mg/dL)'])
```