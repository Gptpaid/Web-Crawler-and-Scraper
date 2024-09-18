# Web Crawler and Scraper Prototype
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import time

# Function to scrape a URL and get its internal links
def get_internal_links(domain_url, soup):
    internal_links = set()
    for link in soup.find_all('a', href=True):
        url = urljoin(domain_url, link['href'])
        if urlparse(url).netloc == urlparse(domain_url).netloc:  # Internal link
            internal_links.add(url)
    return internal_links

# Function to crawl and scrape a website domain
def crawl_and_scrape(domain_url, max_pages=100, delay=1):
    scraped_data = []
    visited_urls = set()
    urls_to_visit = [domain_url]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    while urls_to_visit and len(visited_urls) < max_pages:
        current_url = urls_to_visit.pop(0)
        if current_url in visited_urls:
            continue
        try:
            print(f'Scraping: {current_url}')
            response = requests.get(current_url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content = soup.get_text(separator=' ', strip=True)
                scraped_data.append({"url": current_url, "content": content})
                internal_links = get_internal_links(domain_url, soup)
                urls_to_visit.extend(internal_links - visited_urls)
            else:
                print(f'Failed to retrieve {current_url}: Status code {response.status_code}')
            visited_urls.add(current_url)
            time.sleep(delay)  # Polite crawling, add delay between requests
        except requests.RequestException as e:
            print(f"Failed to scrape {current_url}: {e}")
    return scraped_data

# Export scraped data to CSV
def export_to_csv(scraped_data, filename):
    if not scraped_data:
        print('No data scraped.')
        return
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in scraped_data:
            writer.writerow(data)

# Main execution
def main():
    domain = input('Enter a domain to crawl and scrape: ')
    if not (domain.startswith('http://') or domain.startswith('https://')):
        print("Invalid URL format. Please enter a URL starting with 'http://' or 'https://'")
        return
    max_pages = int(input('Enter the maximum number of pages to scrape: '))
    delay = float(input('Enter the delay between requests (in seconds): '))
    scraped_data = crawl_and_scrape(domain, max_pages, delay)
    export_to_csv(scraped_data, 'scraped_data.csv')
    print(f'Scraping complete. Data exported to scraped_data.csv')

if __name__ == '__main__':
    main()