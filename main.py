from bs4 import BeautifulSoup
import requests
google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeeBklGTpr3CI3RZUL7PRonCV6fHZZmTxebar8_LiUrpl3mgA/viewform?usp=publish-editor"


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# find all price data
span_list = soup.find_all("span")
# price_list = [i.text for i in span_list if i["data-test"] == "property-card-price"]
price_list = []
for i in span_list:
    try:
        if i["data-test"] == "property-card-price":
            price_list.append(i.text)
    except KeyError:
        pass

print(price_list)

