from controller import business
from datetime import datetime



def ValidarRegistrar_Persona(cedula,nombre,edad,Veterinaria1):

    if not cedula.isdigit() or len(cedula) > 10:
        print("Error: La cédula debe ser numérica y tener un máximo de 10 caracteres.")
        return
    if not nombre.isalpha():
        print("Error: El nombre solo puede contener letras.")
        return
    if not edad.isdigit() or len(edad) > 3:
        print("Error: La edad debe ser numérica y tener un máximo de 3 caracteres.")
        return
    if len(cedula) == 0 or len(nombre) == 0 or len(edad) == 0:
        print("Error: Ningún campo puede estar vacío.")
        return
    
    business.registrar_Persona(cedula,nombre,edad,Veterinaria1)
    
def ValidarRegistrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,Veterinaria1):
    if not all([id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,Veterinaria1]):
        
        print("Todos los campos son obligatorios")
        return
    
    if not (cedula_dueno.isnumeric() and edad.isnumeric() and peso.endswith('kg')):
        print("Cedula del dueño, edad y peso deben ser numéricos y el peso debe terminar en 'kg'")
        return
    if len(edad) != 2:
        print("La edad debe tener dos dígitos")
    return

    return True

    business.registrar_mascota(id, nombre, cedula_dueno, edad, especie, raza, caracteristicas, peso,Veterinaria1)


def ValidarRegistrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento,Veterinaria1):
    if not id_mascota.isdigit():
        print("Error: El ID de la mascota debe ser un número.")
    elif not medico.isalpha():
        print("Error: El nombre del médico debe ser solo texto.")
    elif not motivo_consulta.isalpha():
        print("Error: El motivo de la consulta debe ser solo texto.")
    elif not sintomatologia.isalpha():
        print("Error: La sintomatología debe ser solo texto.")
    elif not diagnostico.isalpha():
        print("Error: El diagnóstico debe ser solo texto.")
    elif not procedimiento.isalpha():
        print("Error: El procedimiento debe ser solo texto.")
    elif not medicamento.isalpha():
        print("Error: El medicamento debe ser solo texto.")
    elif not dosis.isdigit():
        print("Error: La dosis debe ser un número.")
    elif not id_orden.isdigit():
        print("Error: El ID de la orden debe ser un número.")
    elif not historial_vacunacion.isalpha():
        print("Error: El historial de vacunación debe ser solo texto.")
    elif not alergias.isalpha():
        print("Error: Las alergias deben ser solo texto.")
   
    else:
        print("Todas las entradas son válidas.")
        
    business.registrar_historia_clinica(id_mascota, fecha, medico, motivo_consulta, sintomatologia, diagnostico, procedimiento, medicamento, dosis, id_orden, historial_vacunacion, alergias, detalle_procedimiento,Veterinaria1)

def ValidarBuscar_historia_clinica(id_mascota, fecha, Veterinaria1):
    if not id_mascota or not fecha:
                print("Error: Ningún campo debe estar vacío.")
    elif not id_mascota.isnumeric():
                print("Error: El campo id_mascota debe ser numérico.")
    else:
            try:
                datetime.strptime(fecha, '%Y-%m-%d %H:%M')
                business.buscar_historia_clinica(id_mascota, fecha, Veterinaria1)
            except ValueError:
                print("Error: La fecha debe tener el formato AAAA-MM-DD HH:MM.")


def ValidarCrear_orden(id_orden, idM, cedula_duenoM, cedula_vete, medicamentoO, dosis_enviada,estado,Veterinaria1):
    if not id_orden or not idM or not cedula_duenoM or not cedula_vete or not medicamentoO or not dosis_enviada:
        print("Error: Ningún campo debe estar vacío.")
    elif not id_orden.isnumeric() or not idM.isnumeric() or not cedula_duenoM.isnumeric() or not cedula_vete.isnumeric():
        print("Error: Los campos id_orden, idM, cedula_duenoM y cedula_vete deben ser numéricos.")
    elif medicamentoO.isnumeric() or dosis_enviada.isnumeric():
        print("Error: Los campos medicamentoO y dosis_enviada deben ser de texto.")
    else:
        business.crear_orden(id_orden, idM, cedula_duenoM, cedula_vete, medicamentoO, dosis_enviada,estado,Veterinaria1)
        
def ValidarBuscar_ordenID(id_orden, Veterinaria1):
    
    if not id_orden:
        print('El campo no puede estar vacío')
    elif not id_orden.isnumeric():
        print('Solo se permiten numeros')
    else:
        business.buscar_ordenID(id_orden, Veterinaria1)
        
def ValidarRegistrar_factura_venta(idFactura, id_orden, nombre_producto, precio, cantidad_llevar, Veterinaria1):
    if not idFactura or not id_orden or not nombre_producto or not precio or not cantidad_llevar:
        print("Error: Ningún campo debe estar vacío.")
        
    elif not idFactura.isdigit() or not id_orden.isdigit()  or not precio.isdigit()  or not cantidad_llevar.isdigit() :
        print("Error: Los campos idFactura, id_orden, precio, cantidad_llevar deben ser numéricos.")
        
    elif nombre_producto.isnumeric():
        print("Error: El campo nombre_medicamento debe ser de texto.")
    else:
        precio=float (precio)
        cantidad_llevar=int (cantidad_llevar)
        business.registrar_factura_venta(idFactura, id_orden, nombre_producto, precio, cantidad_llevar, Veterinaria1)
