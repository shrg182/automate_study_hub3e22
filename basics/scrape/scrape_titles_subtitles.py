#!/usr/bin/env python3
# Filename: scrape_titles_subtitles.py

"""
A Python script to scrape the title and subtitles from one or more webpages, 
save the results as JSON, and convert them to CSV.

Usage:
    python scrape_titles_subtitles.py <url1> <url2> ... [--output-json <filename>] [--output-csv <filename>]

Example:
    python scrape_titles_subtitles.py https://automatetheboringstuff.com/2e/chapter11/
"""

import argparse
import logging
import requests
from bs4 import BeautifulSoup
import json
import csv
from typing import Dict, List, Optional
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

def scrape_titles_and_subtitles(url: str) -> Optional[Dict[str, any]]:
    """
    Scrape the main title and subtitles from a webpage.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing the main title and a list of subtitles, or None if an error occurs.
    """
    try:
        # Send a GET request to the URL with a timeout
        headers = {'User-Agent': 'Mozilla/5.0 (compatible; WebScraper/1.0)'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Scrape the main title (from <title> tag)
        main_title = soup.title.string.strip() if soup.title else "No Title Found"

        # Scrape subtitles (from <h1> to <h6> tags)
        subtitles = [
            tag.get_text(strip=True) for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if tag.get_text(strip=True)  # Filter out empty tags
        ]

        # Prepare the result
        result = {
            "url": url,
            "main_title": main_title,
            "subtitles": subtitles
        }

        logging.info(f"Successfully scraped {len(subtitles)} subtitles from {url}")
        return result

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while scraping {url}: {e}")
        return None

def save_to_json(data: List[Dict[str, any]], json_filename: str) -> bool:
    """
    Save scraped data to a JSON file.

    Args:
        data (list): List of dictionaries containing scraped data.
        json_filename (str): The name of the JSON file to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        logging.info(f"Scraped data saved to '{json_filename}'")
        return True
    except Exception as e:
        logging.error(f"Error saving JSON to '{json_filename}': {e}")
        return False

def convert_json_to_csv(json_filename: str, csv_filename: str) -> bool:
    """
    Convert JSON data to CSV format.

    Args:
        json_filename (str): The name of the JSON file to read.
        csv_filename (str): The name of the CSV file to save.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            # Write header
            writer.writerow(["URL", "Type", "Content"])

            # Handle both single dict and list of dicts
            data_list = data if isinstance(data, list) else [data]
            for item in data_list:
                # Write main title
                writer.writerow([item.get("url", ""), "Main Title", item.get("main_title", "")])
                # Write subtitles
                for subtitle in item.get("subtitles", []):
                    writer.writerow([item.get("url", ""), "Subtitle", subtitle])

        logging.info(f"JSON data converted to CSV and saved to '{csv_filename}'")
        return True
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from '{json_filename}': {e}")
        return False
    except Exception as e:
        logging.error(f"Error converting JSON to CSV: {e}")
        return False

def main():
    """Main function to handle command-line arguments and orchestrate scraping."""
    parser = argparse.ArgumentParser(
        description="Scrape titles and subtitles from webpages and save to JSON and CSV."
    )
    parser.add_argument(
        "urls",
        nargs='+',
        help="One or more URLs to scrape"
    )
    parser.add_argument(
        "--output-json",
        default="titles_and_subtitles.json",
        help="Output JSON filename (default: titles_and_subtitles.json)"
    )
    parser.add_argument(
        "--output-csv",
        default="titles_and_subtitles.csv",
        help="Output CSV filename (default: titles_and_subtitles.csv)"
    )
    args = parser.parse_args()

    # Scrape each URL
    results = []
    for url in args.urls:
        result = scrape_titles_and_subtitles(url)
        if result:
            results.append(result)

    if not results:
        logging.error("No data was scraped from any provided URLs.")
        return

    # Save to JSON
    if save_to_json(results, args.output_json):
        # Convert JSON to CSV
        convert_json_to_csv(args.output_json, args.output_csv)

if __name__ == "__main__":
    main()