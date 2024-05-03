import matplotlib.pyplot as plt
from ejercicio_pandas import df_ventas_mensuales

def graficos(df_ventas_mensuales):

    #Crear un gráfico de lineas asignando los meses al eje x y el total de ventas de cada mes al eje y
    plt.plot(df_ventas_mensuales["mes"], df_ventas_mensuales["total_ventas"], color="green")

    #Definir el título de la gráfica
    plt.title('Tendencia de ventas a lo largo de los meses')
    #Definir el nombre del eje x
    plt.xlabel('Meses')
    #Definir el nombre del eje y
    plt.ylabel('Total de ventas')
    #Poner grid en la gráfica
    plt.grid(True)
    plt.xticks(rotation=50)
    #Mostrar la gráfica 
    plt.show()
    
graficos(df_ventas_mensuales)