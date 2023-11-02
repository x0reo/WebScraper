from bs4 import BeautifulSoup
import requests, html2text

# Paste url here
url = "https://www.javatpoint.com/theory-of-automata"
pageToScrape = requests.get(url)

# Some urls to test:
    # https://sourcemaking.com/design_patterns
    # https://www.w3schools.com/html/
    # https://www.javatpoint.com/theory-of-automata



def scrapeToText():
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(pageToScrape.text, "html.parser")

    def contains_link(element):
        return element.find('a') is not None

    # Elements to exclude
    def is_valid_element(element):
        if element.name == 'a':
            return False
        if element.find_parent('a'):
            return False
        if element.find_parent('nav'):
            return False
        if element.find_parent('div', id=lambda value: value and ('menu' in value or 'footer' in value)):
            return False # Divs with id that includes 'menu' and 'footer'
        return True

    # Find all headers (h1 to h6), paragraphs, and their parent elements while excluding links and their child elements
    valid_elements = filter(is_valid_element, soup.recursiveChildGenerator())
    valid = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'pre', 'li', 'span']

    # Iterate through the valid elements and print their text
    for element in valid_elements:
        if element.name and element.name in valid and not contains_link(element):
            print(element.text.strip())

def scrapeToMarkdown():

    html_content = pageToScrape.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Exclude specific elements (e.g., 'nav', 'a' for links)
    for tag in soup.find_all(['nav', 'a']):
        tag.extract()

    for div in soup.find_all('div', id=lambda value: value and ('menu' in value or 'footer' in value)):
        div.extract()

    # Convert the modified HTML to Markdown using html2text
    markdown_content = html2text.html2text(str(soup))

    # Print the Markdown content
    print(markdown_content)

def scrapeToHtml():
    # Html and css of the website
    print(pageToScrape.text)



# scrapeToText()
scrapeToMarkdown()
# scrapeToHtml()
