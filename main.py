from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import requests
import time

google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeeBklGTpr3CI3RZUL7PRonCV6fHZZmTxebar8_LiUrpl3mgA/viewform?usp=publish-editor"

# scrape demo Zillow website with beautifulsoup
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


# scrape property links
a_list = soup.find_all("a")
link_list = []
for a in a_list:
    try:
        if a["data-test"] == "property-card-link":
            if a["href"] in link_list:
                pass
            else:
                link_list.append(a["href"])
    except KeyError:
        pass




# fill google form with property data with selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(google_form_link)


submit_button = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")

for i, j, k in zip(address_list, price_list, link_list):
    time.sleep(5)
    input_fields = driver.find_elements(By.CSS_SELECTOR, value='input[type="text"]')
    print(input_fields)
    try:
        input_fields[0].send_keys(i)
        input_fields[1].send_keys(j)
        input_fields[2].send_keys(k)

        submit_button = driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
        submit_button.click()
    except StaleElementReferenceException, IndexError:
        submit_new_response = driver.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        submit_new_response.click()
        time.sleep(5)




