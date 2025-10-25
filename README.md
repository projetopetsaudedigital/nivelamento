# 🚀 SPRINT II - Introdução à Análise de Dados com Python

Olá, pessoal! Bem-vindos a este repositório. O objetivo é explicar um pouco sobre o universo da análise de dados, mostrando um fluxo de trabalho básico.


## 📖 Por que Análise de Dados?

Vivemos na era dos dados. Cada clique, cada compra online, cada rota no GPS gera um volume gigantesco de informações. Diante disso, é preciso saber extrair as informações, encontrar padrões e transformar esse ruído em conhecimento.


Esse conhecimento nos ajuda a tomar decisões mais inteligentes, otimizar produtos e fazer novas descobertas.


É nesse contexto que entram as bibliotecas que vamos usar: **NumPy** e **Pandas**.


Para escrever e executar os códigos em Python, podemos instalar no computador o Anaconda, uma distribuição do Python, e escolher a ferramenta JupyterLab. Porém, vocês também podem optar pelo Google Colab, um servidor que também permite escrever e executar código em Python diretamente no seu navegador. É só digitar Google Colab no Google que o servidor aparece.



## 🛠️ Ferramenta 1: NumPy (Python Numérico)


O NumPy é a biblioteca fundamental para computação numérica em Python.


Ele trabalha com matrizes e arranjos multidimensionais, permitindo cálculos rápidos e eficientes. Sua grande vantagem são as "operações vetorizadas", onde cálculos (como somas ou multiplicações) são aplicados a todos os elementos simultaneamente.


### Prática com NumPy


Primeiro, importamos a biblioteca:


Usamos 'np' como um apelido (para não precisar repetir 'numpy' novamente).

```python
import numpy as np
```
1. Criando um Array Simples

   
Vamos criar um array (um vetor) de 1 dimensão. 


Todos os valores devem ser do mesmo tipo, por exemplo, todos os números decimais ou todos os números inteiros.


```python
# Criando um array simples de números inteiros
arr = np.array([10, 20, 30, 40, 50], np.int16)
print("Array:", arr)
```


Ao executar o código, podemos ver o resultado. Note que aparecem os números escolhidos.


2. Operações Vetorizadas


Veja como é fácil aplicar operações a todos os números de uma vez:
```python
# Operações matemáticas vetorizadas
print("Multiplicado por 2:", arr * 2)
print("Soma total:", arr.sum())
print("Média:", arr.mean())
print("Desvio padrão:", arr.std())
```


Percebam que o NumPy multiplicou cada número do array por 2. Depois, o numpy somou todos os números que estão dentro do array, obtendo um valor de 150. Após isso, ele somou o valor total de 150 e dividiu pela quantidade de números (5), obtendo assim o valor da média. E, por fim, ele mediu o quão “dispersos” estão os dados em relação à média, fornecendo o valor do desvio padrão.


Agora iremos fazer um pouco diferente, ao invés de criarmos um array de uma dimensão, como fizemos antes, vamos criar um array bidimensional, também chamado de matriz. Uma estrutura composta de valores organizados em linhas e colunas, no nosso caso, vamos criar uma matriz de 2 linhas e 3 colunas.


3. Matrizes (Array Bidimensional)


Também podemos criar matrizes (linhas e colunas):

```python
# Criando uma matriz de 2 linhas e 3 colunas
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)

# '.T' calcula a transposta (inverte linhas e colunas)
print("Transposta:\n", matriz.T)
```


A forma como você agrupa os números nos colchetes vai definir exatamente como essa matriz será montada. Percebam que temos duas listas internas. A primeira, [1, 2, 3], se torna a primeira linha, e a segunda, [4, 5, 6], se torna a segunda linha.


Observem também que o número de elementos dentro de cada linha define o número de colunas. Como cada linha tem 3 números, a nossa matriz tem 3 colunas. 


Quando usamos o comando T, realizamos o processo de transposição. Basicamente, as linhas da matriz original se tornam as colunas da nova matriz. Como a nossa matriz original tinha 2 linhas e 3 colunas, a transposta passará a ter 3 linhas e 2 colunas.


## 🛠️ Ferramenta 2: Pandas


Enquanto o numpy lida com as operações numéricas, o pandas lida com a manipulação de dados estruturados, como banco de dados, planilhas e tabelas. 


Mas o que o pandas faz? 


Ele **lê**, **limpa**, **transforma**, **analisa** e **representa visualmente os dados em formato de tabelas**. As suas principais estruturas são o DataFrame e a Series:

* DataFrame é a tabela inteira
* Series é uma coluna da tabela


### Prática com NumPy e Pandas


Agora que vimos o básico de operações numéricas com NumPy, vamos usar o Pandas (que usa o NumPy por baixo dos panos) para importar, limpar e analisar um conjunto de dados.


Usaremos um conjunto de dados sobre diabetes (diabetes.csv).


Parte 1: Importando e Conhecendo os Dados


O primeiro passo é carregar os dados para o ambiente de análise e fazer uma primeira inspeção, para conhecer os dados. 


Mas antes disso, vamos importar o pandas e o numpy, usando o comando:

```python
import pandas as pd
import numpy as np
```


Agora, vamos ler o arquivo CSV e criar uma "tabela" que o Pandas chama de DataFrame.

```python
df = pd.read_csv('diabetes.csv')
```


## Conhecendo os dados

```python
# Ver as primeiras 5 linhas da tabela
print(df.head())

# Ver o tamanho (linhas, colunas)
print(df.shape) # Resultado: (768, 9)

# Ver um resumo dos tipos de dados e se há valores nulos
print(df.info())
```


Conhecendo as Colunas:


- Pregnancies: Número de gestações.
- Glucose: Nível de glicose no sangue.
- BloodPressure: Pressão arterial.
- SkinThickness: Medida da dobra cutânea.
- Insulin: Nível de insulina.
- BMI: Índice de Massa Corporal.
- DiabetesPedigreeFunction: Predisposição genética.
- Age: Idade.
- Outcome: Resultado (1 = tem diabetes, 0 = não tem).


Parte 2: Limpeza e Tratamento dos Dados


A etapa de limpeza é uma etapa fundamental, é o momento em que verificamos se no nosso conjunto de dados há erros de digitação, dados faltantes, tipo de dado errado. A limpeza garante que a nossa análise seja confiável.


Executando o df.info(), vimos que NÃO há dados "faltantes" (NaN). 


Porém, ao investigar os dados mais adiante, usando o df.describe(), percebemos que os dados ausentes foram, na verdade, preenchidos com o número zero (0).


Sendo assim, sabemos que é fisicamente impossível ter valor de glicose 0 ou de pressão arterial 0. Ou seja, isso significa que existem dados faltantes no conjunto de dados.


Para resolver esse problema e tratar os dados vamos fazer as seguintes operações:
```python
# 1. Criar uma cópia para não alterar o original
df_tratado = df.copy()

# 2. Definir colunas onde '0' é um dado faltante
colunas_problematicas = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# 3. Substituir '0' por 'NaN' (Not a Number), que é o marcador correto
df_tratado[colunas_problematicas] = df_tratado[colunas_problematicas].replace(0, np.nan)

# 4. Verificar quantos dados faltantes (NaN) temos agora
print(df_tratado.isna().sum())
```


Agora sim vemos os dados faltantes. Dos 768 pacientes, 227 estão com o dado de medida da dobra cutânea faltando, e 374 com o dado da insulina faltando.


Preenchendo os dados faltantes


Poderíamos substituir os dados ausentes por zero usando o comando:

```python
df=df.fillna (0)
```
Então, se tiver algum valor ausente, o fillna substitui por esse valor.
Ainda podemos também usar a média, no entanto, como a média é fortemente influenciada por valores extremos (outliers), na nossa análise optamos por usar a mediana. 


Lembre-se que a escolha da substituição dependerá muito do conjunto de dados que está em análise.
```python
# 5. Lista das colunas que queremos preencher
colunas_para_limpar = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

# 6. Loop: para cada coluna da lista...
for coluna in colunas_para_limpar:
    mediana = df_tratado[coluna].median() # Calcula a mediana
    df_tratado[coluna] = df_tratado[coluna].fillna(mediana) # Preenche os NaNs com a mediana

# 7. Verificar se limpamos tudo (deve dar tudo zero)
print(df_tratado.isnull().sum())
```


Verificando Dados Duplicados


Outro tipo de verificação é ver se há algum dado (linhas repetidas) duplicado.


```python
# Verifica se há alguma linha duplicada (retorna 0 se não houver)
print(df.duplicated().sum())
```


Havendo dados duplicados, o comando abaixo remove as linhas repetidas:


```python
# Comando para remover linhas duplicadas (apenas se houver)
# df.drop_duplicates(inplace=True)
```


Parte 3: Operações Numéricas e Estatísticas


Para ter um resumo estatístico das colunas numéricas, usamos:

```python
# Usamos o .describe() no DataFrame TRATADO
print(df_tratado.describe())
```


Dessa forma, obtemos o valor da média, desvio padrão, valor mínimo, valor máximo e os quartis de colunas, e assim temos um panorama da saúde do grupo. Esse comando também identifica outliers, simetria dos dados.


O resumo estatístico geral é muito útil, mas para fazer cálculos mais específicos usamos o Numpy. 


Se quisermos, por exemplo, fazer um agrupamento? Comparando grupos diferentes...


Ex: Como as características dos pacientes com diabetes se comparam às dos pacientes sem diabetes?


Podemos agrupar os dados pela coluna Outcome (o resultado) e calcular a média de cada grupo.

```python
# Agrupa por 'Outcome' e calcula a média de todas as outras colunas
print(df_tratado.groupby('Outcome').mean())
```


Ao excutar, vemos que o nível médio de 'Glucose' é visivelmente maior no grupo 1 (142.13) isto é, nos pacientes com diabetes, do que no grupo 0 (110.68) pacientes sem diabetes.


Esse tipo de agrupamento é fundamental para identificar padrões.


Além do resumo estatístico geral, também podemos entender como as variáveis se relacionam entre si e responder perguntas como:


Quais fatores têm maior relação com o diabetes? Será que o nível de glicose aumenta conforme o IMC aumenta? 


Uma maneira de medir a força da relação é calcular o coeficiente de correlação, onde:
* Valor próximo de 1: correlação positiva forte
* Valor próximo de -1: correlação negativa forte.
* Valor próximo de 0: Sem correlação clara (fraca)


```python
# Calcula a matriz de correlação
print(df_tratado.corr())
```


Analisando a linha Resultado (Outcome), notamos que a Glicose (Glucose) possui a correlação positiva mais forte. Isso faz total sentido clinicamente, já que níveis elevados de glicose são o principal indicador usado para diagnosticar o diabetes.


Observe:


* Pregnancies: 0.221
* **Glucose: 0.492**
* BloodPressure: 0.165
* SkinThickness: 0.214
* Insulin: 0.203
* BMI: 0.312
* DiabetesPedigreeFunction: 0.173
* Age: 0.238


Nesta Sprint, nós conseguimos:


1. Importar e preparar o conjunto de dados `diabetes.csv`.
2. Realizar a limpeza e tratamento de dados faltantes.
3. Extrair informações estatísticas e descobrir que a Glicose tem a correlação mais forte com o diagnóstico neste conjunto de dados.
   

Dominar essas técnicas nos auxilia na tomada de decisão, no entendimento sobre o perfil de nossos pacientes e otimização de tratamentos. 

