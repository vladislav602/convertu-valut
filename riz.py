import  requests



def valuta():
    response = requests.get(
        f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20200302&json"
    )
    data = response.json()
    print(data)
    print(data[0]["rate"])
valuta()