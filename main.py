from os import name, system
import platform
from time import sleep
from Sistema_Gestio_Producto import ProductoAlimento, ProductoElectronico, CRUDProductos

###################### LIMPIA PANTALLA ######################
# Para Unix/Linux/MacOS/BSD
if name == "posix":
    limpiar = "clear"
# Para DOS/Windows
elif name == "ce" or name == "nt" or name == "dos":
    limpiar = "cls"


# def limpiar_pantalla():
#     ''' Limpiar la pantalla según el sistema operativo'''
#     if platform.system() == 'Windows':
#         os.system('cls')
#     else:
#         os.system('clear') # Para Linux/Unix/MacOs

################## ESPERA Y LIMPIEZA #######################

def sleep_and_clear():
    """ GENERAMOS UN TIEMPO DE ESPERA Y PUEGO EJECUTAMOS UNA LIMPIEZA DE PANTALLA"""
    sleep(2)
    system(limpiar)

# time.sleep(3) tiempo de esperta antes de la siguiente ejecucion
# os.system(limpiar) limpia la pantalla



def menu_ppal():
    menu = input('''
        *******************************************
        *       Sistema Analisis de Datos         *
        *******************************************
        *                                         *
        *     1 - Add Producto                    *
        *     2 - Buscar Producto X codigo        *
        *     3 - Alctualizar Stock               *
        *     4 - Eliminar Producto               *
        *     5 - Mostrar Productos               *
        *     6 - Salir                           *
        *                                         *
        *******************************************
    Ingrese una opción: ''')
    return menu


def menu_tipo_producto():
    opciones = ['1','2','3']
    while True:
        menu = input('''
            *******************************************
            *          MENU TIPO DE PRODUCTO          *
            *******************************************
            *                                         *
            *     1 - Producto Electro                *
            *     2 - Producto Alimento               *
            *     3 - Salir                           *
            *                                         *
            *******************************************
        Ingrese una opción: ''')
        if str(menu) in opciones:
            return menu
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-3)')
            

def agregar_producto(control_productos, tipo_de_producto):
    try:
        #tipo_de_producto = menu_tipo_producto()
        codigo = input('Ingrese CODIG: ')
        nombre = input('Ingrese NOMBRE: ')
        precio = float(input('Ingrese PRECIO: '))
        stock = int(input('Ingrese Cantidad de STOCK: ') )
        proveedor = input('Ingrese PROVEEDOR: ')
        
        if tipo_de_producto == '1':
            meses_garantia = input('Ingrese Meses de Garantia: ')
            producto = ProductoElectronico(codigo, nombre, precio,  stock, proveedor, meses_garantia)
        elif tipo_de_producto == '2':
            fecha_vencimiento = input('Ingrese Fecha de Vencimiento DD/MM/AAAA: ')
            producto = ProductoAlimento(codigo, nombre, precio,  stock, proveedor, fecha_vencimiento)
        else:
            print("OCURRIO UN ERROR !ENTRO POR ACA!.")

        control_productos.crear_producto(producto, tipo_de_producto)
        input('ENTER para continuar...')
        sleep_and_clear()

    except Exception as error: #TODO HAY QUE SER MAS CLAROS CON LOS TIPOS DE ERRORES
            print(f'Error inesperado: {error}')

def buscar_producto_por_codigo(control_productos, tipo_de_producto):
    codigo = input('Ingrese el CODIGO del PRODUCTO: ')
    control_productos.leer_producto(codigo, tipo_de_producto)
    input('Presione enter para continuar...')

def actualizar_stock(control_productos, tipo_de_producto):
    codigo = input('Ingrese el CODIGO del PRODUCTO: ')
    control_productos.actualizar_producto(codigo, tipo_de_producto)
    input('Presione enter para continuar...')

def eliminar_producto_por_codigo(control_productos,tipo_de_producto):
    codigo = input('Ingrese el CODIGO del PRODUCTO: ')
    control_productos.eliminar_producto(codigo, tipo_de_producto)
    input('Presione enter para continuar...')

def mostrar_todos_los_productos(control_productos):
    print('=============== Listado completo de los PRODUCTOS =============== ')
    #producto = control_productos.leer_datos()#ORIGINAL
    #for categoria, productos in producto.items(): #ORIGINAL
    for categoria, productos in control_productos.leer_datos().items():
        print(f"Categoría: {categoria}")
        for producto_id, detalles in productos.items():
            print(f"  Producto ID: {producto_id}")
            for key, value in detalles.items():
                print(f"    {key}: {value}")
    print('================================================================== ')
    input('Presione enter para continuar...')


if __name__ == "__main__":
    # json_productos = 'productos_db.json'
    # control_productos = CRUDProductos(json_productos)
    control_productos = CRUDProductos()

    while True:
        opcion = menu_ppal()
        if opcion == '1': # AGREGAR PRODUCTO
            tipo_producto = menu_tipo_producto()
            agregar_producto(control_productos, tipo_producto)

        elif opcion == "2": # BUSCAR POR CODIGO
            tipo_producto = menu_tipo_producto()
            buscar_producto_por_codigo(control_productos, tipo_producto)
            
        elif opcion == "3": # ACTUALIZAR
            tipo_producto = menu_tipo_producto()
            actualizar_stock(control_productos, tipo_producto)

        elif opcion == "4": # ELIMINAR PRODUCTO
            tipo_producto = menu_tipo_producto()
            eliminar_producto_por_codigo(control_productos,tipo_producto)

        elif opcion == "5": # MOSTRAR TODOS LOS PRODUCTOS
            mostrar_todos_los_productos(control_productos)

        elif opcion == "6": # SALIR
            print('Saliendo del programa...')
            break
        
        else:
            system(limpiar)
            print('Opción no válida. Por favor, seleccione una opción válida (1-7)')
            sleep_and_clear()
        


