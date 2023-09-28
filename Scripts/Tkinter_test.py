import tkinter as tk
from tkinter import messagebox
import requests

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

def convert_currency():
    try:
        ans = float(entry_amount.get())
        exchange_rate = get_exchange_rate(api, from_currency, to_currency)

        if exchange_rate is not None:
            if option.get() == 1:
                label_result.config(text=f"Conversion from USD to EUR: {ans} USD = {ans * exchange_rate} EUR")
            elif option.get() == 2:
                label_result.config(text=f"Conversion from EUR to USD: {ans} EUR = {ans / exchange_rate} USD")
            else:
                messagebox.showerror("Error", "You can choose only from 1-2")
        else:
            messagebox.showerror("Error", "Failed to retrieve the exchange rate.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

print("This is currency calculator")

api = "FRMHKK9YV5A8X6VL"
from_currency = "USD"
to_currency = "EUR"

root = tk.Tk()
root.title("Currency Calculator")

label_option = tk.Label(root, text="Select conversion direction:")
label_option.pack()

option = tk.IntVar()
radio_usd_to_eur = tk.Radiobutton(root, text="USD to EUR", variable=option, value=1)
radio_usd_to_eur.pack()
radio_eur_to_usd = tk.Radiobutton(root, text="EUR to USD", variable=option, value=2)
radio_eur_to_usd.pack()

label_amount = tk.Label(root, text="Enter the amount:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
