import requests
import xml.etree.ElementTree as ET
import tkinter as tk
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def fetch_rates(event=None):
    selected_currency = currency_entry.get()
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    response = requests.get(url=url)
    tree = ET.fromstring(response.content)

    for currency in tree.findall(".//Currency"):
        currency_code = currency.get("Kod")
        if currency_code == selected_currency:
            banknote_buying = currency.find("BanknoteBuying").text
            banknote_selling = currency.find("BanknoteSelling").text
            result = float(banknote_selling) - float(banknote_buying)
            result_label.config(text=f"Alış: {banknote_buying}\nSatış : {banknote_selling}\nAlış Satış Farkı: {result}")

root = tk.Tk()
root.title("TL Karşılığı Birim Fiyat")

currency_entry = tk.Entry(root)
currency_entry.pack()

currency_entry.bind("<Return>", fetch_rates)

fetch_button = tk.Button(root, text="Dövizin TL karşılık fiyatını getir", command=fetch_rates)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
