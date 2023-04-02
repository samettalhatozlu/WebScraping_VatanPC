from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.vatanbilgisayar.com/masaustu-bilgisayarlar/"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

ws1 = soup.find_all("div", {"class":"product-list product-list--list-page"},limit=20)


count = 1
for div in ws1:
    name = div.find("div", {"class":"product-list__product-name"}).find_all("h3")[0].text
    price = div.find("div", {"class":"product-list__cost"}).find_all("span")[0].text
    print(f"{count}. bilgisayar adı: {name}, fiyatı: {price}")
    count +=1
    with open('database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow(["PC isim: "+ name +" fiyat: "+ price])


