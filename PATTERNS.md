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
