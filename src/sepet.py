
	
from abc import ABC, abstractmethod

class IndirimStratejisi(ABC):
    @abstractmethod
    def uygula(self, tutar):
        pass

class EfsaneKasimIndirimi(IndirimStratejisi):
    def uygula(self, tutar):
        return tutar*0.50

class HosGeldinKuponIndirimi(IndirimStratejisi):
    def uygula(self, tutar):
        retrn max (0, tutar-50)

class OgrenciIndirimi(IndirimStratejisi):
    def uygula(self, tutar):
        return tutar *0.90
    
class standartFiyat(IndirimStratejisi):
    def uygula(self, tutar):
        return tutar
    
class IndirimFabrikasi:
    @staticmethod
    def indirim_olustur(indirim_turu: str)-> IndirimStratejisi:
        sozluk = {
            "EFSANE_KASIM": EfsaneKasimIndirimi(),
            "HOŞ_GELDİN_KUPONU": HosGeldinKuponIndirimi(),
            "ÖĞRENCİ": OgrenciIndirimi()
        }
        return sozluk.get(indirim_turu, standartFiyat())
    

class AlisverisSepeti:
    def __init__(self, toplam_tutar):
        self.toplam_tutar =toplam_tutar
    
    def toplam_hesapla(self, indirim_turu: str):
        indirim =IndirimFabrikasi.indirim_olustur(indirim_turu=)
        return indirim.uygula(self.toplam_tutar)
    
        self.toplam_tutar = toplam_tutar

    def toplam_hesapla(self, indirim_turu):
        if indirim_turu == "EFSANE_KASIM":
            return self.toplam_tutar * 0.50  # %50 indirim
        elif indirim_turu == "HOŞ_GELDİN_KUPONU":
            return self.toplam_tutar - 50     # 50 TL indirim
        elif indirim_turu == "ÖĞRENCİ":
            return self.toplam_tutar * 0.90  # %10 indirim
        else:
            return self.toplam_tutar

