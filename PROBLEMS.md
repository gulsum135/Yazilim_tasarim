
KENDİ CEVABIM:

1)Tek Sorumluluk Prensibine göre uyumsuzdur. Tek bir sınfta hem tutar hesabı yapılıyor hem de indirim türünü belirliyor.

2) Açık/Kapalı prensibi: Kod şuan değişime kapalı değil yeni bir indirim türü eklendiğinde veya yeni özellik eklemek istenildiğinde kod yapısını değiştirmek gerekiyor her özellik için elif veya else vs. eklemek gerekir. Bu da hatalara yol açabilir.

3)Dependency Prensibi: Bu kodda indirim türünde metin girdisi bağımlılık yaratıyor.Alt seviyede olan İndirim_turu, üst seviyedeki AlisverisSepeti sınıfını bağımlı hale getiriyor.

AI CEVABI:

1) Tek Sorumluluk Prensibi İhlali (SRP)
AlisverisSepeti sınıfı hem sepeti temsil ediyor hem de indirim hesaplıyor. İki ayrı sorumluluğun tek sınıfta olması, birbirinden bağımsız değişimleri birbirine bağlıyor.


2) Açık/Kapalı Prensibi İhlali (OCP)
Yeni bir indirim türü eklemek için mevcut sınıfı değiştirmek gerekiyor. Her değişimde çalışan kodu bozma riski doğuyor.


 3) Magic String Kullanımı
"EFSANE_KASIM", "ÖĞRENCİ" gibi ham string'ler tip güvensizdir. Yazım hatası sessizce else dalına düşer, IDE otomatik tamamlama sunmaz.



4) Birden Fazla İndirim Uygulanamıyor
Yapı yalnızca tek indirim destekliyor. "Öğrenci + Hoş Geldin Kuponu" gibi kombine senaryolar mümkün değil.


5) Negatif Tutar Koruması Yok
HOŞ_GELDİN_KUPONU dalında tutar 50 TL'nin altındaysa negatif sonuç üretiliyor. Hiçbir sınır kontrolü yok.


KARŞILAŞTIRMA BÖLÜMÜ:

Ben sistemin nesne yönelimli tasarım ve SOLID prensiplerine (SRP, OCP, DIP) olan uyumsuzluklarına ve teorik altyapısına odaklandım. AI ise mimari prensiplerin yanı sıra kodun iş mantığı ve çalışma zamanı hatalarına odaklandı.


Aralarındaki Farklar ve Çıkarımlar:

- Mimaride Ortak Noktalar:Hem ben hem de AI, kodun SRP ve OCP prensiplerini ağır şekilde ihlal ettiği konusunda tamamen hemfikiriz.
- Benim Farkım (DIP):AI doğrudan DIP ihlaline değinmezken, ben alt seviye metin girdilerinin üst seviye sınıfa bağımlılık yarattığını doğru bir şekilde analiz ettim.
-AI'ın Farkı (Yazılımsal Açıklar):AI benden farklı olarak kodun çalışırken üretebileceği mantıksal hataları (50 TL altı alışverişte sepetin negatif tutara düşmesi) ve Magic String kullanımının getirdiği tip güvensizliğini fark etti.




