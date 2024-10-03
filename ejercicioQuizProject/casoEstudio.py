#entradas
nombre = input('Ingrese el nombre del empleado: ')
diasLaborados = int(input('Ingrese el número de días laborados: '))
salario = int(input('Ingrese su salario: '))

#procesos
def calcularLiquidacion(salario, diasLaborados):

    #calcular prima
    prima = salario * diasLaborados / 360

    #calular sesantias
    cesantias = salario * diasLaborados / 360

    # Calcular intereses a las cesantías
    interesesCesantias = cesantias * 0.12 / diasLaborados

    # Calcular vacaciones
    vacaciones = salario * diasLaborados / 720

    # Retornar los resultados
    return prima, cesantias, interesesCesantias, vacaciones

# Calcular la liquidación
prima, cesantias, interesesCesantias, vacaciones = calcularLiquidacion(salario, diasLaborados)

# Mostrar los resultados
print('-------------------------------------------------------------------------------')
print('RESULTADOS')
print(f'''Señor {nombre} para los {diasLaborados} dias laborados
y salario ${salario:.2f}, su liquidación se compone así:
Prima: ${prima:.2f}
Cesantia: ${cesantias:.2f}
Intereses Cesantias: ${interesesCesantias:.2f}
Vacaciones: ${vacaciones:.2f}
Liquidacion: ${prima + cesantias + interesesCesantias + vacaciones:.2f}''')