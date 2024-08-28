datos = [
    {'nombre': 'Juan', 'edad': '15', 'nota': '8.5'},
    {'nombre': 'Ana', 'edad': '14', 'nota': '9.0'},
    {'nombre': 'Luis', 'edad': '16', 'nota': '7.5'},
    {'nombre': 'Marta', 'edad': '15', 'nota': '8.0'},
]

cabeceras = ['nombre', 'edad', 'nota']

print(f"{cabeceras[0]:<10} {cabeceras[1]:<5} {cabeceras[2]:<5}")

for fila in datos:
    print(f"{fila['nombre']:<10} {fila['edad']:<5} {fila['nota']:<5}")