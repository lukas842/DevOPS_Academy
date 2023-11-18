#!/usr/bin/env python3
import httpx


def scrape_data(query: str) -> dict:
   print(">> Scraping Data")
   url = "http://api.openweathermap.org/data/2.5/weather"
   params = {
      'units': 'metric',
      'q': query,
      'appid': '9e547051a2a00f2bf3e17a160063002d'
   }
   response = httpx.get(url, params=params)
   data = response.json()
   return data


def process_data(data: dict) -> str:
    print(">> Processing Data")

    # return 'dt;mesto;krajina;teplota;tlak;vlhkost;sila vetra;smer vetra;vychod slnka;zapad slnka'

    return '{};{};{};{};{};{};{};{};{};{}'.format(
        data['dt'],                     #datetime
        data['name'],                   #mesto
        data['sys']['country'],         #krajina
        data['main']['temp'],           #teplota
        data['main']['pressure'],       #tlak
        data['main']['humidity'],       #vlhkost
        data['wind']['speed'],          #rychlost vetra
        data['wind']['deg'],            #smer vetra
        data['sys']['sunrise'],         #vychod slnka
        data['sys']['sunset']           #zapad slnka

    )





def publish_data(line: str):
    print(">> Publishing Data")
    # print(line)
    # file = open('dataset.csv' , mode='a')
    # print(line, file=file)
    # file.close()

    with open ('dataset.csv', mode='a') as dataset:
        print(line, file=dataset)


# [ scrape_data ] -> [ process_data ] -> [ publish_data ]

def main():
    json_data = scrape_data('kosice,sk')
    line = process_data(json_data)
    publish_data(line)


if __name__ == '__main__':
    main()