
# 🧪 Estimador de Área de Manchas - Angular App

Aplicación desarrollada en Angular para estimar el área de una mancha en imágenes binarias usando muestreo aleatorio. Esta aplicación forma parte del reto técnico #4 para la empresa **IMEXHS**.

---

## 🖼️ ¿Cómo Funciona?

1. Carga una imagen binaria (blanco = mancha, negro = fondo).
2. Selecciona cuántos puntos aleatorios deseas generar.
3. Calcula el área estimada de la mancha en píxeles cuadrados.
4. Visualiza la tabla con los resultados históricos.
5. Consulta la metodología paso a paso en la pestaña "Metodología".

---

## 🛠️ Tecnologías

- ✔️ Angular 17+
- ✔️ Angular Standalone Components
- ✔️ Angular Material (tema Azure/Blue)
- ✔️ Bootstrap (layout responsivo)
- ✔️ RxJS Signals
- ✔️ TypeScript
- ✔️ SCSS moderno

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Alejolora25/imexhs-prueba.git

# Ir al directorio del reto 4
cd imexhs-prueba/4-angular-app/frontend

# Instalar dependencias
npm install

# Iniciar la aplicación
npm start
```

La app se abrirá en tu navegador en:  
[http://localhost:4200](http://localhost:4200)

---

## 📸 Capturas

| Cargar Imagen y Ver Resultados | Metodología Interactiva |
|-------------------------------|--------------------------|
| ![Imagen](https://via.placeholder.com/400x200?text=Preview) | ![Imagen](https://via.placeholder.com/400x200?text=Step-by-step) |

---

## ✅ Funcionalidades

- 📤 Subida de imagen binaria.
- 🎯 Generación aleatoria de puntos sobre el canvas.
- 🧮 Cálculo dinámico del área de la mancha.
- 🧾 Historial de resultados con tabla interactiva (Angular Material).
- 🪜 Guía visual paso a paso con `mat-stepper`.

---

## 📂 Estructura de Componentes

```
frontend/
├── components/
│   ├── image-upload/         # Subida y renderizado de imagen
│   ├── area-result-table/    # Tabla de resultados con Angular Material
│   └── method-carousel/      # Stepper para explicar la metodología
├── services/
│   └── area-result.service.ts  # Lógica de almacenamiento en memoria
```

---

## 🧠 Metodología del Cálculo

> Área estimada = Ancho × Alto × (ni / n)

Donde:
- **n**: número de puntos generados.
- **ni**: puntos que caen dentro de la mancha (pixeles blancos).
- Se considera blanco como valores RGB mayores a 200.

---

## 📋 Notas Adicionales

- El diseño es **responsive** gracias al uso de **Bootstrap Grid**.
- Se utilizó el tema **Azure Blue de Angular Material**.
- Separamos lógica en servicios (`area-result.service.ts`).
- La app está completamente **autocontenida**: no requiere backend.

---

## 👤 Autor

**Jesús Alejandro Lora Tovar**  
📧 alejandroloratovar@outlook.com  
🔗 [https://github.com/Alejolora25](https://github.com/Alejolora25)
