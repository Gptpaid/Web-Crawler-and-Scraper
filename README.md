# Web Crawler and Scraper

## Overview

This project is a simple web crawler and scraper that allows users to input a domain, crawl all internal links, scrape their contents, and export the data into a CSV file.

## How it Works

- Users input a domain URL.
- The program crawls through all internal links within the same domain.
- The text content of each page is scraped and saved.
- Scraped data is exported to a CSV file.

## Setup Instructions

1. Install the required dependencies with `pip install -r requirements.txt`.
2. Run the program using `python main.py`.
3. Enter the domain URL when prompted.
4. The crawler will scrape the content and export it to a `scraped_data.csv` file.

## Deployment

To deploy the project on Replit:
1. Clone this repository on Replit.
2. Use the Replit environment to run the program.

### Dependencies
- `requests`
- `beautifulsoup4`
