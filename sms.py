import requests

# Gönderilecek mesaj
mesaj = "Naptin yarrrrram."

# Telefon numaraları listesi
telefon_numaralari = ["+901234567890", "+909876543210"]

# API anahtarı ve URL'yi girin
api_key = "YOUR_API_KEY"
url = "https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json"

for numara in telefon_numaralari:
    data = {
        "To": numara,
        "From": "+15555555555",
        "Body": mesaj,
    }
    headers = {
        "Authorization": "Basic {}".format(base64.b64encode(bytes(api_key + ":", "utf-8")).decode("utf-8")),
    }
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 201:
        print("Mesaj başarıyla gönderildi:", numara)
    else:
        print("Mesaj gönderilemedi:", numara, response.status_code)
