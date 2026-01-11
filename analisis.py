# 1. Cargar datos del CSV
# 2. Calcular ventas totales por mes
# 3. Determinar producto más vendido y con mayor ingresos
# 4. Graficar ventas por mes
# 5. Graficar top 5 productos por ingresos

import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_sinteticas.csv')

df['fecha'] = pd.to_datetime(df['fecha'])

df['mes'] = df['fecha'].dt.to_period('M')

ventas_por_mes = df.groupby('mes').apply(lambda d: (d['cantidad'] * d['precio']).sum())

ventas_por_mes = ventas_por_mes.sort_index()

print("Ventas por mes:")

print(ventas_por_mes)

#df.info()

df['ingreso'] = df['cantidad'] * df['precio']

ventas_prod = df.groupby('producto').agg({

    'cantidad': 'sum',

    'ingreso': 'sum'
})

mas_vendido = ventas_prod['cantidad'].idxmax()

mayor_ingreso = ventas_prod['ingreso'].idxmax()

#Aquí .idxmax() da el índice (producto) del máximo valor. 
# Imprimimos también los valores. Revisa que tenga sentido 
# (por ejemplo, un producto barato pudo tener más unidades pero menos dinero).

print(f"Producto más vendido en unidades: {mas_vendido} (total {ventas_prod.loc[mas_vendido, 'cantidad']})")

print(f"Producto con mayores ingresos: {mayor_ingreso} (total {ventas_prod.loc[mayor_ingreso, 'ingreso']:.2f} €)")

# Si ventas_por_mes es index Period, convertir a str para mejor manejo
ventas_por_mes.index = ventas_por_mes.index.astype(str)

plt.figure(figsize=(6,4))

ventas_por_mes.plot(kind='bar')

plt.title("Ventas por Mes")

plt.xlabel("Mes")

plt.ylabel("Ventas (€)")
plt.tight_layout()

plt.savefig("ventas_por_mes.png")

plt.show()


top5 = ventas_prod.nlargest(5, 'ingreso')

plt.figure(figsize=(6,4)) # Crear figura

plt.bar(top5.index, top5['ingreso']) # Gráfica de barras

plt.title("Top 5 Productos por Ingresos") # Título de la gráfica

plt.ylabel("Ingresos (€)") # Etiqueta del eje Y

plt.xlabel("Producto") # Etiqueta del eje X

plt.xticks(rotation=45) # Rotar etiquetas del eje X

plt.tight_layout() # Ajuste de diseño

plt.savefig("top5_productos.png") # Guardar la figura

plt.show() # Mostrar la figura
