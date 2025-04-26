def transform(data):
    print("Transformando datos.")

    #Rellenar precios faltantes
    data["precio"] = data["precio"].fillna(0)

    #Rellenar cantidades faltantes
    if "cantidad" not in data.columns:
        data["cantidad"] = 1

    data["cantidad"] = data["cantidad"].fillna(1)

    #Calcular total de la compra
    data["total_compra"] = data["precio"] * data["cantidad"]

    #Nivel de precio por unidad
    data["nivel_precio"] = data["precio"].apply(lambda x: "Compra alta" if x>= 1000 else "Compra baja")

    return data