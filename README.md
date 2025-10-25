# 🚀 Projeto de Introdução à Análise de Dados com Python

Olá, pessoal! Bem-vindos a este repositório. O objetivo é explicar um pouco sobre o universo da análise de dados, mostrando um fluxo de trabalho básico.

## 📖 Por que Análise de Dados?

Vivemos na era dos dados. Cada clique, cada compra online, cada rota no GPS gera um volume gigantesco de informações. Diante disso, é preciso saber extrair as informações, encontrar padrões e transformar esse ruído em conhecimento.

Esse conhecimento nos ajuda a tomar decisões mais inteligentes, otimizar produtos e fazer novas descobertas.

É nesse contexto que entram as bibliotecas que vamos usar: **NumPy** e **Pandas**.

Para escrever e executar os códigos em Python, podemos instalar no computador o Anaconda, uma distribuição do Python, e escolher a ferramenta JupyterLab. Porém, vocês também podem optar pelo Google Colab, um servidor que também permite escrever e executar código em Python diretamente no seu navegador. É só digitar Google Colab no Google que o servidor aparece.

---

## 🛠️ Ferramenta 1: NumPy (Python Numérico)

O NumPy é a biblioteca fundamental para computação numérica em Python.

Ele trabalha com matrizes e arranjos multidimensionais, permitindo cálculos rápidos e eficientes. Sua grande vantagem são as "operações vetorizadas", onde cálculos (como somas ou multiplicações) são aplicados a todos os elementos simultaneamente.

### Prática com NumPy

Primeiro, importamos a biblioteca:

```python
# Usamos 'np' como um apelido (para não precisar repetir 'numpy' novamente.
import numpy as np

Criando um Array Simples
Vamos criar um array (um vetor) de 1 dimensão. Todos os valores devem ser do mesmo tipo, por exemplo, todos os números decimais ou todos os números inteiros.

# Criando um array simples de números inteiros
arr = np.array([10, 20, 30, 40, 50], np.int16)
print("Array:", arr)
```

Ao executar o código, podemos ver o resultado. Note que aparecem os números escolhidos.

```python
Operações Vetorizadas
Veja como é fácil aplicar operações a todos os números de uma vez:
# Operações matemáticas vetorizadas
print("Multiplicado por 2:", arr * 2)
print("Soma total:", arr.sum())
print("Média:", arr.mean())
print("Desvio padrão:", arr.std())
```

Percebam que o NumPy multiplicou cada número do array por 2. Depois, o numpy somou todos os números que estão dentro do array, obtendo um valor de 150. Após isso, ele somou o valor total de 150 e dividiu pela quantidade de números (5), obtendo assim o valor da média. E, por fim, ele mediu o quão “dispersos” estão os dados em relação à média, fornecendo o valor do desvio padrão.

Agora iremos fazer um pouco diferente, ao invés de criarmos um array de uma dimensão, como fizemos antes, vamos criar um array bidimensional, também chamado de matriz. Uma estrutura composta de valores organizados em linhas e colunas, no nosso caso, vamos criar uma matriz de 2 linhas e 3 colunas.

Matrizes (Array Bidimensional)
Também podemos criar matrizes (linhas e colunas):
```python
# Criando uma matriz de 2 linhas e 3 colunas
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)

# '.T' calcula a transposta (inverte linhas e colunas)
print("Transposta:\n", matriz.T)
```

A forma como você agrupa os números nos colchetes vai definir exatamente como essa matriz será montada. Percebam que temos duas listas internas. A primeira, [1, 2, 3], se torna a primeira linha, e a segunda, [4, 5, 6], se torna a segunda linha. Observem também que o número de elementos dentro de cada linha define o número de colunas. Como cada linha tem 3 números, a nossa matriz tem 3 colunas. Quando usamos o comando T, realizamos o processo de transposição. Basicamente, as linhas da matriz original se tornam as colunas da nova matriz. Como a nossa matriz original tinha 2 linhas e 3 colunas, a transposta passará a ter 3 linhas e 2 colunas.

## 🛠️ Ferramenta 2: Pandas

Enquanto o numpy lida com as operações numéricas, o pandas lida com a manipulação de dados estruturados, como banco de dados, planilhas e tabelas. Mas o que o pandas faz? Ele lê, limpa, transforma, analisa e representa visualmente os dados em formato de tabelas. As suas principais estruturas são o DataFrame e a Series, onde o DataFrame é a tabela inteira e a Series é uma coluna da tabela.

### Prática com NumPy e Pandas

Agora que vimos o básico de operações numéricas com NumPy, vamos usar o Pandas (que usa o NumPy por baixo dos panos) para importar, limpar e analisar um conjunto de dados real.

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





