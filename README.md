# Çok sahneli hikâye üretimi denemesi

Metin üretimi, görsel açıklama ve görsel üretim modellerini aynı akışta birleştirmeyi denediğim Colab notebook'u. Konudan sekiz sahnelik hikâye oluşturuyor; her sahne için bir görsel üretip sonucu HTML olarak dışarı veriyor.

## Akış

1. İsteğe bağlı giriş görseli BLIP-2 ile açıklanıyor.
2. GPT-4o-mini hikâyeyi ve sahne açıklamalarını JSON olarak üretiyor.
3. DreamShaper-8 ile sahne görselleri oluşturuluyor.
4. Gradio arayüzü sonucu gösteriyor ve HTML dosyası sunuyor.

Burada hazır modelleri birleştiren bir prototip üzerinde çalıştım; yeni bir temel model eğitmedim. Karakter açıklamasını sahneler arasında tekrar kullanmak görsel tutarlılığı amaçlıyor, aynı karakter görünümünü garanti etmiyor.

## Çalıştırma

[Multimodal_Story_Generator.ipynb](Multimodal_Story_Generator.ipynb) dosyasını Google Colab'da açıp GPU çalışma ortamını seç. Notebook içindeki kurulum, yapılandırma, model yükleme ve arayüz hücrelerini sırayla çalıştır. Model indirmeleri ve görsel üretimi için yeterli GPU belleği gerekir.

OpenAI anahtarı `getpass` ile çalışma anında alınır; notebook'a kaydetme. API kullanımı hesaba göre ücretli olabilir. Son hücre Gradio paylaşım bağlantısı açar; çalışma ortamı kapanınca bu bağlantı kalıcı demo olarak kullanılamaz.

[test_api.py](test_api.py) yalnız API bağlantısını sınar; hikâye kalitesi veya GPU çalışmasını test etmez. `demo_output.jpg` önceki denemeden bir örnektir. Notebook çıktıları ve çalışma kimlikleri repoda tutulmaz.
