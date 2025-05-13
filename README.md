# API Key di Python: Penjelasan & Tata Cara Penggunaan

API key adalah kode unik yang digunakan untuk mengautentikasi permintaan ke layanan API. Di Python, API key biasanya digunakan saat mengakses layanan eksternal seperti Google Maps, OpenWeather, atau layanan pihak ketiga lainnya.

## Cara Menggunakan API Key di Python

1. **Dapatkan API Key**
    - Daftar ke layanan yang ingin digunakan.
    - Ikuti instruksi untuk mendapatkan API key.

2. **Simpan API Key dengan Aman**
    - Jangan hardcode API key di dalam kode.
    - Gunakan file `.env` atau variabel lingkungan untuk menyimpan API key.

3. **Contoh Implementasi**

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Memuat variabel dari file .env

API_KEY = os.getenv("API_KEY")
url = f"https://api.example.com/data?api_key={API_KEY}"

response = requests.get(url)
data = response.json()
print(data)
```

4. **Tips Keamanan**
    - Jangan membagikan API key secara publik.
    - Gunakan file `.gitignore` untuk mengecualikan file yang berisi API key dari version control.

## UI Profesional untuk Input API Key

Jika Anda membuat aplikasi dengan antarmuka pengguna (UI), sediakan form input khusus untuk API key, misalnya:

```python
import tkinter as tk

def submit_key():
     api_key = entry.get()
     # Simpan atau gunakan API key sesuai kebutuhan

root = tk.Tk()
root.title("Masukkan API Key")

label = tk.Label(root, text="API Key:")
label.pack(padx=10, pady=5)

entry = tk.Entry(root, width=40, show="*")
entry.pack(padx=10, pady=5)

button = tk.Button(root, text="Submit", command=submit_key)
button.pack(padx=10, pady=10)

root.mainloop()
```

Dengan cara ini, pengguna dapat memasukkan API key secara aman dan profesional.
