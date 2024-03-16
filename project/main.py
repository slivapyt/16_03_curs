from datetime import datetime
import requests
import json
import os
API_KEY = os.getenv('Exchange_Rates_Data_API')
CURRENCY_RATES_FILE = 'currency_rates.json'


def main():
    while True:
        currency = input("Введите названеие валюты (USD или EUR)")
        if currency not in ('USD', 'EUR'):
            print("неверная валюта")
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f"Курс {currency} к рублю: {rate}")
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('выберите действие: (1 - продожить, 2 - выйти)')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print("Некорректный ввод")


def get_currency_rate(base: str) -> float:
    """Получает курс API и возвращает его в виде float"""
    url = "https://api.apilayer.com/exchangerates_data/latest"

    response = requests.get(
        url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    '''Сохраняет данные в json файл.'''
    with open(CURRENCY_RATES_FILE, 'a') as f:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATES_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as f:
                json.dump(data_list, f)


if __name__ == '__main__':
    main()
