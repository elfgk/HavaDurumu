Hava Durumu Uygulaması


Bu proje, kullanıcıların seçtikleri bir şehir için hava durumu bilgisini almasını sağlayan bir Python uygulamasıdır.
Uygulama, Gradio kütüphanesi ile bir arayüz sunar ve OpenWeather API'sini kullanarak gerçek zamanlı hava durumu verilerini sağlar.

Özellikler


Kullanıcıdan şehir adı alır.
OpenWeather API üzerinden hava durumu verilerini çeker.
Sıcaklık bilgisi Celsius cinsinden gösterilir.
Hava durumu açıklaması Türkçe olarak sunulur.
Kullanıcı dostu bir web arayüzüne sahiptir.


Kurulum
1. Depoyu Klonlayın
Proje deposunu yerel makinenize klonlayın

2. Gerekli Kütüphaneleri Yükleyin
Projenin çalışması için gerekli kütüphaneleri requirements.txt dosyasından yükleyin:

pip install -r requirements.txt

3. API Anahtarı Edinin
OpenWeather API platformundan bir API anahtarı alın.

4. .env Dosyasını Oluşturun
Proje dizinine bir .env dosyası oluşturun ve aşağıdaki gibi API anahtarını ekleyin:

API_KEY=your_api_key_here



5. Uygulamayı Çalıştırın
Aşağıdaki komutu kullanarak uygulamayı başlatın:

python app.py


Artık şehir adını yazarak hava durumu bilgisine ulaşabilirsiniz!
