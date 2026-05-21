from abc import ABC, abstractmethod


class IndirimStratejisi(ABC):
    @abstractmethod
    def uygula(self, tutar: float) -> float:
        pass

class EfsaneCumaIndirimi(IndirimStratejisi):
    def uygula(self, tutar: float) -> float: return tutar * 0.50

class HosGeldinKuponuIndirimi(IndirimStratejisi):
    def uygula(self, tutar: float) -> float: return max(0, tutar - 50)

class StandartFiyat(IndirimStratejisi):
    def uygula(self, tutar: float) -> float: return tutar

class IndirimFabrikasi:
    @staticmethod
    def indirim_olustur(indirim_turu: str) -> IndirimStratejisi:
        indirim_haritasi = {
            "EFSANE_CUMA": EfsaneCumaIndirimi(),
            "HOŞ_GELDİN_KUPONU": HosGeldinKuponuIndirimi()
        }
        return indirim_haritasi.get(indirim_turu, StandartFiyat())


class SepetBileseni(ABC):
    @abstractmethod
    def fiyat_hesapla(self) -> float:
        pass

class AlisverisSepeti(SepetBileseni):
    def __init__(self, toplam_tutar: float, indirim_turu=""):
        self.toplam_tutar = toplam_tutar
        self.indirim_turu = indirim_turu

    def fiyat_hesapla(self) -> float:
        indirim = IndirimFabrikasi.indirim_olustur(self.indirim_turu)
        return indirim.uygula(self.toplam_tutar)

class SepetDecorator(SepetBileseni):
    def __init__(self, sepet: SepetBileseni):
        self._sepet = sepet
    def fiyat_hesapla(self) -> float:
        return self._sepet.fiyat_hesapla()

class HediyePaketiEkle(SepetDecorator):
    def fiyat_hesapla(self) -> float: return self._sepet.fiyat_hesapla() + 15.0

class KargoSigortasiEkle(SepetDecorator):
    def fiyat_hesapla(self) -> float: return self._sepet.fiyat_hesapla() + 25.0




class SiparisGozlemcisi(ABC):
    @abstractmethod
    def guncelle(self, mesaj: str):
        pass


class SmsBildirimci(SiparisGozlemcisi):
    def guncelle(self, mesaj: str):
        print(f"[SMS] Kullaniciya mesaj gonderildi: {mesaj}")

class EpostaBildirimci(SiparisGozlemcisi):
    def guncelle(self, mesaj: str):
        print(f"[E-Posta] Sirkete rapor gonderildi: {mesaj}")



class StokSistemi:
    def kontrol_et(self): return "Stok onaylandi."

class OdemeSistemi:
    def tahsil_et(self, tutar: float): return f"{tutar} TL tahsil edildi."

class KargoSistemi:
    def kayit_olustur(self): return "Kargo kaydi acildi."

class AlisverisGecidiFacade:
    def __init__(self):
        self.stok = StokSistemi()
        self.odeme = OdemeSistemi()
        self.kargo = KargoSistemi()
        self._gozlemciler = []  # Gözlemci listesi

    def gozlemci_ekle(self, gozlemci: SiparisGozlemcisi):
        self._gozlemciler.append(gozlemci)

    def gozlemci_cikar(self, gozlemci: SiparisGozlemcisi):
        self._gozlemciler.remove(gozlemci)

    def _herkese_haber_ver(self, mesaj: str):
        for gozlemci in self._gozlemciler:
            gozlemci.guncelle(mesaj)

    def alisverisi_tamamla(self, sepet: SepetBileseni):
        son_tutar = sepet.fiyat_hesapla()
        rapor = [
            self.stok.kontrol_et(),
            self.odeme.tahsil_et(son_tutar),
            self.kargo.kayit_olustur()
        ]
        
        cikis_mesaji = f"Siparisiniz {son_tutar} TL ile tamamlanmistir."
        # Davranışı tetikliyoruz (Observer eylemi)
        self._herkese_haber_ver(cikis_mesaji)
        
        return " | ".join(rapor)

# Basit Bir Derleme Doğrulama Testi (CI hattının patlamaması için)
def test_sepet_akisi():
    sepet = AlisverisSepeti(100, "EFSANE_CUMA") # 50 TL kalır
    suslu_sepet = HediyePaketiEkle(sepet) # 50 + 15 = 65 TL kalır
    
    facade = AlisverisGecidiFacade()
    facade.gozlemci_ekle(SmsBildirimci())
    facade.gozlemci_ekle(EpostaBildirimci())
    
    sonuc = facade.alisverisi_tamamla(suslu_sepet)
    assert suslu_sepet.fiyat_hesapla() == 65.0
    print("Tum mimari testler basariyla gecti!")

if __name__ == "__main__":
    test_sepet_akisi()
