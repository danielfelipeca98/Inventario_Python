import json
import os
from producto import Producto

class Inventario:
    def __init__(self):
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.join(directorio_actual, "lista.json")
        self.id = None
        self.productos = []
        self.contador_id = 0
        self.cargar()

    def cargar(self):
        try:
            with open(self.archivo,"r") as archivo: ##Cargar archivo
                datos = json.load(archivo) ##Lee el archivo

            self.contador_id = datos["contador_id"]## recupera el contador y lo guarda

            for producto_data in datos["productos"]:##recorre  la lista de productos
                producto = Producto.from_dict(producto_data)##convierte cada diccionario en un objeto
                self.productos.append(producto)##agreda el producto a la lista de inventario
            print(f"Cargados {len(self.productos)} productos")
        
        except FileNotFoundError:
            print("No hay datos guardados")
        
        except Exception as e:
            print(f"Error al cargar: {e}")

    def guardar(self):
        try:
            datos = {
                "contador_id":self.contador_id,
                "productos": [producto.to_dict()for producto in self.productos]
            }
            with open(self.archivo,"w") as archivo: ##toma el archivo para escribir archivo
              json.dump(datos, archivo, indent=2, ensure_ascii=False) ##Lee el archivo
                
        except Exception as e:
             print(f"Error al guardar: {e}")

    def agregar(self,nombre,categoria,precio,cantidad):
        
        try:
            newProduct = Producto (nombre,categoria,precio,cantidad)
            self.contador_id += 1
            newProduct.asignar_id(self.contador_id)
            self.productos.append(newProduct)
            self.guardar()
            return newProduct
            
        except Exception as e:
             print(f"Error al guardar: {e}")

    def listar(self):
        return self.productos

    def buscar(self,id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        raise ValueError(f"Producto con ID {id} no encontrado")    
    
    def eliminar(self,id):
        producto  = self.buscar(id)  
        self.productos.remove(producto) 
        self.guardar()

    def actualizar_stock(self,id,nueva_cantidad):
        if nueva_cantidad >= 0 :
            producto  = self.buscar(id) 
            producto.cantidad = nueva_cantidad
            self.guardar()
            return producto
        
    def valor_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio * producto.cantidad
        return total
    
    def reporte_categoria(self):
        reporte = {}
        for producto in self.productos:
            categoria = producto.categoria if producto.categoria else "Sin categoría"
            if categoria not in reporte:
                reporte[categoria]= []
            reporte[categoria].append(producto)
        return reporte  




                
            
    
