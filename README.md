# 📌 Recursão em Python - Exercícios Resolvidos

Bem-vindo(a) ao repositório de exercícios resolvidos sobre **recursão em Python**! 🐍🚀

## 📂 Estrutura do Repositório

```
📦 recursao-python
 ┣ 📜 ex1.py
 ┣ 📜 ex2.py
 ┣ 📜 ex3.py
 ┣ 📜 ex4.py
 ┣ 📜 README.md
```

Cada arquivo contém um exercício resolvido de forma recursiva, com exemplos de entrada e saída.

---

## 🚀 Exercícios

### 1️⃣ Reverter os Caracteres de uma String
📄 **Arquivo:** `ex1.py`

📌 **Descrição:** 
Escreve uma função recursiva que recebe uma string e devolve a string invertida. Não utiliza laços (`for` ou `while`).

🔹 **Exemplo de uso:**
```python
from ex1 import reverter_caracteres

print(reverter_caracteres("python"))  # Saída esperada: "nohtyp"
```

---

### 2️⃣ Soma de Números em uma Lista Aninhada
📄 **Arquivo:** `ex2.py`

📌 **Descrição:** 
Implementa uma função recursiva que calcula a soma de todos os números dentro de uma lista, mesmo que estejam dentro de sublistas aninhadas.

🔹 **Exemplo de uso:**
```python
from ex2 import soma_lista_aninhada

print(soma_lista_aninhada([1, [2, 3], [4, [5]]]))  # Saída esperada: 15
```

---

### 3️⃣ Contar Caracteres em uma String
📄 **Arquivo:** `ex3.py`

📌 **Descrição:**
Cria uma função recursiva que conta quantas vezes um caractere específico aparece em uma string.

🔹 **Exemplo de uso:**
```python
from ex3 import contar_caracteres

print(contar_caracteres("banana", "a"))  # Saída esperada: 3
```

---

### 4️⃣ Encontrar o Índice do Maior Elemento
📄 **Arquivo:** `ex4.py`

📌 **Descrição:**
Escreve uma função recursiva que encontra o índice do maior elemento dentro de uma lista de números.

🔹 **Exemplo de uso:**
```python
from ex4 import indice_maior_elemento

print(indice_maior_elemento([1, 5, 3, 9, 2]))  # Saída esperada: 3
```

---

## 🛠️ Como Executar os Exercícios

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/recursao-python.git
   ```
2. **Acesse o diretório**
   ```bash
   cd recursao-python
   ```
3. **Execute os arquivos individualmente**
   ```bash
   python3 ex1.py
   ```

---

