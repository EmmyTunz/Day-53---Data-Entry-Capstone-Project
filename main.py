from bs4 import BeautifulSoup
import requests
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeeBklGTpr3CI3RZUL7PRonCV6fHZZmTxebar8_LiUrpl3mgA/viewform?usp=publish-editor"


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# find all price data
span_list = soup.find_all("span")
# price_list = [i.text for i in span_list if i["data-test"] == "property-card-price"]
raw_price_list = []
for i in span_list:
    try:
        if i["data-test"] == "property-card-price":
            raw_price_list.append(i.text)
    except KeyError:
        pass


price_list = [i.split("+")[0].split("/")[0] for i in raw_price_list]

# scrape address data
address_list = [i.text.split("\n")[1].split("                                  ")[1] for i in soup.find_all("address")]
print(address_list)

# scrape property links
a_list = soup.find_all("a")
link_list = []
for a in a_list:
    try:
        if a["data-test"] == "property-card-link":
            link_list.append(a["href"])
    except KeyError:
        pass

print(link_list)