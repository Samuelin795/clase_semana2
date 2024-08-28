from tabulate import tabulate

cabeceras = ['nombre', 'edad', 'nota']
datos = [
        
        ['Juan', '15', '8.0'],
        ['Ana', '15', '9.0'],
        ['Luis', '16', '7.5'],
        ['Marta', '18', '7.0']
]

print(tabulate(datos, headers=cabeceras, tablefmt='grid'))
