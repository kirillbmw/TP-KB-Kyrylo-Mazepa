import requests

NBU_API_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

def get_exchange_rates():
    response = requests.get(NBU_API_URL)
    return response.json()

def convert_currency(amount, currency, rates): 
    for rate in rates: #Ітерація по списку курсів валют
        if rate['cc'] == currency:
            return amount * rate['rate']
    return None 

def main():
    rates = get_exchange_rates()
    currencies = {"EUR": "Євро", "USD": "Долар США", "PLN": "Польський злотий"}

    print("Доступні валюти для конвертації: EUR, USD, PLN")
    currency = input("Введіть код валюти (EUR, USD, PLN): ").upper()
    amount = float(input(f"Введіть кількість {currencies[currency]}: "))

    result = convert_currency(amount, currency, rates)
    print(f"{amount} {currency} = {result:.5f} UAH") 

main()
