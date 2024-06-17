import requests
from bs4 import BeautifulSoup

def fetch_headlines():
    url = "https://www.bbc.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.select('h3.gs-c-promo-heading__title')

    return [headline.get_text() for headline in headlines[:10]]  # Fetch top 10 headlines

def display_headlines(headlines):
    if not headlines:
        print("No headlines found.")
        return
    
    print("\nLatest BBC News Headlines:\n")
    for idx, headline in enumerate(headlines, start=1):
        print(f"{idx}. {headline}")

def main():
    print("Fetching the latest news headlines from BBC News...")
    headlines = fetch_headlines()
    display_headlines(headlines)

if __name__ == "__main__":
    main()
