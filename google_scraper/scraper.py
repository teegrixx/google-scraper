#!/data/data/com.termux/files/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import time

def google_search(query, num_pages=1):
    all_results = []
    retries = 3  # Number of retries
    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}"
        headers = {"User-Agent": "Mozilla/5.0"}
        for attempt in range(retries):
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
                soup = BeautifulSoup(response.text, "html.parser")
                links = soup.find_all("a")
                for link in links:
                    href = link.get("href")
                    if href.startswith("/url?q="):
                        all_results.append(href.split("/url?q=")[1].split("&")[0])
                break  # Exit the retry loop if successful
            except (requests.exceptions.RequestException, urllib3.exceptions.HTTPError) as e:
                print(f"Error fetching page {page + 1}, attempt {attempt + 1}: {e}")
                if attempt < retries - 1:
                    print("Retrying...")
                    time.sleep(2)  # Add a delay before retrying
                else:
                    print("Maximum retries exceeded. Skipping page.")
    return all_results

def save_links_to_file(links, filename):
    with open(filename, "w") as f:
        for link in links:
            f.write(link + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: ./google_scraper.py <search_query> <num_pages>")
        sys.exit(1)

    query = sys.argv[1]
    num_pages = int(sys.argv[2])
    
    results = google_search(query, num_pages)
    output_file = "search_results.txt"
    save_links_to_file(results, output_file)
    print(f"Search results saved to {output_file}")

if __name__ == "__main__":
    main()
