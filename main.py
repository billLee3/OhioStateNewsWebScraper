import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chrome_driver_path = "/home/billlee3/Documents/webdriver/ChromeDriver/chromedriver"
endpoint = "https://www.google.com/search?q=ohio+state+football&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiMxJWFg7PyAhWTKs0KHTKlBd4Q_AUoAXoECAEQAw&biw=1848&bih=949"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "en-GB, en-US; q=0.9, en;q=0.8"
}

response = requests.get(endpoint, headers=header)
ohiostateheadlines = response.text

soup = BeautifulSoup(ohiostateheadlines, "html.parser")
# cards = soup.find_all(name='g-card')
# print(cards)
headlines = soup.find_all('div', {'class':'JheGif nDgy9d'})
# nDgy9d


headline_dict = {}
index = 0
for headline in headlines:
    a = headline.find_previous('a')
    link = a['href']
    headline_text = headline.getText()
    headline_dict[index] = {'headline':headline_text, 'link':link}
    index +=1

# cards = soup.find_all('g-card["a"]["href"]', {'class':'nChh6e DyOREb'})
# print(cards)




# print(news_headlines)
# driver.find_element_by_id
#driver.find_element_by_name


# INTERACTION
# On selected element variable. Variable.send_keys or variable.click()

# driver.quit()