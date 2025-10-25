# 🚀 Projeto de Introdução à Análise de Dados com Python

Olá, pessoal! Bem-vindos a este repositório. O objetivo é explicar um pouco sobre o universo da análise de dados, mostrando um fluxo de trabalho básico.

## 📖 Por que Análise de Dados?

Vivemos na era dos dados. Cada clique, cada compra online, cada rota no GPS gera um volume gigantesco de informações. Sendo assim, não basta apenas ter os dados, é preciso saber extrair as informações, encontrar padrões e transformar esse ruído em conhecimento.

Esse conhecimento nos ajuda a tomar decisões mais inteligentes, otimizar produtos e fazer novas descobertas.

É nesse contexto que entram as bibliotecas que vamos usar: **NumPy** e **Pandas**.

---

## 🛠️ Ferramenta 1: NumPy (Python Numérico)

O NumPy é a biblioteca fundamental para computação numérica em Python.

Ele trabalha com matrizes e arranjos multidimensionais, permitindo cálculos rápidos e eficientes. Sua grande vantagem são as "operações vetorizadas", onde cálculos (como somas ou multiplicações) são aplicados a todos os elementos de uma vez.

### Prática com NumPy

Primeiro, importamos a biblioteca:

```python
# Usamos 'np' como um apelido (para não precisar repetir 'numpy' novamente.
import numpy as np

Criando um Array Simples
Vamos criar um array (um vetor) de 1 dimensão. Todos os valores devem ser do mesmo tipo.

# Criando um array simples de números inteiros
arr = np.array([10, 20, 30, 40, 50], np.int16)
print("Array:", arr)
