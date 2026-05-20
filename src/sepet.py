
class AlisverisSepeti:
    def __init__(self, toplam_tutar):
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

