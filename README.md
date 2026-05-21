# E-Ticaret Sepeti Kampanya ve İşlem Yönetim Sistemi (Konu D)

Bu proje; bir e-ticaret sistemindeki alışveriş sepeti, kampanya/indirim uygulamaları ve sipariş tamamlama süreçlerinin, **Nesne Yönelimli Tasarım Örüntüleri (Design Patterns)** kullanılarak esnek, sürdürülebilir ve genişletilebilir bir mimariye dönüştürülmesini içerir.

## 🚀 Projenin Ne Yaptığı
Sistem; temel bir alışveriş sepeti üzerine dinamik olarak indirimlerin (Efsane Cuma, Öğrenci İndirimi vb.) uygulanmasını, sepete ek hizmetlerin (Kargo Sigortası, Hediye Paketi) çalışma zamanında giydirilmesini sağlar. Sipariş onaylandığında ise arka plandaki karmaşık alt sistemleri (Stok, Ödeme, Kargo) tek bir merkezden yöneterek süreci tamamlar ve ilgili gözlemcilere (SMS, E-Posta) otomatik bildirim tetikler.

## Kullanılan Tasarım Örüntüleri (Design Patterns)

### 1. Creational (Yaratımsal): Factory Method
* **Açıklama:** İndirim nesnelerinin (`EfsaneCumaIndirimi`, `OgrenciIndirimi`) yaratılma sorumluluğunu sepet sınıfından ayırır. Sistemde yeni bir indirim türü eklendiğinde mevcut kodların bozulmasını önleyerek (Open-Closed Prensibi) nesne üretimini tek merkezden yönetir.

### 2. Structural (Yapısal): Decorator
* **Açıklama:** Alışveriş sepetine kodun temel yapısını değiştirmeden dinamik olarak ek özellikler veya maliyetler (Örn: Hediye Paketi, Kargo Sigortası) eklemek için kullanılmıştır. Her dekoratör, sepet bileşenini sarmalayarak fiyat hesaplamasını genişletir.

### 3. Structural (Yapısal): Facade
* **Açıklama:** Arka planda çalışan Karmaşık Stok, Ödeme ve Kargo alt sistemlerinin yönetimini tek bir sınıf (`AlisverisGecidiFacade`) arkasında gizler. İstemci (Client), bu alt sistemlerin detaylarıyla uğraşmadan tek bir metotla alışverişi tamamlar.

### 4. Behavioral (Davranışsal): Observer
* **Açıklama:** Sipariş başarıyla tamamlandığında sistemlerin gevşek bağlı (loosely coupled) bir şekilde tetiklenmesini sağlar. `AlisverisGecidiFacade` bir olay tetiklediğinde, sisteme abone olan SMS ve E-Posta servisleri otomatik olarak bilgilendirilir.

---

## 📊 Mimari Diyagram (UML)

Projenin nesne yönelimli tasarım mimarisini ve örüntülerin birbiriyle olan ilişkisini gösteren UML Sınıf Diyagramı aşağıda sunulmuştur:

![E-Ticaret Sepeti UML Sınıf Diyagramı](docs/diagrams/sepet_mimari_uml.png)

---

## 💻 Nasıl Çalıştırılır?

Projenin yerel ortamda test senaryolarıyla birlikte çalıştırılması ve doğrulanması için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler
* Python 3.8 veya üzeri bir sürümün bilgisayarınızda kurulu olması gerekmektedir.

### Çalıştırma Komutu
Projenin kök dizininde terminali açarak şu komutu çalıştırmanız yeterlidir:
```bash
python src/sepet.py
