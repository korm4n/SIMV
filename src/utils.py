from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def calculate_quantity_available(cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada):
    return cantidad_recibida - cantidad_usada - cantidad_devuelta - cantidad_desechada

def update_quantity_available(cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada, cantidad_disponible):
    if cantidad_disponible == 0 and (cantidad_usada > 0 or cantidad_devuelta > 0 or cantidad_desechada > 0):
        raise ValueError("No se puede restar de la cantidad disponible si es 0")
    return calculate_quantity_available(cantidad_recibida, cantidad_usada, cantidad_devuelta, cantidad_desechada)