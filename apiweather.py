import requests

def hava_durumu_goster(api_key, sehir):
    base_url = "http://api.weatherapi.com/v1/current.json"

    params = {
        'key': api_key,
        'q': sehir
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        hava_durumu_verisi = response.json()

        print(f"Hava Durumu Bilgileri - {sehir}")
        print(f"Sıcaklık: {hava_durumu_verisi['current']['temp_c']}°C")
        print(f"Nem Oranı: {hava_durumu_verisi['current']['humidity']}%")
        print(f"Hava Durumu: {hava_durumu_verisi['current']['condition']['text']}")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Hatası: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Bağlantı Hatası: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Zaman Aşımı Hatası: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Bilinmeyen bir hata oluştu: {err}")


api_key = "73a75bb3f1a443cd88f170415231312"
sehir = input("Hava durumu bilgisini öğrenmek istediğiniz şehir adını girin: ")

hava_durumu_goster(api_key, sehir)
