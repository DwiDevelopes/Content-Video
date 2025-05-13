import requests
import json

api_key = 'cufTmpycJCxw3ND5oeBKMrhv'
url = 'https://api.remove.bg/v1.0/removebg'
images_path = 'bb.jpg'
files = {'image_file': open(images_path, 'rb')}
response = requests.post(url, files=files, data={'size': 'auto'}, headers={'X-Api-Key': api_key})
if response.status_code == 200 :
    with open('output_image 3.png', 'wb') as open_file:
        open_file.write(response.content)
    print ('gambar berhasil terhapus remove bacground')
else: 
    print ('Peingatan Error : ', response.status_code, response.text)