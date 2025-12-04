# Tutorial-Python

Repositorio oficial del **curso de Python aplicado a la Ciencia de Datos**, impartido por **Óscar Centeno**.  
El objetivo es guiar al estudiante desde los **fundamentos del lenguaje**, pasando por **ETL completo (Extract–Transform–Load)**, **manipulación avanzada de datos**, hasta **visualización profesional** con las librerías más utilizadas en la industria.

Este curso fue desarrollado con un enfoque 100% práctico y orientado a proyectos reales.

 ![class](/ima/ima1.webp)

---

## 🎯 Objetivos del Curso

Al finalizar el tutorial, la persona será capaz de:

- Comprender los **fundamentos de Python** y su ecosistema para análisis de datos.
- Dominar **VSCode** como IDE profesional, entender los archivos `.py` y `.ipynb`, y estructurar un proyecto correctamente.  
   [oai_citation:1‡Python en los proyectos de Datos.pptx](sediment://file_000000003888722f93c87440caedab9c)
- Utilizar Python como **herramienta ETL completa**:  
  - Ingesta de datos
  - Exploración (EDA)
  - Transformación profunda
  - Carga hacia un destino (archivos, bases de datos, nube)  
   [oai_citation:2‡Importar + EDA a los datos + exportar.pptx](sediment://file_000000006b08722f828e80b528d7c61e)  [oai_citation:3‡Transformación de datos.pptx](sediment://file_0000000043f4722f8a23bd7f689ad568)  [oai_citation:4‡La Carga de Datos.pptx](sediment://file_000000009e44722faa979dfdbd140dac)
- Trabajar con **estructuras de datos**: escalares, listas, vectores, matrices y DataFrames.  
   [oai_citation:5‡Python en los proyectos de Datos.pptx](sediment://file_000000003888722f93c87440caedab9c)
- Manipular DataFrames con gran detalle:  
  combinaciones, filtrado, creación de variables, strings, valores faltantes, pivotajes, joins y más.
- Crear **tablas**, visualizaciones y dashboards ligeros en Python.  
   [oai_citation:6‡Tablas + Gráficos + y aún más._.pptx](sediment://file_000000002380722fae523bef774b3a03)
- Utilizar múltiples librerías modernas de **gráficos**: Matplotlib, Seaborn, Plotly, ggplot, Bokeh.  
   [oai_citation:7‡Visualización gráfica en Python.pptx](sediment://file_000000006ccc722fada4cd19c50c7424)

---

## 🧩 Contenido del Curso

### **Módulo 0 — Buenas prácticas de código**
- Convenciones, estilo, indentación
- Comentarios y documentación
- Organización de proyectos
- Uso correcto de VSCode y extensiones
- Principios para código reproducible

---

### **Módulo A — Fundamentos de Python**
Basado en el material: *BP.ipynb* y *Python en los proyectos de Datos*  
 [oai_citation:8‡Python en los proyectos de Datos.pptx](sediment://file_000000003888722f93c87440caedab9c)

- ¿Qué es Python? ¿Por qué se usa en ciencia de datos?
- IDEs: VSCode, Anaconda
- Archivos `.py` vs `.ipynb`
- Variables y asignaciones
- Tipos de datos:
  - Números
  - Strings
  - Booleanos
  - Fechas
  - Listas, tuplas, conjuntos, diccionarios
- Python como calculadora
- Funciones y módulos
- Los módulos esenciales:
  - `os`, `sys`, `math`, `random`, `datetime`
  - Módulos de ciencia de datos: `numpy`, `pandas`, `matplotlib`, etc.

---

### **Módulo B — ETL: Importar datos + EDA + Exportar**
Basado en: *Importar + EDA + exportar.pptx*  
 [oai_citation:9‡Importar + EDA a los datos + exportar.pptx](sediment://file_000000006b08722f828e80b528d7c61e)

- El proceso ETL explicado
- Extracción:
  - Archivos CSV, Excel, TXT, JSON
  - Bases de datos (intro)
  - APIs y web scraping (intro)
- Establecer el espacio de trabajo (`os`, rutas)
- EDA general:
  - Tipos de estructuras
  - Columnas, tipos, dimensiones, duplicados
- EDA específico:
  - `head()`, `tail()`, `sample()`
  - Outliers, valores inconsistentes
- Exportación:
  - `.csv`
  - `.xlsx`
  - `.parquet`

---

### **Módulo C — Transformación de Datos**
Basado en: *Transformación de datos.pptx*  
 [oai_citation:10‡Transformación de datos.pptx](sediment://file_0000000043f4722f8a23bd7f689ad568)

Temas cubiertos:

#### **1. Columnas**
- Cambiar nombres y tipos
- Reordenar columnas
- Seleccionar o eliminar variables

#### **2. Filas**
- Filtros simples y múltiples condiciones
- Ordenamientos y muestreos
- `distinct` / categorías únicas

#### **3. Nuevas Variables**
- Operaciones numéricas
- Variables categóricas por condiciones
- Rangos
- Totales y métricas calculadas

#### **4. Variables String**
- Upper / lower
- Reemplazo
- Corte de texto
- Limpieza de caracteres

#### **5. Valores Faltantes**
- Identificación
- Imputación
- Manejo de outliers

#### **6. Estructura General**
- Concatenar
- Append
- Merge / Join

#### **7. Subestructuras**
- Tablas resumen
- Tablas filtradas

#### **8. Simulación**
- Crear dataframes sintéticos

---

### **Módulo D — La Carga (Load)**
Basado en: *La Carga de Datos.pptx*  
 [oai_citation:11‡La Carga de Datos.pptx](sediment://file_000000009e44722faa979dfdbd140dac)

- ¿Qué es una base de datos?
- Bases relacionales y no relacionales
- Sistemas comerciales (PostgreSQL, MySQL, etc.)
- Cargas:
  - Inicial
  - Incremental
  - Full Load
- Loading en la nube
- Limitaciones y buenas prácticas
- Cuándo usar ETL vs ELT

---

### **Módulo E — Visualización de la Información**
Basado en: *Visualización gráfica en Python.pptx*  
 [oai_citation:12‡Tablas + Gráficos + y aún más._.pptx](sediment://file_000000002380722fae523bef774b3a03)

- ¿Qué es una tabla?
- ¿Qué es un gráfico?
- Cómo escoger el gráfico adecuado
- Tipos principales:
  - Comparación
  - Relación
  - Composición
  - Distribución
  - Desviación
  - Evolución temporal
  - Mapas
  - Flujos

---

### **Módulo F — Tablas**
- Pandas para tablas
- Mostrado profesional:
  - `.style`
  - `tabulate`
  - `dataframe.to_markdown()`
  - Exportación a HTML y Excel

---

### **Módulo G — Gráficos**
Basado en: *Gráficos en Python.pptx*  
 [oai_citation:13‡Visualización gráfica en Python.pptx](sediment://file_000000006ccc722fada4cd19c50c7424)

- **Matplotlib**
- **Seaborn**
- **ggplot (plotnine)**
- **Bokeh**
- **Plotly**

Cada caso con:
- Sintaxis base
- Opciones más usadas
- Personalización
- Ejemplos claros

---

## 📂 Estructura del Repositorio

```text
Tutorial-Python/
├── 0. Buenas prácticas de código/
├── A. Fundamentos/
├── B. Importar Datos + EDA + exportar/
├── C. La transformación/
├── D. La carga/
├── Data Manipulation/
│   ├── Combinar DataFrames
│   ├── Crear variables
│   ├── Descriptive statistics
│   ├── Inspección de datos
│   ├── Modificar filas y columnas
│   ├── Modificar strings
│   ├── Valores faltantes
│   ├── Pivotear
│   └── Directorio y exportaciones
├── E. Visualización/
├── F. Tablas/
└── G. Gráficos/
```

![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white)
