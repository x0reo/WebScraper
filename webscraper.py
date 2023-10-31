from bs4 import BeautifulSoup
import requests

def scrapeWeb():
    # pageToScrape = requests.get("https://realpython.github.io/fake-jobs/")
    pageToScrape = requests.get("https://www.w3schools.com/html/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    paragraphs = soup.findAll('p')
    for paragraph in paragraphs:
        print(paragraph.text)

    print(pageToScrape.text)

scrapeWeb()
