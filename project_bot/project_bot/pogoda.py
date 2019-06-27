
import requests
import bs4

def get_weather(city):
    url = "https://yandex.ru/pogoda/" + city
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content,"lxml")
    return soup
def get_temp(soup):
    result = soup.find("span",{"class":"temp__value"})
    return result.text
def muin(city):
    soup = get_weather(city)
    return get_term(soup)


  

    


    