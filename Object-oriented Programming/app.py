"""
25/07/2022

oop # 28 - dars. Kllasslar 

Doston Kamolov

"""
# Class yaratiw uchun class operatoridan foydalanamiz !
class Talaba: # class - yaratiw uchun kalit so'z. Talaba - bu classning nomi.
    def __init__(self,ism,familiya,tyil): # xar bir class ni ichida classni xususyatlarini yaratish uchun class yaratiladi. self - classni ichidagi funksiyaga obyectni uzini uzatish uchun
        self.ism = ism # biz keyingi safar bu classdan obyrct yaratganimizda manashu ibyectni kiritilgan ism ga teyng boladi diyapmiz
        self.familiya = familiya
        self.tyil = tyil
    def get_name(self):
        return self.ism 
    
    def get_age(self,yil):
        return yil - self.tyil
    
    def get_lastname(self):
        return self.familiya 
    
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tu'gilgan yilim {self.tyil}"
talaba1 = Talaba('Doston','Kamolov',2006)  
talaba2 = Talaba('Hasan','Hasanov',2005)  
talaba3 = Talaba('Akrom','Alimov',2008)  











