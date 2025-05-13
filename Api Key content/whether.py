import requests
import json
import datetime
import folium

API_KEY ='2686cbd9ceb0896ba3999b20e8a4406d'
CITY = (input('Masukkan nama kota: '))
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
response = requests.get(URL)
data = response.json()
if response.status_code == 200 :
    try:
        print(f"Cuaca di wilayah : {CITY}")
        print(f"Temperatur: {data['main']['temp']}°C")
        print(f"Deskripsi: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"speed: {data['wind']['speed']} m/s")
        print(f"clouds: {data['clouds']['all']}%")
        if 'rain' in data:
            print(f"rain: {data['rain']['3h', 0]} mm")
        else:
            print(f"rain: Tidak Hujan")
        print(f"sunrise: {data['sys']['sunrise']}")
        print(f"sunset: {data['sys']['sunset']}")
        print(f"country: {data['sys']['country']}")
        if 'timezone' in data['sys']:
            print(f"timezone: {data['sys']['timezone']}")
        else:
            print(f"timezone: Tidak Ditemukan")
        if 'id' in data['sys']:
            print(f"id: {data['sys']['id']}")
        else:
            print(f"id : Tidak Ditemukan")
        print(f"name: {data['name']}")
        print(f"dt: {data['dt']}")
        print(f"cod: {data['cod']}")
        print(f'lat: {data["coord"]["lat"]}')
        print(f'lon: {data["coord"]["lon"]}')
        if 'weather' in data:
            print(f'Weather: {data["weather"][0]["description"]}')
        else:
            print(f'Weather: Tidak Ditemukan')
        if 'clear' in data['weather'][0]['description'].lower():
            print("Pesan: Cuaca terangkai, bersiaplah untuk cuaca dingin.")
            
        datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Waktu: {datetime.datetime.now().strftime('%H:%M:%S')}")
        print(f"Temperatur: {data['main']['temp']}°C")
        print(f"Deskripsi: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"speed: {data['wind']['speed']} m/s")
        print(f"clouds: {data['clouds']['all']}%")
        if 'rain' in data:
            print(f"rain: {data['rain']['3h', 0]} mm")
        else:
            print(f"rain: Tidak Hujan")
        if 'snow' in data:
            print(f"snow: {data['snow']['3h', 0]} mm")
        else:
            print(f"snow: Tidak Salju")
        lat = data['coord']['lat']
        lon = data['coord']['lon']
        cuaca = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup=data['weather'][0]['description']).add_to(cuaca)
        folium.Marker([lat, lon], popup=f"Temperatur: {data['main']['temp']}°C").add_to(cuaca)
        folium.Marker([lat, lon], popup=f"Humidity: {data['main']['humidity']}%").add_to(cuaca)
        folium.Marker([lat, lon], popup=f"speed: {data['wind']['speed']} m/s").add_to(cuaca)
        folium.Marker([lat, lon], popup=f"clouds: {data['clouds']['all']}%").add_to(cuaca)
        if 'rain' in data:
            folium.Marker([lat, lon], popup=f"rain: {data['rain']['3h', 0]} mm").add_to(cuaca)
        else:
            print("Tidak Ada Hujan")
        folium.Marker([lat, lon], popup=f"sunrise: {data['sys']['sunrise']}").add_to(cuaca)
        folium.Marker([lat, lon], popup=f"sunset: {data['sys']['sunset']}").add_to(cuaca)
        folium.Marker([lat, lon], popup=f"country: {data['sys']['country']}").add_to(cuaca)
        cuaca.save(f"{CITY}.html")
        print(f"Gambar telah disimpan di {CITY}.html")
    except ValueError:
        print (f'Terjadi kesalahan pada data Json')
else :
    print (f'Error: {response.status_code}, {response.text}')
    print ('pesan : ', response.text)