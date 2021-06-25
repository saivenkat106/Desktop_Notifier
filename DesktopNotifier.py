#Desktop Notifier
import bs4
#from urllib.request import urlopen,Request
from win10toast import ToastNotifier 
import requests
import time
def collectData():
    res=requests.get("https://www.worldometers.info/coronavirus/country/india/")
    s=bs4.BeautifulSoup(res.text,'html.parser')
    cases=s.find('li',class_="news_li").strong.text
    print(cases)
    deaths=list(s.find('li',class_="news_li").strong.next_siblings)[1].text
    print(deaths)
    notif=ToastNotifier()
    message=cases+"\n"+deaths
    notif.show_toast(title='covid-19 ALERT',msg=message,duration=10)
while(True):
    collectData()
    time.sleep(60)

#,icon_path="C:/Users/Venkat/Desktop/covid_virus_coronavirus_infection_disease_flu_corona_illness_icon_140898.ico"
