# Web Scraper Tool

## What it does

This tool scrapes the latest headline from CNN World news (https://edition.cnn.com/world) and prints them to the console

## How to use

1. **Install dependencies**
    ```
    python -m pip install requests beautifulsoup4 lxml
    ```

2. **Run the scraper**
    ```
    python scraper.py
    ```

## How it works

- Fetches the HTML content of the CNN World page
- Parses the page using BeautifulSoup
- Extracts and prints the text of each headline found in specific HTML elements

## Requirements

- Python 3.6 and above
- `requests`
- `beautifulsoup4`
- `lxml`
