import requests # Import the requests library to handle HTTP requests
from bs4 import BeautifulSoup # Import BeautifulSoup from bs4 to parse HTML content

url = 'https://edition.cnn.com/world' # URL of the CNN World section
response = requests.get(url) # Send a GET request to the URL
soup = BeautifulSoup(response.text, 'lxml') # Parse the HTML content using BeautifulSoup

for title in soup.find_all('span', class_='container__headline-text'): # Find all span elements with the specified class
    print(title.text.strip())  # Print the text content of each title, stripping any extra whitespace
    print('---')
