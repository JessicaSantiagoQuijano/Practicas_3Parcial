import pandas as pd

print("\n")
print("CARGAR EL CONJUNTO DE DATOS dirtydata.csv")
df = pd.read_csv("dirtydata.csv")
print(df.to_string())
print("\n")

print("MOSTRAR LOS PRIMEROS 5 REGISTROS")
print(df.head())
print("\n")

print("MOSTRAR LA INFORMACIÓN DEL CONJUNTO DE DATOS")
print(df.info)
print("\n")

print("CORREGIR EL FORMATO DE LA COLUMNA FECHA")
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
print("\n")

print("REMOVER CELDAD VACIAS O INCORRECTAS")
df.fillna(130, inplace=True)
print(df)
print("\n")
