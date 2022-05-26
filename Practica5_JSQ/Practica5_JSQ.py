import api_key
import requests
import pandas as pd
from IPython.core.display import HTML

your_client_access_token = api_key.client_access_token
print(your_client_access_token)
print("\n")

print("HACER UNA SOLICITUD DE API")
print("vamos a asignar la cadena Missy Elliott a la variable search_term. Luego, vamos a crear una URL\n"
      "de cadena f que contenga las variables search_termy client_access_token")


search_term = "Missy Elliott"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={your_client_access_token}"
print(genius_search_url)
print("\n")

print("En lugar de obtener el .textde la respuesta, como hicimos antes, vamos a usar .json().")
print("JSON es un formato de datos que las API suelen utilizar. Los datos JSON se pueden anidar y contienen pares\n"
      "clave/valor, como un diccionario de Python.")

response = requests.get(genius_search_url)
json_data = response.json()

print("Los datos JSON que obtenemos de nuestra consulta de la API de Missy Elliott se ven así:")
print(json_data)
print("\n")

print("Podemos indexar estos datos (nuevamente, como un diccionario de Python) y mirar el primer\n acierto sobre Missy Elliott de Genius.com .")

json_data["response"]["hits"][0]
print(json_data)
print("\n")

print("BUCLES A TRAVÉS DE DATOS JSON")
print("OBTNER TITULOS DE CANCIONES")
for song in json_data["response"]["hits"]:
    print(song["result"]["full_title"])
print("\n")

print("OBTENER MOSAICOS DE CANCIONES Y RENCUENTOS DE PAGINAS VISITADAS")
for song in json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats']['pageviews'])
print("\n")

print("TRANSFORME LOS TITULOS DE LAS CANCIONES Y LOS RECUENTOS DE PAGINAS VISTAS EN UN MARCO DE DATOS")
print("Podemos recorrer estos datos, agregarlos a una lista y luego transformar esa lista en un marco de datos de Pandas llamandopd.DataFrame()")
missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append([song['result']['full_title'], song['result']['stats']['pageviews']])

# Make a Pandas dataframe from a list
missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views']
print(missy_df)
print("\n")

print("TRANFORME TITULOS DE CANCIONES, RECUENTOS DE PÁGINAS VISTAS Y PORTADAS DE ÁLBUMES EN UN MARCO DE DATOS")
print("podemos hacer lo mismo pero también agregar enlaces a imágenes de la carátula del álbum de Missy Elliott,\n"
      "¡y también podemos mostrar esas imágenes!")

print("Para mostrar imágenes en un marco de datos de Pandas, debe ejecutar y realizar la función . Vamos a tomar\n"
      "las URL de las imágenes y convertirlas en objetos HTML.from IPython.core.display import HTMLget_image_html()")
def get_image_html(link):
    image_html = f"<img src='{link}' width='500px'>"
    return image_html


missy_songs = []
for song in json_data['response']['hits']:
    missy_songs.append(
        [song['result']['full_title'], song['result']['stats']['pageviews'], song['result']['song_art_image_url']])

missy_df = pd.DataFrame(missy_songs)
missy_df.columns = ['song_title', 'page_views', 'album_cover_url']

    # Use the function get_image_html()
missy_df['album_cover'] = missy_df['album_cover_url'].apply(get_image_html)
datos_HTML = missy_df[['album_cover', 'page_views', 'song_title']].to_html()
print(datos_HTML)
print(missy_df)
print("\n\n\n")

# PRACTICA PROPIA

search_term_ = "Juanes"
genius_search_url_ = f"http://api.genius.com/search?q={search_term_}&access_token={your_client_access_token}"
response_ = requests.get(genius_search_url_)
json_data_ = response_.json()

songs_ = []
for song in json_data_['response']['hits']:
    songs_.append((song['result']['full_title'], song['result']['stats']['pageviews'],
                  song['result']['song_art_image_url']))

artist_df = pd.DataFrame(songs_)
artist_df.columns = ['song_title', 'page_views', 'album_cover_url']
artist_df['album_cover'] = artist_df['album_cover_url'].apply(get_image_html)
datosMe_HTML = artist_df[['album_cover', 'page_views', 'song_title']].to_html()
print(datosMe_HTML)
print(artist_df)



