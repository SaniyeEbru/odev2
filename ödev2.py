def katmaDegerCiroHesapla():
    print("Lütfen istenilen değerleri giriniz.")
    a=int(input("toplam satış miktarı:"))
    b=int(input("hammadde maliyeti:"))
    c=int(input("bakım onarım giderleri:"))
    d=int(input("sevkiyat giderleri:"))
    e=int(input("satın alınan hizmet giderleri:"))
    katmaDegerCiro=a-(b+c+d+e)
    if (katmaDegerCiro>1000):
        print("İşletme katma değer cirosu yüksek.")
    elif (500<katmaDegerCiro<999):
        print("İşletme katma değer cirosu normal")
    else:
        print("İşletme katma değer cirosu düşük")






def ilkyıl():
    cS=170
    tMS=50
    global müstericalismasüre
    müstericalismasüre=cS/tMS
    return müstericalismasüre
def ikinciyıl():
    cS=220
    tMS=70
    global müstericalismasüre
    müstericalismasüre=cS/tMS
    return müstericalismasüre
ilk=ilkyıl()
ikinci=ikinciyıl()

cıkar=ikinci-ilk
print("2017 ve 2016 yılları müşterilerle çalışma süreleri arasındaki fark",cıkar)







def ilkaltiaygelir(yazılımGeliri,finansmanGeliri,ürünSatısGeliri):
    global itoplamGelir
    itoplamGelir=yazılımGeliri+finansmanGeliri+ürünSatısGeliri
    return itoplamGelir
def ilkaltiaygider(calısanMaaslari,kiraGideri,donanımMaliyeti):
    global itoplamGider
    itoplamGider=calısanMaaslari+kiraGideri+donanımMaliyeti
    return itoplamGider
def sonaltiaygelir(yazılımGeliri,finansmanGeliri,ürünSatısGeliri):
    global stoplamGelir
    stoplamGelir=yazılımGeliri+finansmanGeliri+ürünSatısGeliri
    return stoplamGelir
def sonaltiaygider(calısanMaaslari,kiraGideri,donanımMaliyeti):
    global stoplamGider
    stoplamGider=calısanMaaslari+kiraGideri+donanımMaliyeti
    return stoplamGider
def isletmekarhesapla(itoplamGelir,itoplamGider,stoplamGelir,stoplamGider):
    kar=((itoplamGelir-itoplamGider)-(stoplamGelir-stoplamGider))
    if (kar>5000):
        print("işletme çok karlı.")
    elif (1000<kar<5000):
        print("işletme karı normal.")
    else:
        print("işletme yeterince karda değil.")
        
yazılımGeliri=int(input("yazılım geliri giriniz."))
finansmanGeliri=int(input("finasnman geliri giriniz."))
ürünSatısGeliri=int(input("ürün satış geliri giriniz."))
calısanMaaslari=int(input("çalışan maaşları giiriniz."))
kiraGideri=int(input("kira gideri giriniz."))
donanımMaliyeti=int(input("donanım maliyeti giriniz."))

iagelir=ilkaltiaygelir(yazılımGeliri,finansmanGeliri,ürünSatısGeliri)
iagider=ilkaltiaygider(calısanMaaslari,kiraGideri,donanımMaliyeti)
sagelir=sonaltiaygelir(yazılımGeliri,finansmanGeliri,ürünSatısGeliri)
sagider=sonaltiaygider(calısanMaaslari,kiraGideri,donanımMaliyeti)

isletmekarhesapla(iagelir,iagider,sagelir,sagider)





print("Dönem başı stok değerlerini giriniz.")
ks=int(input("koltuk sayısı:"))
ys=int(input("yatak sayısı:"))
ds=int(input("dolap sayısı:"))
def dönembasistokgerleri(ks,ys,ds):
    global dönembasistok
    dönembasistok=ks+ys+ds
    return dönembasistok
def dönemsonustokdegerlerisatılan(ks,ys,ds):
    ks=25
    ys=20
    ds=10
    global dönemsonusatılan
    dönemsonusatılan=ks+ys+ds
    return dönemsonusatılan
def dönemsonustokdegerlerialınan(ks,ys,ds):
    ks=10
    ys=15
    ds=5
    global dönemsonualınan
    dönemsonualınan=ks+ys+ds
    return dönemsonualınan
def yıllıkortalamastokdegerleri(dönembasistok,dönemsonusatılan,dönemsonualınan):
    ortalamastok=(dönembasistok+(dönemsonusatılan+dönemsonualınan))/2
    print("yıllık ortalama stok degeri;",yıllıkortalamastokdegerleri) 
    
bas=dönembasistokgerleri(ks,ys,ds)
sons=dönemsonustokdegerlerisatılan(ks,ys,ds)
sona=dönemsonustokdegerlerialınan(ks,ys,ds)

yıllıkortalamastokdegerleri(bas,sons,sona)









    
    
    
