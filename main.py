import requests
from bs4 import BeautifulSoup
import smtplib
import datetime as dt
import json

MY_EMAIL = '' #Insert Email 
MY_PASSWORD = '' #Insert Password

chrome_driver_path = "/home/billlee3/Documents/webdriver/ChromeDriver/chromedriver"
endpoint = "https://www.google.com/search?q=ohio+state+football&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiMxJWFg7PyAhWTKs0KHTKlBd4Q_AUoAXoECAEQAw&biw=1848&bih=949"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "en-GB, en-US; q=0.9, en;q=0.8"
}

response = requests.get(endpoint, headers=header)
ohiostateheadlines = response.text

soup = BeautifulSoup(ohiostateheadlines, "html.parser")

headlines = soup.find_all('div', {'class':'JheGif nDgy9d'})

headline_dict = {}
index = 0
for headline in headlines:
    a = headline.find_previous('a')
    link = a['href']
    headline_text = headline.getText()
    headline_dict[headline_text] = link
    
json_object = json.dumps(headline_dict, indent=4)

now = dt.datetime.now()
hour = now.hour

if hour == 8:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="" #Insert receipient email,
            msg=f'Subject:OHIO STATE NEWS {now}\n\n{json_object}'
        )

# SET UP CRON TASK AUTOMATION FOR 8AM EVERY MORNING. 
# MOVE PASSWORD AND EMAIL INTO ENV VARIABLES. 
