# PATTERNS.md - Uygulanan Tasarım Örüntüleri

## 1. Factory Method (Creational Pattern)

- **Nerede Kullanıldı:** `src/sepet.py` içerisindeki `IndirimFabrikasi` sınıfında.
- **Neden Kullanıldı:** İndirim nesnelerinin çalışma zamanında (runtime) dinamik olarak yaratılmasını, bu sorumluluğun `AlisverisSepeti` sınıfından tamamen soyutlanmasını sağlamak için.
- **Ne Kazandırdı:** `AlisverisSepeti` sınıfı artık hangi indirim türünün nasıl yaratıldığını bilmek zorunda değil. Sadece fabrikaya ismi söyler ve nesneyi alır. Kod nesne yaratma bazında genişletilebilir hale geldi.

### UML Diyagramı (Önce / Sonra)

#### Önceki Yapı:
AlisverisSepeti (Tüm indirim mantığı ve if-else'ler içeride tek sınıf)

#### Sonraki Yapı:
                                            
     ![UML Diyagramı Sonraki Yapı](sonraki-yapi-uml.png)
     
     
 ## 2. Decorator Pattern (Structural)
- **Nerede Kullanıldı:** `SepetDecorator`, `HediyePaketiEkle` ve `KargoSigortasiEkle` sınıflarında.
- **Neden Kullanıldı:** Temel sepet fiyatlandırma algoritmasına dokunmadan, kullanıcının seçtiği opsiyonel ek hizmetlerin (hediye paketi, sigorta vb.) çalışma zamanında dinamik olarak eklenebilmesi için.
- **Ne Kazandırdı:** Sisteme yeni bir ek hizmet getirilmek istendiğinde mevcut sepet sınıfları değiştirilmek zorunda kalınmayacaktır (OCP).

## 3. Facade Pattern (Structural)
- **Nerede Kullanıldı:** `AlisverisGecidiFacade` sınıfında.
- **Neden Kullanıldı:** Stok, Ödeme ve Kargo alt sistem karmaşasını dış dünyadan gizlemek ve istemciye tek bir bitirme noktası sunmak için.
- **Ne Kazandırdı:** İstemci kod alt sistemlerin detaylarından arındırıldı, gevşek bağlılık (Loose Coupling) sağlandı.

### Faz 2 Mimari Güncellemesi (UML Sınıf Yapısı)


![E-Ticaret Sistemi Mimari Tasarım Diyagramı](mimari-diyagram.png)
