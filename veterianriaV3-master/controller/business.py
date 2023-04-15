from model import model
from datetime import datetime
from datetime import date



def iniciar_sesion(username, password,Veterinaria1):
    

    for Usuarios in Veterinaria1.Usuarios:
            if Usuarios.username == username and Usuarios.password == password:
                Veterinaria1.usuario_actual= Usuarios.rol
                return Usuarios
    return False
def cerrar_sesion():
        usuario_actual = None


def registrar_usuario(username, password, rol,Veterinaria1):
    if rol=='Vendedor':
        
        Vendedor=model.usuario(username,password,"Vendedor")
        Veterinaria1.Usuarios.append(Vendedor)
        print('Vendedor registrado correctamente')
    elif rol=='Veterinario':   
        veterinario=model.usuario(username,password,"veterinario")
        Veterinaria1.Usuarios.append(veterinario)
        print('veterinario registrado correctamente')
    else:
        #Se uso un menu pensando en que el usuario no se vaya a equivocar ingresando el ROL de la persona por lo cual este else no sera muy util 
        print('Por favor intentalo de nuevo')
        exit()   
def registrar_Persona(cedula, nombre, edad, Veterinaria1):
    for persona in Veterinaria1.personas:
        if persona.cedula == cedula:
            print("Error: la cédula ya existe en el sistema.")
            return
    
    nuevo_vendedor = model.Persona(cedula, nombre, edad)
    Veterinaria1.personas.append(nuevo_vendedor)
    print(f'{nombre} registrado correctamente')
    print('')
    
    
    print("Por favor, elija el rol de la persona que ingreso")
    print("1. Veterinario")
    print("2. Vendedor")
    print("3. Dueño")

    opcion = input("Escriba el número de su opción: ")

    if opcion == "1":
        rolP = "Veterinario"
    elif opcion == "2":
        rolP = "Vendedor"
    elif opcion == "3":
        pass
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 3.")
        print('')
        exit()

    if opcion=='1' or opcion=='2':
        registrar_usuario(input('Ingrese el usuario: '),input('Ingrese la contraseña: '),rolP,Veterinaria1)
        print("")
    else:
        print('')
        print('Gracias por confiar en nosotros')


def registrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento, Veterinaria1):
# Buscar la mascota por id
    mascota = buscar_mascota_por_id(id_mascota, Veterinaria1)
    mascota_existente = mascota != None

    if not mascota_existente:
        print('La mascota no existe en el sistema')
        return

    # Crear el objeto HistoriaClinica
    historia_clinica = model.HistoriaClinica(id_mascota, fecha,medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento)

    # Verificar si ya existe una historia clínica para la mascota en la fecha especificada
    if id_mascota in Veterinaria1.historiasClinicas and fecha in Veterinaria1.historiasClinicas[id_mascota]:
        print(f'Ya existe una historia clínica para la mascota con id {id_mascota} registrada en la fecha {fecha}.')
        return

    # Agregar la historia clínica a la lista correspondiente
    if id_mascota not in Veterinaria1.historiasClinicas:
        Veterinaria1.historiasClinicas[id_mascota] = {}

    Veterinaria1.historiasClinicas[id_mascota][fecha] = historia_clinica
    print('')
    print('Historia registrada con exito')
    print(fecha)
def buscar_historia_clinica(id_mascota, fecha, Veterinaria1):

    print(' ')
    if id_mascota in [mascota.id for mascota in Veterinaria1.mascotas] and fecha in Veterinaria1.historiasClinicas[id_mascota]:
        historia_clinica = Veterinaria1.historiasClinicas[id_mascota][fecha]
        print(f'Historia clínica de la mascota con id {id_mascota} registrada en la fecha {fecha}:')
        print(f'Motivo de consulta: {historia_clinica.motivo_consulta}')
        print(f'Sintomatología: {historia_clinica.sintomatologia}')
        print(f'Diagnóstico: {historia_clinica.diagnostico}')
        print(f'Procedimiento: {historia_clinica.procedimiento}')
        print(f'Medicamento: {historia_clinica.medicamento}')
        print(f'Dosis: {historia_clinica.dosis}')
        print(f'ID de orden: {historia_clinica.id_orden}')
        print(f'Historial de vacunación: {historia_clinica.historial_vacunacion}')
        print(f'Alergias: {historia_clinica.alergias}')
        print(f'Detalle del procedimiento: {historia_clinica.detalle_procedimiento}')

    else: 
        print("La historia clinica no existe")

# def buscar_historia_clinica2(id_mascota, veterinaria):
    if id_mascota in Veterinaria1.historiasClinicas:
        return Veterinaria1.historiasClinicas[id_mascota]
    else:
        print('No existe historia clínica para la mascota')
        return None


def registrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,
Veterinaria1):
    print('Ingreso a metodo registrar mascota')
    # Verificar si la mascota ya existe en el sistema
    for Mascota in Veterinaria1.mascotas:
        if Mascota.id == id :
            print("Error al ingresar la mascota: la mascota ya existe en el sistema.") ###########################
            return
    
    # Verificar si el dueño está registrado en el sistema
    dueno_existente = False
    for persona in Veterinaria1.personas:
        if persona.cedula == cedula_dueno:
            dueno_existente = True
            break

    if not dueno_existente:
        print("El dueño no está registrado en el sistema.")
        return
    
    # Si la mascota no existe y el dueño está registrado, registrar la mascota
    nueva_mascota = model.Mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso)
    Veterinaria1.mascotas.append(nueva_mascota)
    print('____________________________________________')
    print(f"La mascota {nombre} se registró con éxito.")
    print('')
def buscar_mascota_por_id(id,Veterinaria1):
        # Buscar la mascota por ID en la lista de mascotas existentes
        print(' ')
        for Mascota in Veterinaria1.mascotas:
            if Mascota.id == id:
                # Imprimir los datos de la mascota
                print("Datos de la mascota:")
                print('')
                print("ID:", Mascota.id)
                print("Nombre:", Mascota.nombre)
                print("Cédula del dueño:", Mascota.cedula_dueno)
                print("Edad:", Mascota.edad)
                print("Especie:", Mascota.especie)
                print("Raza:", Mascota.raza)
                print("Características:", Mascota.caracteristicas)
                print("Peso:", Mascota.peso)
                return Mascota

        # Si no se encuentra la mascota, imprimir un mensaje y devolver None
        print("No se encontró ninguna mascota con el ID proporcionado.")
        return None


"""def crear_orden(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis,estado, veterinaria1):
    
    for Orden in veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            print("La orden ya existe en el sistema")
            return
        
    nueva_orden= model.Orden(id_orden, id_mascota, cedula_dueno,cedula_veterinario,medicamento,dosis,estado)
    veterinaria1.ordenes.append(nueva_orden)
    print('')
    print("La orden se ha registrado correctamente")
    print('')
    
    id_busqueda_orden= id_orden
    
    buscar_ordenID(id_busqueda_orden,veterinaria1)"""

def crear_orden(id_orden, id_mascota, cedula_dueno, cedula_veterinario, medicamento, dosis, estado, veterinaria1):
   # Verificar si la orden ya ha sido registrada
    orden_existente = False
    for orden in veterinaria1.ordenes:
        if orden.id_orden == id_orden:
            orden_existente = True
            break

    if orden_existente:
        print('La orden ya existe en el sistema')
        return
   
    # Verificar si la mascota existe
    mascota_existente = False
    for mascota in veterinaria1.mascotas:
        if mascota.id == id_mascota:
            mascota_existente = True
            break

    if not mascota_existente:
        print('La mascota no existe en el sistema')
        return

    # Verificar si existe una historia clínica para la mascota
    historia_existente = id_mascota in veterinaria1.historiasClinicas
    if not historia_existente:
        print('No existe historia clínica para la mascota')
        return
    
    
        
    
   
    """  for historia in veterinaria1.historiasClinicas.values():
        if historia.id_orden == id_orden:
            print("La orden ya existe en la historia clínica.")
            return"""
    
    nueva_orden= model.Orden(id_orden, id_mascota, cedula_dueno,cedula_veterinario,medicamento,dosis,estado)
    veterinaria1.ordenes.append(nueva_orden)
    print('')
    print("La orden se ha registrado correctamente")
    print('')
    
    id_busqueda_orden = id_orden
    buscar_ordenID(id_busqueda_orden, veterinaria1)
    
def buscar_ordenID(id_orden, Veterinaria1):
    existe_orden=False
    print('VALIDAR INGRESO AL BUSCAR ORDEN')
    for Orden in Veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            existe_orden = True
            print("Datos de la orden" ,Orden.id_orden)
            print("*************************************")
            print("ID mascota: " ,Orden.id_mascota)
            print("Cedula dueño: " ,Veterinaria1.Orden.cedula_dueno)
            print("Cedula veterinario: " ,Orden.cedula_veterinario)
            print("Medicamento recetado", Orden.medicamento)
            print("Dosis enviada: ", Orden.dosis)
            print("Orden generada a la fecha: ", Orden.fecha_generacion)
            print("Estado: ", Orden.estado)
            print("*****************************************************")
            break
    if(existe_orden == False):
        print("No existe una orden registrada con el id ", id_orden)
def anular_orden(id_orden, Veterinaria1):

    existe_orden=False
    print('VALIDAR INGRESO AL BUSCAR ORDEN')
    for Orden in Veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            existe_orden = True
            Orden.estado = "ANULADA"
            buscar_ordenID(id_orden,Veterinaria1)
            break
    if(existe_orden == False):
        print("No existe una orden registrada con el id ", id_orden)
    
    
    """ # Buscar la orden por su ID
        for orden in self.lista_ordenes:
            if orden.id_orden == id_orden and orden.id_mascota == id_mascota \
                    and orden.id_dueño == id_dueño and orden.id_veterinario == id_veterinario:
                # Cambiar el estado de la orden a "Anulada" y registrar la fecha de anulación
                orden.estado = "Anulada"
                orden.fecha_anulacion = datetime.now()

                # Buscar la historia clínica correspondiente y agregar un registro de anulación de la orden
                for mascota in self.lista_mascotas:
                    if mascota.id == id_mascota and mascota.cedula_dueño == id_dueño:
                        if id_mascota in self.historias_clinicas:
                            historia = self.historias_clinicas[id_mascota]
                        else:
                            historia = {}
                            self.historias_clinicas[id_mascota] = historia
                        registro = {
                            "fecha": datetime.now(),
                            "medico_veterinario": id_veterinario,
                            "motivo_consulta": "Anulación de orden de venta",
                            "sintomatologia": "",
                            "diagnostico": "",
                            "procedimiento": "",
                            "medicamento": "",
                            "dosis_medicamento": "",
                            "id_orden": id_orden,
                            "historial_vacunacion": "",
                            "alergias_medicamentos": "",
                            "detalle_procedimiento": "",
                            "anulacion_orden": True
                        }
                        historia[registro["fecha"]] = registro
                print("La orden ha sido anulada con éxito.")
                return
        print("No se encontró la orden con los datos proporcionados.")"""


def registrar_factura_venta(id_factura, id_orden, nombre_producto, valor, cantidad, Veterinaria1):
    # Pedir datos de la factura y la orden
    print("Ingreso a registrar factura venda VALIDACION")
    # Aquí podrías agregar más input() para pedir información adicional, como el nombre del cliente, por ejemplo.

    # Buscar la orden correspondiente al ID ingresado
    existe_orden = False
    for Orden in Veterinaria1.ordenes:
        if Orden.id_orden == id_orden:
            existe_orden = True
            # Validar el estado de la orden
            if Orden.estado == "ANULADA":
                print('VALIDAR INGRESO A ANULADO')
                print("No se puede vender con una orden anulada.")
           
            elif Orden.estado == "ACTIVO":
                print('VALIDAR INGRESO A ACTIVO')

                # Crear la factura nueva
                for FacturaVenta in Veterinaria1.facturas_ventas:
                    if FacturaVenta.id_orden == id_orden:
                        print("el id ingresado ya existe en el sistema")
                else:
                    
                    factura_nueva = model.FacturaVenta(id_factura, id_orden, nombre_producto, valor, cantidad)
                    factura_nueva.precio_total = valor * cantidad  # Agregar campo de precio total

                # Agregar la factura nueva a la lista de facturas de la veterinaria
                Veterinaria1.facturas_ventas.append(factura_nueva)
                print("***************************************************")
                print("*****************************************************")
                print("Datos de la factura" , id_factura)
                print("*************************************")
                print("Mascota NO. : " ,Orden.id_mascota)
                print("Cedula dueño NO. : " ,Orden.cedula_dueno)
                
                print("orden asociada NO. : " ,id_orden)
                print("Nombre del medicamento: " ,nombre_producto)
                print("precio por unidad: " ,valor)
                print("Cantidad a llevar", cantidad) 
                print(f'Valor total a pagar: {factura_nueva.precio_total}')
                print("Se ha registrado la factura")

                

            break
        elif not existe_orden:
            print("No existe una orden registrada con el id ", id_orden)

def consultar_facturas_ventas(id_orden, veterinaria1):
    existe_orden=False
    for FacturaVenta in veterinaria1.facturas_ventas:
        if FacturaVenta.id_orden == id_orden:
            existe_orden = True
            print("*****************************************************")
            print("Datos de la factura" , FacturaVenta.id_factura)
            print("*************************************")
            print("orden asociada NO. : " ,FacturaVenta.id_orden)
            print("Nombre del medicamento: " ,FacturaVenta.nombre_producto)
            print("precio por unidad: " ,FacturaVenta.valor)
            print("Cantidad a llevar", FacturaVenta.cantidad) 
            
            
            print("*****************************************************")
        elif (existe_orden == False):
            print("No existe orden asociada al id ", id_orden)
            
def factura_sin_orden(id_factura,cedula_cliente, producto, valor, cantidad_llevar, Veterinaria1):
    
    
 
    total_pagar= valor*cantidad_llevar
    
    fecha=date.today()
    
    print("******************************************")
    print("Datos de la factura" , id_factura)
    print("*************************************")
    print("Fecha: ", fecha)
    print("cedula cliente NO. : " ,cedula_cliente)
    print("Nombre del producto : " ,producto)
    print("valor producto : " ,valor)
    print("Cantidad a llevar: ", cantidad_llevar)
    print("Total pagar: ", total_pagar)
            
    print("*****************************************************")