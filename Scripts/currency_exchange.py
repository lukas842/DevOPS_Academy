import requests

print("This is currency calculator")

option = input("Type 1 for USD to EUR | Type 2 for EUR to USD | Type 3 for EUR to BGP: ")
option = float(option)
             
ans = input("Write ammount you want to convert: ")
ans = float(ans)

def get_exchange_rate(api, from_currency, to_currency):
    url = "https://www.alphavantage.co/query" 
    function = "CURRENCY_EXCHANGE_RATE"


    params = {
        "function": function,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "apikey": api        
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.json()

    if "Realtime Currency Exchange Rate" in data:
            exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
            return exchange_rate
    else:
            print("Failed to retrieve exchange rate data from response.")
            return None
      
#Api key for Alpha Vantage exchange    
api = "FRMHKK9YV5A8X6VL"


#Currencies conversion
if option == 1:
    #Currencies to convert
    from_currency = "USD"
    to_currency = "EUR"
    #Get the exchange rate
    exchange_rate = get_exchange_rate(api, from_currency, to_currency)
    conv = ans * exchange_rate
    print(f"Conversion from USD to EUR: {conv}")

elif option ==2:
    #Currencies to convert
    from_currency = "USD"
    to_currency = "EUR"
    #Get the exchange rate
    exchange_rate = get_exchange_rate(api, from_currency, to_currency)
    conv = ans / exchange_rate 
    print(f"Conversion from EUR to USD: {conv}")

elif option ==3:
    #Currencies to convert
    from_currency = "EUR"
    to_currency = "GBP"
    #Get the exchange rate
    exchange_rate = get_exchange_rate(api, from_currency, to_currency)
    conv = ans * exchange_rate 
    print(f"Conversion from EUR to GBP: {conv}")
else:
      print("You can choose only from 1-2")

if exchange_rate is not None:
    print(f"Actuall rates: 1 {from_currency} = {exchange_rate} {to_currency}")
else:
    print("Failed to retrive the exchange rate.")



