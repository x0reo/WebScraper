from bs4 import BeautifulSoup
import requests

def scrapeWeb():
    # paste url here
    pageToScrape = requests.get("https://www.w3schools.com/html/")

    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    # html block elements to read
    paragraphs = soup.findAll('p')
    for paragraph in paragraphs:
        print(paragraph.text)

    # html and css of the website
    print(pageToScrape.text)

scrapeWeb()
