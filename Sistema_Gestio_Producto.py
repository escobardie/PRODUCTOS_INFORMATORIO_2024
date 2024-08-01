# Desafío 1: Sistema de Gestión de Productos
# Objetivo: Desarrollar un sistema para manejar productos en un inventario.
# Requisitos:
#     • Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
#     • Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
#     • Implementar operaciones CRUD para gestionar productos del inventario.
#     • Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
#     • Persistir los datos en archivo JSON.
import json
import os

class Producto:
    def __init__(self, codigo, nombre, precio,  stock, proveedor):
        '''INICIALIZAMOS EN CONSTRUCTOR'''
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__proveedor = proveedor
    
    ### DEFINIMOS GETTER AND SETTER
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, value):
        self.__precio = value

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, value):
        self.__stock = value

    @property
    def proveedor(self):
        return self.__proveedor

    @proveedor.setter
    def proveedor(self, value):
        self.__proveedor = value

    def to_dict(self):
        '''RETORNAMOS UN DICCIONARIO (CLAVE : VALOR)'''
        return {
            "codigo" : self.codigo,
            "nombre" : self.nombre,
            "precio" : self.precio,
            "stock" : self.stock,
            "proveedor" : self.proveedor
        }

    def __str__(self):
        '''RETORNAMOS CODIGO Y NOMBRE'''
        return f"Codigo: {self.codigo} - Nombre: {self.nombre}"


class ProductoAlimento(Producto):
    def __init__(self, codigo, nombre, precio,  stock, proveedor, fecha_vencimiento):
        super().__init__(codigo, nombre, precio,  stock, proveedor)
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, value):
        self.__fecha_vencimiento = value

    def to_dict(self):
        '''RETORNAMOS UN DICCIONARIO (CLAVE : VALOR) CON UN ELEMENTO MAS'''
        data = super().to_dict()
        data["fecha_vencimiento"] = self.fecha_vencimiento
        return data
    
    def __str__(self):
        '''RETORNAMOS CODIGO, NOMBRE Y FECHA DE VENCIMIENTO'''
        return f"{super().__str__()} - Fecha de vencimiento: {self.fecha_vencimiento}"


class ProductoElectronico(Producto):
    def __init__(self, codigo, nombre, precio,  stock, proveedor, meses_garantia):
        super().__init__(codigo, nombre, precio,  stock, proveedor)
        self.__meses_garantia = meses_garantia

    @property
    def meses_garantia(self):
        return self.__meses_garantia

    @meses_garantia.setter
    def meses_garantia(self, value):
        self.__meses_garantia = value

    def to_dict(self):
        '''RETORNAMOS UN DICCIONARIO (CLAVE : VALOR) CON UN ELEMENTO MAS'''
        data = super().to_dict()
        data["meses_garantia"] = self.meses_garantia
        return data
    
    def __str__(self):
        '''RETORNAMOS CODIGO, NOMBRE Y MESES DE GARANTIA'''
        return f"{super().__str__()} - Garantia Validad por: {self.meses_garantia} meses"


class CRUDProductos:
    # # Especifica la ubicación y el nombre del archivo donde se guardará el JSON
    # directorio = os.getcwd()  # Obtiene el directorio actual
    # nombre_archivo = 'productos.json'
    # ruta_completa = os.path.join(directorio, nombre_archivo)

    def __init__(self):
        # Especifica la ubicación y el nombre del archivo donde se guardará el JSON
        directorio = os.getcwd()  # Obtiene el directorio actual
        nombre_archivo = 'productos.json'
        ruta_completa = os.path.join(directorio, nombre_archivo)
        ## self.archivo = archivo #ORIGINAL
        self.archivo = ruta_completa
    
    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)

        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error: #TODO  HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')

    def crear_producto(self, producto, tipo_producto): ## SE ENVIARA EL TIPO DE PRODUCTO YA SELECCIONADO EN EL MENU MAIN
        try:
            datos = self.leer_datos()
            codigo = producto.codigo

            if tipo_producto == '1':
                if 'productoElectronico' not in datos:
                    datos['productoElectronico'] = {}
                if str(codigo) not in datos['productoElectronico']:
                    datos['productoElectronico'][codigo] = producto.to_dict()
                    self.guardar_datos(datos)
                    print(f"Producto ELECTRONICO {codigo} creado correctamente.") #TODO aca ver como mostrar en __str__
                else:
                    print(f"Ya existe producto con CODIGO: '{codigo}'.")

            elif tipo_producto == '2':
                if 'productoAlimenticio' not in datos:
                    datos['productoAlimenticio'] = {}
                if str(codigo) not in datos['productoAlimenticio']:
                    datos['productoAlimenticio'][codigo] = producto.to_dict()
                    self.guardar_datos(datos)
                    print(f"Producto ALIMENTICIO {codigo} creado correctamente.") #TODO aca ver como mostrar en __str__
                else:
                    print(f"Ya existe producto con CODIGO: '{codigo}'.")
            else:
                    print("Erro entro por aca")                      

        except Exception as error: #TODO HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')

    def leer_producto(self, codigo, tipo_producto):
        try:
            datos = self.leer_datos()
            if tipo_producto == '1':
                if codigo in datos['productoElectronico']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    for key, value in datos['productoElectronico'][codigo].items():
                        print(f"    {key}: {value}")
                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')
            else:
                if codigo in datos['productoAlimenticio']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    for key, value in datos['productoAlimenticio'][codigo].items():
                        print(f"    {key}: {value}")
                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')

        except Exception as error: #TODO HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')

    def actualizar_producto(self, codigo, tipo_producto):
        try:
            datos = self.leer_datos()
            
            if tipo_producto == '1':
                if codigo in datos['productoElectronico']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    nuevo_ingreso = int(input('Ingrese cantidad del ingreso: '))
                    datos['productoElectronico'][codigo]['stock'] += nuevo_ingreso
                    #input('Presione enter para continuar...')
                    self.guardar_datos(datos)
                    
                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')

            else:
                if codigo in datos['productoAlimenticio']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    nuevo_ingreso = int(input('Ingrese cantidad del ingreso: '))
                    datos['productoAlimenticio'][codigo]['stock'] += nuevo_ingreso
                    #input('Presione enter para continuar...')
                    self.guardar_datos(datos)

                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')

        except Exception as error: #TODO HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')

    def eliminar_producto(self, codigo, tipo_producto):
        try:
            datos = self.leer_datos()
            
            if tipo_producto == '1':
                if codigo in datos['productoElectronico']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    del datos['productoElectronico'][codigo]
                    input('Presione enter para ELIMINAR...')
                    self.guardar_datos(datos)
                    print(f'Producto CODIGO:{codigo} eliminado correctamente')
                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')
            else:
                if codigo in datos['productoAlimenticio']:
                    print(f'Se encontró PRODUCTO con CODIGO {codigo}')
                    del datos['productoAlimenticio'][codigo]
                    input('Presione enter para ELIMINAR...')
                    self.guardar_datos(datos)
                    print(f'Producto CODIGO:{codigo} eliminado correctamente')
                else:
                    print(f'No se encontró PRODUCTO con CODIGO {codigo}')

        except Exception as error: #TODO HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')
