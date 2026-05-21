from abc import ABC, abstractmethod


class IndirimStratejisi(ABC):
    @abstractmethod
    def uygula(self, tutar):
        pass

class EfsaneCumaIndirimi(IndirimStratejisi):
    def uygula(self, tutar): return tutar * 0.50

class HosGeldinKuponuIndirimi(IndirimStratejisi):
    def uygula(self, tutar): return max(0, tutar - 50)

class StandartFiyat(IndirimStratejisi):
    def uygula(self, tutar): return tutar

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
    def __init__(self, toplam_tutar, indirim_turu=""):
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
    def fiyat_hesapla(self) -> float:
        return self._sepet.fiyat_hesapla() + 15.0  # Hediye paketi +15 TL

class KargoSigortasiEkle(SepetDecorator):
    def fiyat_hesapla(self) -> float:
        return self._sepet.fiyat_hesapla() + 25.0  # Kargo sigortası +25 TL


class StokSistemi:
    def kontrol_et(self): return "Stok onaylandi."

class OdemeSistemi:
    def tahsil_et(self, tutar): return f"{tutar} TL tahsil edildi."

class KargoSistemi:
    def kayit_olustur(self): return "Kargo fise eklendi."


class AlisverisGecidiFacade:
    def __init__(self):
        self.stok = StokSistemi()
        self.odeme = OdemeSistemi()
        self.kargo = KargoSistemi()
    def toplam_hesapla(self, indirim_turu):
        if indirim_turu == "EFSANE_KASIM":
            return self.toplam_tutar * 0.50  # %50 indirim
        elif indirim_turu == "HOŞ_GELDİN_KUPONU":
            return self.toplam_tutar - 50     # 50 TL indirim
        elif indirim_turu == "ÖĞRENCİ":
            return self.toplam_tutar * 0.90  # %10 indirim
        else:
            return self.toplam_tutar

    def alisverisi_tamamla(self, sepet: SepetBileseni):
        son_tutar = sepet.fiyat_hesapla()
        rapor = [
            self.stok.kontrol_et(),
            self.odeme.tahsil_et(son_tutar),
            self.kargo.kayit_olustur()
        ]
        return " | ".join(rapor)
        
