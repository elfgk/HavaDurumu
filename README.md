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
Proje deposunu yerel makinenize klonlayın:

git clone <proje-linki>
cd <proje-dizini>
2. Gerekli Kütüphaneleri Yükleyin
Projenin çalışması için gerekli kütüphaneleri requirements.txt dosyasından yükleyin:

pip install -r requirements.txt
3. API Anahtarı Edinin
OpenWeather API platformundan bir API anahtarı alın.
Bu anahtar, hava durumu verilerini çekmek için gereklidir.
4. .env Dosyasını Oluşturun
Proje dizinine bir .env dosyası oluşturun ve aşağıdaki gibi API anahtarını ekleyin:

API_KEY=your_api_key_here
5. Uygulamayı Çalıştırın
Aşağıdaki komutu kullanarak uygulamayı başlatın:

python app.py
Tarayıcınızda uygulamaya erişmek için verilen bağlantıyı tıklayın. Örneğin:

Running on http://127.0.0.1:7860/
Artık şehir adını yazarak hava durumu bilgisine ulaşabilirsiniz!
