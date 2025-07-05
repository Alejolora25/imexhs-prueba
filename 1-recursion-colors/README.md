# 🧩 Recursion and Colors - Technical Test (IMEXHS)

Este proyecto resuelve el reto técnico "Recursion and Colors" propuesto en la prueba para el rol de Developer. El objetivo es trasladar discos de diferentes tamaños y colores de una torre inicial a una torre destino cumpliendo ciertas reglas.

---

## 📜 Enunciado resumido

Dado un número `n` de discos con distintos tamaños y colores, apilados inicialmente en una varilla origen, se deben mover a una varilla destino utilizando una varilla auxiliar, respetando las siguientes reglas:

1. Solo se puede mover un disco a la vez.
2. Un disco más grande **no puede** colocarse sobre uno más pequeño.
3. **Dos discos del mismo color no pueden** colocarse uno sobre otro, aunque difieran en tamaño.
4. La solución debe implementarse en **Python** y debe usar **recursión**.

---

## 📁 Estructura del proyecto

```
recursion-and-colors/
│
├── main.py               # Implementación principal de la solución
├── test_cases.py         # Archivo con casos de prueba básicos
├── README.md             # Este archivo
└── requirements.txt      # Dependencias del proyecto (vacío si usas solo Python estándar)
```

---

## ▶️ Cómo ejecutar


cd recursion-and-colors
```

### 2. Asegúrate de tener Python 3.8 o superior:

```bash
python --version
```

### 3. Ejecuta los casos de prueba:

```bash
python test_cases.py
```

---

## 🔎 Ejemplo de entrada y salida

### Entrada:
```python
n = 3
disks = [(3, "red"), (2, "blue"), (1, "red")]
```

### Salida esperada:
```python
[
 (1, "A", "C"),
 (2, "A", "B"),
 (1, "C", "B"),
 (3, "A", "C"),
 (1, "B", "A"),
 (2, "B", "C"),
 (1, "A", "C")
]
```

---

## ❌ Ejemplo sin solución

### Entrada:
```python
n = 3
disks = [(3, "red"), (2, "red"), (1, "red")]
```

### Salida:
```python
-1
```

---

## 🧠 Lógica de solución

- Se utiliza un algoritmo **recursivo con búsqueda por profundidad (DFS)** e incremento de profundidad (iterative deepening) para encontrar la secuencia válida de movimientos.
- Cada estado del juego se representa como una tupla de tuplas (inmutable), lo que permite llevar control de los estados visitados.
- Se cumple con todas las restricciones del enunciado, incluyendo el uso obligatorio de recursión.

---

## ✅ Requisitos

Este proyecto no tiene dependencias externas. Solo requiere:

- Python 3.8+
- Sistema operativo Windows, macOS o Linux

---

## 👨‍💻 Autor

**Jesús Alejandro Lora Tovar**  
Desarrollador backend especializado en Java, Spring Boot, Python y arquitectura limpia.  
Contacto: [alejandroloratovar@outlook.com] – GitHub: [(https://github.com/Alejolora25/)]