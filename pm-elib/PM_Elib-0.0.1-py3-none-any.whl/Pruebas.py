from Funciones import process_file as pf

fn="pm.csv"
days=0
hours="00:35:00"
cost=150000

res = pf(fn,days,hours,cost)

print("Generalidades")
print(res[0]["Generalidades"])
print("\nMarcacion inicial")
print(res[0]["Marcacion inicial"])
print("\nPlaces")
print(res[0]["Places"])
print("\nTransitions")
print(res[0]["Transitions"])
print("\nFiltrado secuencias")
print(res[0]["Filtrado secuencias"])
print("\nId_x_Variant")
print(res[0]["Id_x_Variant"])
print("\nD-")
print(res[0]["D-"])
print("\nD+")
print(res[0]["D+"])
print("\nD")
print(res[0]["D"])
print("\nAction_x_Resource")
print(res[0]["Action_x_Resource"])
print("\nMarcacion")
print(res[0]["Marcacion"])
print("\nCuello de botella")
print(res[0]["Cuello de botella"])
print("\nConsejos_0")
print(res[0]["Consejos_0"])
print("\nConsejos_1")
print(res[0]["Consejos_1"])
print("\nMejor Variante")
print(res[0]["Mejor Variante"])
print("\nTiempo Mejor Variante Sin Tiempos Muertos")
print(res[0]["Tiempo Mejor Variante Sin Tiempos Muertos"])
print("\nCosto Mejor Variante")
print(res[0]["Costo Mejor Variante"])