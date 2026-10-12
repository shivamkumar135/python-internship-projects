import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_quotes():
    print("\n--- Web Scraper for Headlines & Quotes ---")
    url = "http://quotes.toscrape.com/"
    
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch webpage. Status code: {response.status_code}")
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        quote_elements = soup.find_all('div', class_='quote')
        
        scraped_data = []
        
        for elem in quote_elements:
            text = elem.find('span', class_='text').get_text()
            author = elem.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in elem.find_all('a', class_='tag')]
            
            scraped_data.append({
                "quote": text,
                "author": author,
                "tags": tags
            })
            
        print(f"Successfully scraped {len(scraped_data)} quotes!\n")
        
        for i, item in enumerate(scraped_data, 1):
            print(f"{i}. {item['quote']}")
            print(f"   - Author: {item['author']}\n")
            
        filename = "scraped_quotes.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=4)
            
        print(f"Data successfully saved to '{filename}'.")
        
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

def main():
    while True:
        print("\n=== Web Scraper Menu ===")
        print("1. Run Quote Scraper")
        print("2. Exit")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            scrape_quotes()
        elif choice == '2':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()