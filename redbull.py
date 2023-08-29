import requests
import random
import string
import time
import warnings

def handle_warning(message, category, filename, lineno, file=None, line=None):
    if category == requests.packages.urllib3.exceptions.InsecureRequestWarning:
        pass

warnings.showwarning = handle_warning

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)



device_id = '-'.join(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) for _ in range(5))




def giris_token():
	url2 = "https://wndr.azurewebsites.net/api/v1/auth/login/email"
	headers2 = {
		"X-Device-Model": "iPhone13,2",
		"Connection": "keep-alive",
		"X-Device-ID": device_id,
		"X-Device-Type": "iOS",
		"X-Accept-Version": "1.1",
		"Content-Type": "application/json",
		"Accept-Encoding": "gzip, deflate, br",
		"X-App-Version": "1.3.0",
		"Host": "wndr.azurewebsites.net",
		"Accept-Language": "en",
		"User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
		"Accept": "*/*"
		}
		
	data2 = {"email": "eposta","password":"sifre"}
	response2 = requests.post(url2, headers=headers2, json=data2)
	sonuc2 = response2.json()
	try:
		token = response2.json()["accessToken"]
		print("Token cekildi")
		return token
	except:
		print("Token Cekilemedi")
		raise SystemExit()

sonuc2 = giris_token()


headers3 = {
    "X-Device-Model": "iPhone13,2",
    "Connection": "keep-alive",
    "Authorization": "Bearer " + sonuc2,
    "X-Device-Type": "iOS",
    "X-Accept-Version": "1.1",
    "X-Device-ID": device_id,
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "X-App-Version": "1.3.0",
    "Host": "wndr.azurewebsites.net",
    "Accept-Language": "en",
    "User-Agent": "RBM%20data/84 CFNetwork/1390 Darwin/22.0.0",
    "Accept": "*/*"
}


def paket_aktifle():
    satin_al = "https://wndr.azurewebsites.net/api/v1/packages/order-free-package"
    satinal_data = {"packageId": "mDFiwArRhFsEJVhTEd_XU"}
    satinal = requests.post(satin_al, headers=headers3, json=satinal_data)
    sonucc = satinal.json()

    if sonucc == {}:
        print("\nPaket Aktiflendi")
    else:
        print("Paket Aktiflenmedi")
        raise SystemExit()

paket_aktifle()

while True:
    kontrol = requests.get("https://wndr.azurewebsites.net/api/v1/dashboard/active-packages", headers=headers3)
    try:
    	kullanilan1 = kontrol.json()["packages"][0]["usedData"]
    	if kullanilan1 == 1124:
    		paket_aktifle()
    except:
    	giris_token()
	sonuc2 = giris_token()
    	paket_aktifle()
    	time .sleep(3)
    time.slee(3)
