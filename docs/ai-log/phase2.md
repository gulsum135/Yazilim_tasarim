# AI Log - Faz 2 (Structural Örüntüler)

## AI Tasarım Tartışması (Soru)
"E-Ticaret sepeti sisteminde alt sistem entegrasyonlarını basitleştirmek için Adapter pattern mı burada daha uygundur, yoksa Facade mı? Farkını açıkla."

## AI Yanıt Özeti
AI, sistemimizde uyumsuz iki arayüzü birbirine uydurma zorunluluğumuz olmadığını; aksine Stok, Ödeme ve Kargo gibi birbirinden bağımsız çalışan karmaşık alt sistemleri tek bir üst merkezden yönetmek istediğimizi belirtti. Bu yüzden Adapter yerine Facade kullanılmasının doğru olduğunu doğruladı.

## AI'ın Yanlış/Eksik Önerisi ve Kritik Değerlendirme
AI, Decorator modelini koda eklemeyi önerirken doğrudan `AlisverisSepeti` sınıfının iç yapısını değiştirmemi tavsiye etti. Ancak bu yaklaşım Faz 1'de çalışan fabrika mimarimi bozuyordu ve Open-Closed prensibine aykırıydı. Bu mimari hatayı bağımsız olarak fark ettim ve hem mevcut sepet sınıfımızın hem de süsleyicilerin türeyeceği ortak bir `SepetBileseni` soyut sınıfı tanımladım. Böylece eski koda hiç dokunmadan sistemi sarmalamayı başardım.
