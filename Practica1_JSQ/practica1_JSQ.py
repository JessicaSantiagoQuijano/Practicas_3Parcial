import pandas as pd
import matplotlib.pyplot as plt
surveys_df  = pd.read_csv("surveys.csv")
print(surveys_df)

print("El método head() muestra las primeras líneas de un archivo.")
print("Eso se analiza a continuación.")
print(surveys_df.head())

print("EXPLORANDO LOS DATOS DEL CENSO DE ESPECIES")
print(type(surveys_df))

print("Qué tipo de cosas surveys_df contiene? Los DataFrame tienen un atributo llamado dtypes que contesta esta pregunta:?}\nsurveys_df.dtypes")
print(surveys_df.dtypes)
print("\n")

print("FORMAS UTILES DE VER OBJETOS DataFrame en Python")

print("1. Accesar a un atributo, surveys_df.columns")
print(surveys_df.columns)
print("\n")

print("2. Metodos que son llamados de la misma manera, surveys_df.shape")
print(surveys_df.shape)
print("\n")

print("3. Mostrar los elementos primeros 5 elementos de la base de datos")
print(surveys_df.head())
print(surveys_df.head(15))
print("¿qué hace esto?")
print("Con print(surveys_df.head()) muestra los primeros 5 elementos de la base de datos y con print(surveys_df.head(15)) \nmuestra los primeros 15 elementos de la base de datos")

print("\n")
print("4.Imprimir los ultimos elementos con surveys_df.tail()")
print(surveys_df.tail())

print("\n")
print("CALCULAR ESTADÍTICAS DE LOS DATOS EN UN DataFrame de Pandas")
print("Echemos un vistazo a las columnas")
print(surveys_df.columns)
print("\n")

print("Obtengamos una lista de todas las especies. La función pd.unique nos dice los distintos\nvalores presentes en la columnaspecies_id.")
print("\n")
print(pd.unique(surveys_df['species_id']))
print("\n")

print("GRUPO EN PANDAS")
print("Podemos calcular algunas estadísticas básica de todos los datos en una columna usando el siguiente comando:\nsurveys_df['weight'].describe()")
print(surveys_df['weight'].describe())
print("\n")

print("También podemos extraer una métrica en particular::")
print(surveys_df['weight'].min())
print(surveys_df['weight'].max())
print(surveys_df['weight'].mean())
print(surveys_df['weight'].std())
print(surveys_df['weight'].count())

print("si nosotros queremos extraer información por una o más variables, por ejemplo sexo, podemos usar el \nmétodo .groupby de Pandas. Una vez que creamos un DataFrame groupby, podemos calcular estadísticas por el grupo de nuestra elección.")
# Datos agrupados por sexo
grouped_data = surveys_df.groupby('sex')
print(grouped_data)
print("\n")

print("La función describe de Pandas regresa estadísticas descriptivas incluyendo: media, meadiana, máx, mín, std y conteos para una columna en particular de los datos. \nLa función describe solo regresa los valores de estas estadísticas para las columnas numéricas.")
# Estadísticas para todas las columnas numéricas por sexo
print(grouped_data.describe())
# Regresa la media de cada columna numérica por sexo
print(grouped_data.mean())
print("\n")

print("CREANDO ESTADÍSTICAS DE CONTEOS RAPIDAMENTE CON PANDAS")
print("Ahora contemos el número de muestras de cada especie. Podemos hacer esto de dsitintas maneras, \npero usaremos groupby combinada con el método count().")
# Cuenta el número de muestras por especie
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)
print("\n")

print("también podemos contar las líneas que tienen la especie “DO”:")
print(surveys_df.groupby('species_id')['record_id'].count()['DO'])
print("\n")

print("FUNCIONES BÁSICAS DE MATEMÁTICAS")
print("se puede hacer operaciones en una columna de los datos. Como ejemplo multipliquemos todos los valores de peso por 2. ")
# Multiplicar todos los valores de peso por 2
d = surveys_df['weight']*2
print(d)
print("\n")

print("GRAFICAR RÁPIDA Y FÁCILMENTE LOS DATOS USANDO PANDAS")
# Creaemos una gráfica de barras
print("Conteos de especie por sitio")
species_counts.plot(kind='bar');
plt.show()

print("También podemos ver cuantos animales fueron capturados por sitio:")
total_count = surveys_df.groupby('plot_id')['record_id'].nunique()
# También grafiquemos eso
total_count.plot(kind='bar')
plt.show()
print("\n")

print("RETO DE GRÁFICAS")
print("1. Crea una gráfica del promedio de peso de las especies por sitio.")
total_count = surveys_df.groupby('weight')['record_id'].nunique()
total_count.mean()
# También grafiquemos eso
total_count.plot(kind='bar');
plt.show()

print("2. Crea una gráfica del total de machos contra el total de hembras para todo el conjunto de datos.")

total_count = surveys_df.groupby('sex')['record_id'].nunique()
# También grafiquemos eso
total_count.plot(kind='bar');
plt.show()

print("GRAFICACIÓN FINAL")
print("Puedes usar el siguiente código para crear una gráficad de barras apiladas pero los datos para apilar deben de estar en distintas columnas. \nAquí hay un pequeño ejemplo con algunos datos donde ‘a’, ‘b’ y ‘c’ son los grupos, y ‘one’ y ‘two’ son los subgrupos.")
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(d))
print("\n")

print("Graficar datos apilados de modo que las columnas 'one' y 'two' estén apiladas")
my_df = pd.DataFrame(d)
my_df.plot(kind='bar',stacked=True,title="The title of my graph")
plt.show()

print("Crea una gráfica de barras apiladas con el peso en el eje Y, y la variable de apilamiento que sea el sexo. \nLa gráfica debe mostrar el peso total por sexo para cada sitio.")
print("Primero agrupemos los datos por sitio y por sexo y después calculemos el total para cada sitio.")
by_site_sex = surveys_df.groupby(['plot_id','sex'])
site_sex_count = by_site_sex['weight'].sum()
print(site_sex_count)
print("Esto calcula la suma de los pesos para cada sexo por sitio como una tabla")
print("\n")

print("Ahora usaremos .unstack() en los datos agrupados para entender como el peso total de cada sexo contribuye a cada sitio.")
by_site_sex = surveys_df.groupby(['plot_id','sex'])
site_sex_count = by_site_sex['weight'].sum()
site_sex_count.unstack()
print(site_sex_count)
print("\n")

print("Ahora creamos una gráfica de barras apilada con los datos donde el peso para cada sexo es apilado por sitio.")
print("En vez de mostrarla como tabla, nosotros podemos graficar los datos apilando los datos de cada sexo como sigue:")
by_site_sex = surveys_df.groupby(['plot_id','sex'])
site_sex_count = by_site_sex['weight'].sum()
spc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar',stacked=True,title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Plot")
plt.show()



