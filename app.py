import requests
import gradio as gr
from dotenv import load_dotenv
import os
load_dotenv()

api_anahtari= os.getenv("api_anahtari")

# İngilizce açıklamaları Türkçe'ye çevirme
ceviri = {
    "clear sky": "açık hava",
    "few clouds": "az bulutlu",
    "scattered clouds": "dağınık bulutlar",
    "broken clouds": "parçalı bulutlu",
    "shower rain": "sağanak yağmur",
    "rain": "yağmur",
    "thunderstorm": "gök gürültülü fırtına",
    "snow": "kar",
    "mist": "sis",
    "overcast clouds": "bulutlu"
}


def hava_durumu(sehir):
    api_anahtari = "1ed5a18117b88f4879ea14c1ffa44858"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}'
    response = requests.get(url)

    if response.status_code == 200:
        veri = response.json()
        temp = veri['main']["temp"]
        aciklama_ing = veri['weather'][0]['description']
        temp_c = temp - 273.15
        # Açıklamayı Türkçe'ye çevirme
        aciklama_tr = ceviri.get(aciklama_ing, aciklama_ing)  # Eğer çeviri bulunamazsa orijinalini kullan

        return f"Sıcaklık: {temp_c:.2f} °C \n Durum: {aciklama_tr}"
    else:
        return f"Hava Durumu verileri alınırken hata oluştu.\n Hata Kodu: {response.status_code}"

# Gradio arayüzü
arayuz = gr.Interface(
    fn=hava_durumu,
    inputs=["text"],
    outputs=["text"],
    title="Hava Durumu Uygulaması",
    description="Şehrinizi girin ve hava durumu bilgisini alın."
)

arayuz.launch(share=True)
