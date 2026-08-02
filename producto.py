from datetime import datetime
class Producto:
    def __init__(self,nombre, categoria, precio,cantidad):
        self.__id = None
        self.__nombre = nombre
        self.__categoria = categoria  
        self.__precio = precio
        self.__cantidad = cantidad
        self.__fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
        pass
    
    def asignar_id(self, id):
        self.__id = id

    @property
    def nombre(self):
        return self.__nombre 
    @nombre.setter
    def nombre(self,nombre):
        if not nombre or nombre.strip()=="":
            raise ValueError("nombre no puede ser vacio")
        self.__nombre = nombre

    @property
    def categoria(self):
        return self.__categoria
    @categoria.setter
    def categoria(self,categoria):
        if not categoria or categoria.strip()=="":
            raise ValueError("categoria no puede ser vacio")
        self.__categoria = categoria

    @property
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,precio):
        if precio < 0:
            raise ValueError("Precio no puede ser negativo")
        self.__precio = precio

    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        if cantidad < 0:
            raise ValueError("cantidad no puede ser negativo")
        self.__cantidad = cantidad

    @property
    def fecha(self):
        return self.__fecha

    @property
    def id(self):
        return self.__id


    def __str__(self):
        if self.__id is not None:
            return f"ID: {self.__id} - {self.__nombre} {self.__precio} - (cantidad:{self.__cantidad}UND)"

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "cantidad": self.__cantidad,
            "categoria": self.__categoria,
            "fecha": self.__fecha
        }

    @classmethod
    def from_dict(cls, datos):
        producto = cls(
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["cantidad"]
            
        )
        producto.asignar_id(datos["id"])
        producto.fecha = datos.get("fecha", "2024-01-01")
        return producto
    
    