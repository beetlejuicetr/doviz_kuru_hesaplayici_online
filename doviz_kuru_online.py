from bs4 import BeautifulSoup
import requests


acilis_ekrani = """
______________________________
| DÖVİZ KURU HESAPLAYICI 
______________________________
| 
| Sürüm   : v1.4
| Yapımcı : Beetlejuicetr (MID)
| Destekci: Адыгэ
| Dil     : Python 3.9
______________________________


Kullanım;

USD - TRY için : 1
TRY - USD için : 2

EUR - TRY için : 3
TRY - EUR için : 4

USD - EUR için : 5
EUR - USD için : 6 

yazabilirsiniz.

- Çıkmak için Ctrl - Z -

"""

print(acilis_ekrani)

url = "https://dolar.tlkur.com/" #Yazılan siteyi "url" değişkenine eşitliyor

result = requests.get(url) #sonucu alınan isteklere eşitliyor
doc = BeautifulSoup(result.text, "html.parser") #sonuç yazısını ayıklıyor

####################################
dolar_tl = doc.find_all(id="USDTRY") #Dosyada (sitede) arama yapar.
dolar_tl_parent = dolar_tl[0].parent
#---------------------------------#
####################################

euro_tl = doc.find_all(id="EURTRY")
euro_tl_parent = euro_tl[0].parent
#---------------------------------#
###################################

euro_usd = doc.find_all(id="EURUSD")
euro_usd_parent = euro_usd[0].parent

dolar_tl_span = dolar_tl_parent.find("span")
dolar_tl_kur= dolar_tl_span.string



euro_tl_span = euro_tl_parent.find("span")
euro_tl_kur= euro_tl_span.string


euro_usd_span = euro_usd_parent.find("span")
euro_usd_kur = euro_usd_span.string


while True:
	try:
		girdi = float(input("\nYapılacak işlemi giriniz: "))
		if float(girdi) < 1 or float(girdi) > 6:
			print("[UYARI] Lütfen (1 - 6) arası sayı giriniz.")
			break

		girdi2 = float(input("Dönüştürmek istediğiniz miktarı giriniz: "))
	except ValueError:
		print("[UYARI] Sadece sayı girmelisiniz.")
		break
	print("-"*15)
	print("Sonuç ;")
	
	if girdi == 1:
		sonuc = girdi2 * float(dolar_tl_kur)
		print(girdi2,"Dolar ($)",":",sonuc,"Türk Lirası (₺)")
		pass
	elif girdi == 2:
		sonuc = girdi2 / float(dolar_tl_kur)
		print(girdi2,"Türk Lirası (₺)",":",sonuc,"Dolar ($)",)
		pass
	elif girdi == 3:
		sonuc = girdi2 * float(euro_tl_kur)
		print(girdi2,"Euro (€)",":",sonuc,"Türk Lirası (₺)")
		pass
	elif girdi == 4:
		sonuc = girdi2 / float(euro_tl_kur)
		print(girdi2,"Türk Lirası (₺)",":",sonuc,"Euro (€)",)
		pass

	elif girdi == 5:
		sonuc = girdi2 / float(euro_usd_kur)
		print(girdi2,"Dolar ($)",":",sonuc,"Euro (€)")
	elif girdi == 6:
		sonuc = girdi2 * float(euro_usd_kur)
		print(girdi2,"Euro (€)",":",sonuc,"Dolar ($)")
	print("-"*15)
	

	pass
