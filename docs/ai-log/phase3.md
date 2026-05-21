# AI Log - Faz 3 (Behavioral)

## AI ile Pair Programming Oturumu Özeti
Sipariş tamamlandığında tetiklenecek eylemleri dinamik kılmak adına Observer örüntüsü üzerine 30 dakikalık mimari bir çalışma yürütüldü. AlisverisGecidiFacade sınıfı "Subject" (özne) haline getirilerek, bildirim yapılarının dışarıdan inject edilmesi sağlanmıştır.

## Kritik Soru Cevapları
- **AI olmadan bu faz ne kadar sürerdi?:** AI olmadan CI pipeline yaml konfigürasyonunu kurmak ve test senaryolarını entegre etmek yaklaşık 2-3 saat sürebilirdi, AI desteğiyle 30 dakikada tamamlandı.
- **AI sizi nerede yanılttı?:** AI ilk etapta Observer listesini AlisverisSepeti sınıfına eklememi söyledi. Fakat sepet sadece ürün fiyatı tutmalıdır; sipariş tamamlama işini Facade yürüttüğü için gözlemcilerin Facade sınıfına bağlanması gerektiğini bağımsız mantığımla çözdüm ve AI hatasını düzelttim.
