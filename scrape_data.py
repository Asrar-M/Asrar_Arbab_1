import requests

def getRawHTML(url):
    r = requests.get(url)
    return r.text

print(getRawHTML('https://www.sofascore.com/tournament/football/england/premier-league/17#id:61627'))