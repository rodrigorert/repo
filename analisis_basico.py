#crear una tabla de datos de fecha y temperatura de un año
#la fecha se genera aleatoriamente y la temperatura se genera aleatoriamente entre -10 y 40
#la tabla se debe guardar en un archivo csv



"Version inicial"

import random
import csv
import datetime
import statistics
import matplotlib.pyplot as plt  # type: ignore
import matplotlib.dates as mdates  # type: ignore

def generar_temperatura():
    return random.randint(20, 35)

def generar_tabla():
    # Fecha inicial: 1 de enero de 2026
    fecha_inicial = datetime.datetime(2026, 1, 1)
    
    with open("tabla_temperatura.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Fecha", "Temperatura"])
        for i in range(365):
            # Generar fecha sumando i días a la fecha inicial
            fecha = fecha_inicial + datetime.timedelta(days=i)
            fecha_str = fecha.strftime("%Y-%m-%d")
            temperatura = generar_temperatura()
            writer.writerow([fecha_str, temperatura])

generar_tabla()

def analizar_tabla():
    with open("tabla_temperatura.csv", "r") as f:
        reader = csv.reader(f)
        # Saltar la primera fila (encabezado)
        next(reader, None)
        for row in reader:
            # Validar que la fila tenga al menos 2 elementos
            if len(row) >= 2:
                fecha = row[0]
                temperatura = row[1]
                print(f"Fecha: {fecha}, Temperatura: {temperatura}")



#Calcula estadísticas simples: media, mediana, desviación estándar
def calcular_estadisticas():
    temperaturas = []
    with open("tabla_temperatura.csv", "r") as f:
        reader = csv.reader(f)
        # Saltar la primera fila (encabezado)
        next(reader, None)
        for row in reader:
            if len(row) >= 2:
                temperatura = float(row[1])
                temperaturas.append(temperatura)
    
    if not temperaturas:
        return None, None, None
    
    media = statistics.mean(temperaturas)
    mediana = statistics.median(temperaturas)
    desviacion = statistics.stdev(temperaturas)
    return media, mediana, desviacion


media, mediana, desviacion = calcular_estadisticas()
print(f"Media: {media:.2f}, Mediana: {mediana:.2f}, Desviacion: {desviacion:.2f}")

#Genera una gráfica de dispersión de una columna vs. la otra
def graficar_dispersio():
    fechas = []
    temperaturas = []
    
    with open("tabla_temperatura.csv", "r") as f:
        reader = csv.reader(f)
        # Saltar la primera fila (encabezado)
        next(reader, None)
        for row in reader:
            if len(row) >= 2:
                fecha_str = row[0]
                temperatura = float(row[1])
                # Convertir string de fecha a objeto datetime
                fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
                fechas.append(fecha)
                temperaturas.append(temperatura)
    
    # Crear el scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(fechas, temperaturas, alpha=0.6, s=20)
    plt.xlabel("Fecha")
    plt.ylabel("Temperatura (°C)")
    plt.title("Gráfica de Dispersión: Temperatura vs Fecha (2026)")
    plt.grid(True, alpha=0.3)
    
    # Formatear el eje X para mostrar fechas correctamente
    plt.gcf().autofmt_xdate()
    date_format = mdates.DateFormatter("%Y-%m-%d")
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    
    plt.tight_layout()
    plt.show()

graficar_dispersio() 

