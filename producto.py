from datetime import datetime
class Producto:
    def __init__(self,nombre, categoria, precio,cantidad):
        
        self.nombre = nombre
        self.categoria = categoria  
        self.precio = precio
        self.cantidad = cantidad
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        pass

    def __str__(self):
        return f"ID: {self.id} - {self.nombre} {self.precio}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "categoria": self.categoria,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        producto = cls(
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
            
        )
        producto.id = datos["id"]
        producto.fecha = datos.get("fecha", "2024-01-01")
        return producto
    
    