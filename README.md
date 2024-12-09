Hava Durumu Uygulaması

Bu proje, kullanıcıların seçtikleri bir şehir için hava durumu bilgisini almasını sağlayan bir Python uygulamasıdır. Uygulama, Gradio kütüphanesi ile bir arayüz sunar ve OpenWeather API'sini kullanarak gerçek zamanlı hava durumu verilerini alır.

##Özellikler
Kullanıcıdan şehir adı alır.
OpenWeather API üzerinden hava durumu verilerini çeker.
Sıcaklık bilgisi Celsius cinsinden gösterilir.
Hava durumu açıklaması Türkçe olarak sunulur.
Kullanıcı dostu bir web arayüzüne sahiptir.

#Kurulum
1-Depoyu Klonlayın
2-Gerekli Kütüphaneleri Yükleyin 
requirements.txt dosyasındaki bağımlılıkları yüklemek için:

pip install -r requirements.txt

3-API Anahtarı
OpenWeather API’den bir API anahtarı edinin

4-Proje dizinine bir .env dosyası oluşturun ve aşağıdaki gibi API anahtarını ekleyin:

API_KEY=your_api_key_here

5-Uygulamayı Çalıştırın Aşağıdaki komutla uygulamayı başlatın:

python app.py

