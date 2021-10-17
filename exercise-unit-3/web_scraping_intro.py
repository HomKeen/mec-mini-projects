from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

my_url = "https://www.newegg.com/p/pl?d=graphics+card"
uclient = ureq(my_url)
page_raw_html = uclient.read()
uclient.close()

page_soup = soup(page_raw_html, "html.parser")
graphics_cards_containers = page_soup.findAll("div", {"class": "item-cell"})

filename = "graphics_cards.csv"
f = open(filename, "w")
f.write("Brand,Product Name,Shipping info\n")

error = 0
for cur_card in graphics_cards_containers:
    try:
        product_name = cur_card.findAll("a", {"class": "item-title"})[0].text
        maker = cur_card.div.div.a.img["title"]
        shipping = cur_card.findAll("li", {"class": "price-ship"})[0].text.strip()
        f.write(f"{maker.replace(',', ',')},{product_name.replace(',', '|')},{shipping.replace(',', '|')}\n")
    except:
        error += 1
        #print("couldn't get: \n", cur_card)
f.close()
print(error, "couldn't be found")
