import csv
import datetime

# metin.txt dosyası oluşturup içerisine menuyu yazdırdım.

with open("metin.txt", "w") as f:
    f.write("* Lutfen Bir Pizza Tabani Seciniz:\n"
        "1: Klasik\n"
        "2: Margarita\n"
        "3: TurkPizza\n"
        "4: Sade Pizza\n"
        "* ve sececeginiz sos:\n"
        "11: Zeytin\n"
        "12: Mantarlar\n"
        "13: Keci Peyniri\n"
        "14: Et\n"
        "15: Sogan\n"
        "16: Misir\n"
        "* Tesekkur ederiz!\n")
    
#Pizza üst sınıfını oluşturdum.
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
# Pizza sınıfının alt sınıflarını oluşturdum.
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 50)
        
class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 60)
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("TurkPizza", 70)
        
class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 45)

class Decorator:
    def __init__(self, pizza, description, cost):
        self.pizza = pizza
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.pizza.get_description() + ", " + self.description
    
    def get_cost(self):
        return self.pizza.get_cost() + self.cost

class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Zeytin", 8)
        
class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mantarlar", 12)
        
class KeçiPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Keçi Peyniri", 10)
        
class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Et", 15)
        
class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Soğan", 3)
        
class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mısır", 5)

def main():
  # Menüyü (metin.txt dosyasını) ekrana yazdırıyorum.
  with open("metin.txt", "r") as f:
    print(f.read())
    
  # Kullanıcıdan bilgilerini ve seçmek istediği pizzayı ve sosu alıyorum. 
    pizza_seçimi = int(input("Pizza seçiminiz nedir? (1-4): "))
    
    if pizza_seçimi == 1:
        pizza = KlasikPizza()
    elif pizza_seçimi == 2:
        pizza = MargaritaPizza()
    elif pizza_seçimi == 3:
        pizza = TurkPizza()
    elif pizza_seçimi == 4:
        pizza = SadePizza()
    else:
        print("Yanlış seçim yaptınız!")
        return
   
    sos_seçimi = int(input("Sos seçiminiz nedir? (11-16): "))
    
    if sos_seçimi == 11:
        pizza = Zeytin(pizza)
    elif sos_seçimi == 12:
        pizza = Mantarlar(pizza)
    elif sos_seçimi == 13:
        pizza = KeçiPeyniri(pizza)
    elif sos_seçimi == 14:
        pizza = Et(pizza)
    elif sos_seçimi == 15:
        pizza = Sogan(pizza)
    elif sos_seçimi == 16:
        pizza = Misir(pizza)
    
    print("\n* Seçtiğiniz pizza ve sos: " + pizza.get_description())
    print("* Toplam ücret: " + str(pizza.get_cost()) + " TL") # Seçilen siparişe göre toplam fiyat hesaplanıyor.

    # Sipariş bilgilerini Orders_Database.csv dosyasına kaydetme işlemini gerçekleştiriyorum.
    now = datetime.datetime.now()
    date_string = now.strftime("%Y-%m-%d_%H-%M-%S")

    isim = input("Lütfen adınızı ve soyadınızı giriniz: ")
    tc = input("Lütfen TC kimlik numaranızı giriniz: ")
    kart_no = input("Lütfen kart numaranızı giriniz: ")
    kart_sifre = int(input("Lütfen kart şifrenizi giriniz: "))

    with open("Orders_Database.csv", "a", newline="") as f:
       writer = csv.writer(f)
       writer.writerow([date_string, pizza.get_description(), pizza.get_cost(), isim , tc, kart_no , kart_sifre])
    print("Siparişiniz Alındı! En kısa sürede size ulaştıracağız. :)")
    
main()
