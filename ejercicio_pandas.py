import pandas as pd

ventas_mensuales = [
    {"mes": "Enero", "total_ventas": 15000, "año": 2023},
    {"mes": "Febrero", "total_ventas": 18000, "año": 2023},
    {"mes": "Marzo", "total_ventas": 22000, "año": 2023},
    {"mes": "Abril", "total_ventas": 19000, "año": 2023},
    {"mes": "Mayo", "total_ventas": 25000, "año": 2023},
    {"mes": "Junio", "total_ventas": 28000, "año": 2023},
    {"mes": "Julio", "total_ventas": 32000, "año": 2023},
    {"mes": "Agosto", "total_ventas": 30000, "año": 2023},
    {"mes": "Septiembre", "total_ventas": 28000, "año": 2023},
    {"mes": "Octubre", "total_ventas": 31000, "año": 2023},
    {"mes": "Noviembre", "total_ventas": 33000, "año": 2023},
    {"mes": "Diciembre", "total_ventas": 36000, "año": 2023},
    {"mes": "Enero 2", "total_ventas": 37000, "año": 2024},
    {"mes": "Febrero 2", "total_ventas": 38000, "año": 2024},
    {"mes": "Marzo 2", "total_ventas": 42000, "año": 2024},
    {"mes": "Abril 2", "total_ventas": 39000, "año": 2024},
    {"mes": "Mayo 2", "total_ventas": 45000, "año": 2024},
    {"mes": "Junio 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Julio 2", "total_ventas": 52000, "año": 2024},
    {"mes": "Agosto 2", "total_ventas": 50000, "año": 2024},
    {"mes": "Septiembre 2", "total_ventas": 48000, "año": 2024},
    {"mes": "Octubre 2", "total_ventas": 51000, "año": 2024},
    {"mes": "Noviembre 2", "total_ventas": 55000, "año": 2024},
    {"mes": "Diciembre 2", "total_ventas": 58000, "año": 2024},
]

try:
    # Convertir la lista en un DataFrame
    df_ventas = pd.DataFrame(ventas_mensuales)

    # Mapear los nombres de los meses a los números de trimestre
    meses_a_trimestres = {
        "Enero": 1, "Febrero": 1, "Marzo": 1,
        "Abril": 2, "Mayo": 2, "Junio": 2,
        "Julio": 3, "Agosto": 3, "Septiembre": 3,
        "Octubre": 4, "Noviembre": 4, "Diciembre": 4
    }

    # Agregar la columna trimestre
    df_ventas["trimestre"] = df_ventas["mes"].map(meses_a_trimestres)

    # Agrupar los datos por trimestre y calcular el total de ventas para cada trimestre
    ventas_trimestrales = df_ventas.groupby("trimestre")["total_ventas"].sum()
    print("Ventas trimestrales:")
    print(ventas_trimestrales)

    # Filtrar los meses donde las ventas superan 20000 y mostrarlos
    meses_altas_ventas = df_ventas[df_ventas["total_ventas"] > 20000]["mes"]
    print("\nMeses con ventas superiores a 20000:")
    print(meses_altas_ventas)

    # Encontrar el mes con el mayor volumen de ventas y mostrarlo
    mes_max_ventas = df_ventas[df_ventas["total_ventas"] == df_ventas["total_ventas"].max()]
    print("\nMes con el mayor volumen de ventas:")
    print(mes_max_ventas)

    # Calcular el promedio de ventas mensuales y mostrarlo
    promedio_ventas_mensuales = df_ventas["total_ventas"].mean()
    print("\nPromedio de ventas mensuales:", promedio_ventas_mensuales)

    # Crear un DataFrame que incluya dos columnas una para los meses y otra para el total de ventas de cada mes.
    df_ventas_mensuales = df_ventas[["mes", "total_ventas"]]
    print("\nDataFrame de ventas mensuales:")
    print(df_ventas_mensuales)
    
except Exception as e:
    print("Ocurrió un error:", e)
