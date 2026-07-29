#  Sistema de Inventario en Python

> Sistema de gestión de inventario para productos con persistencia en archivos JSON.  
> Desarrollado como proyecto de aprendizaje en Python.

---

##  Funcionalidades

-  Agregar productos (nombre, categoría, precio, cantidad)
-  Ver todos los productos en formato tabla
-  Buscar productos por ID
-  Eliminar productos por ID
-  Actualizar stock (cantidad)
-  Ver valor total del inventario
-  Reporte de productos agrupados por categoría
-  Persistencia en archivo JSON
-  ID automático para cada producto
-  Manejo de errores y validaciones

---

##  Cómo ejecutar el programa

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU-USUARIO/sistema-inventario-python.git
cd sistema-inventario-python
python main.py
```

## Estructura del proyecto

inventario/
├── inventario.py      # Lógica del inventario
├── producto.py        # Clase Producto
├── main.py            # Menú interactivo
├── lista.json         # Archivo de datos
└── README.md          # Este archivo

## Tecnologías utilizadas

- **Python 3.14+**
- **Módulos nativos**:
  - `json` → persistencia de datos
  - `os` → manejo de rutas de archivos
  - `datetime` → registro de fechas
- **Persistencia**: Archivos JSON

## Autor

**Danie Felipe Castro**
- [GitHub](https://github.com/danielfelipeca98)