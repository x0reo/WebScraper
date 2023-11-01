from bs4 import BeautifulSoup
import requests, re

# paste url here
url = "https://www.javatpoint.com/theory-of-automata"
pageToScrape = requests.get(url)

# Some urls to test:
    # https://sourcemaking.com/design_patterns
    # https://www.w3schools.com/html/
    # https://www.javatpoint.com/theory-of-automata

def scrapeWebText():

    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    # html block elements to read
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    headers = [h.get_text() for h in soup.find_all(re.compile('^h[1-6]$'))]

    # Initialize an empty string to store the result
    result_string = ""

    # Iterate through headers and paragraphs and concatenate them
    for header, paragraph in zip(headers, paragraphs):
        result_string += f"{header}\n{paragraph}\n\n"

    # Print the result
    print(result_string)

def scrapeAll():
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    # Elements to exclude
    def is_valid_element(element):
        if element.name == 'a':
            return False
        if element.find_parent('a'):
            return False
        if element.find_parent('div', id=lambda value: value and ('menu' in value or 'footer' in value)):
            return False
        return True

    # Find all headers (h1 to h6), paragraphs, and their parent elements while excluding links and their child elements
    valid_elements = filter(is_valid_element, soup.recursiveChildGenerator())

    # Iterate through the valid elements and print their text
    for element in valid_elements:
        if element.name and element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'li']:
            print(element.text.strip())

def scrapeWebHtml():

    # html and css of the website
    print(pageToScrape.text)

scrapeAll()
# scrapeWebText()
# scrapeWebHtml()
