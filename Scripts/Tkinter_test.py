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
        from_currency = ""
        to_currency = ""
        
        if option.get() == 1:
            from_currency, to_currency = "USD", "EUR"
        elif option.get() == 2:
            from_currency, to_currency = "EUR", "USD"
        elif option.get() == 3:
            from_currency, to_currency = "EUR", "GBP"
        elif option.get() == 4:
            from_currency, to_currency = "GBP", "EUR"
        elif option.get() == 5:
            from_currency, to_currency = "EUR", "JPY"
        elif option.get() == 6:
            from_currency, to_currency = "JPY", "EUR"
        elif option.get() == 7:
            from_currency, to_currency = "EUR", "CAD"
        elif option.get() == 8:
            from_currency, to_currency = "CAD", "EUR"
        elif option.get() == 9:
            from_currency, to_currency = "EUR", "CHF"
        elif option.get() == 10:
            from_currency, to_currency = "CHF", "EUR"
        elif option.get() == 11:
            from_currency, to_currency = "EUR", "CNY"
        elif option.get() == 12:
            from_currency, to_currency = "CNY", "EUR"
        elif option.get() == 13:
            from_currency, to_currency = "EUR", "RUB"
        elif option.get() == 14:
            from_currency, to_currency = "RUB", "EUR"
        elif option.get() == 15:
            from_currency, to_currency = "EUR", "NZD"
        elif option.get() == 16:
            from_currency, to_currency = "NZD", "EUR"
        else:
            messagebox.showerror("Error", "You can choose only from 1-16")
            return

        exchange_rate = get_exchange_rate(api, from_currency, to_currency)

        if exchange_rate is not None:
            if option.get() == 1:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 2:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 3:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 4:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 5:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 6:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 7:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 8:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 9:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 10:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 11:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 12:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 13:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 14:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 15:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
            elif option.get() == 16:
                conv = ans * exchange_rate
                label_result.config(text=f"Conversion from {from_currency} to {to_currency}: {conv}")
        else:
            messagebox.showerror("Error", "Failed to retrieve the exchange rate.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# API key for Alpha Vantage exchange
api = "FRMHKK9YV5A8X6VL"

# Create the main window
root = tk.Tk()
root.title("Live Currency Calculator - Created by LK")

# Option selection
label_option = tk.Label(root, text="Select conversion direction:")
label_option.pack()
option = tk.IntVar()
radio_usd_to_eur = tk.Radiobutton(root, text="USD to EUR", variable=option, value=1)
radio_usd_to_eur.pack()
radio_eur_to_usd = tk.Radiobutton(root, text="EUR to USD", variable=option, value=2)
radio_eur_to_usd.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to GBP", variable=option, value=3)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="GBP to EUR", variable=option, value=4)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to JPY", variable=option, value=5)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="JPY to EUR", variable=option, value=6)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to CAD", variable=option, value=7)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="CAD to EUR", variable=option, value=8)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to CHF", variable=option, value=9)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="CHF to EUR", variable=option, value=10)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to CNY", variable=option, value=11)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="CNY to EUR", variable=option, value=12)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to RUB", variable=option, value=13)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="RUB to EUR", variable=option, value=14)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="EUR to NZD", variable=option, value=15)
radio_eur_to_gbp.pack()
radio_eur_to_gbp = tk.Radiobutton(root, text="NZD to EUR", variable=option, value=16)
radio_eur_to_gbp.pack()

# Amount entry
label_amount = tk.Label(root, text="Enter the amount:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# Convert button
button_convert = tk.Button(root, text="Convert", command=convert_currency)
button_convert.pack()

# Result label
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
