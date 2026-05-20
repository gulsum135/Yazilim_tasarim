# AI Log - Phase 1 (Creational)

## AI'a Ne Soruldu? (Prompt)
"E-ticaret sepetindeki if-else indirim kontrolü sorununu çözmek için Factory Method tasarım kalıbını Python'da nasıl uygulayabilirim? Nesne yaratımını sepet sınıfından nasıl soyutlarım?"

## AI Ne Yanıtladı? (Özet)
AI, `IndirimStratejisi` adında bir soyut taban sınıf oluşturmayı, her indirim türünü ayrı bir sınıf yapmayı ve `IndirimFabrikasi` üzerinden string girdilere göre bu nesneleri üretmeyi önerdi. Ayrıca kupon kodunda negatif tutar kontrolü yapılması gerektiği uyarısını yineledi.

## Ben Ne Uyguladım ve Neden?
AI önerisiyle birebir aynı mantıkta Factory yapısını uyguladım. Farklı olarak, kodun okunabilirliğini artırmak için fabrika içinde uzun if-else zinciri yerine Python sözlük (dictionary) yapısını kullanarak nesne eşleştirmesi yaptım. Negatif tutar kontrolünü `max(0, tutar - 50)` şeklinde uygulayarak iş mantığı hatasını düzelttim.
