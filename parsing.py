import time
import requests
from bs4 import BeautifulSoup
import csv

file = open("perfumes.csv", mode='w', encoding="utf-8", newline='')
writer = csv.writer(file)
writer.writerow(['page','Title','price'])

page = 1


while page < 3:

    base_url = f"https://www.ebay.com/sch/i.html?_from=R40&_nkw=perfumes&_oac=2&_pgn={page}"
    response = requests.get(base_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    section = soup.find("div", class_="srp-river-results clearfix")
    titles = section.find_all("div", class_="s-item__title")
    prices = section.find_all('span', class_="s-item__price")

    for title,price in zip(titles,prices):

        writer.writerow([page, title.get_text(strip=True), price.get_text(strip=True)])


    page += 1
    time.sleep(3)

file.close()

