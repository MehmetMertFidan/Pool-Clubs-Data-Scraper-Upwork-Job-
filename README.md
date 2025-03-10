# Pool Clubs Data Scraper (UpworkJob)

## Overview
Pool Clubs Scraper is a web scraping application that collects data on pool clubs from https://www.usms.org/ website for a Upwork job using Selenium. The scraped data is processed and saved into an Excel file.

## Features
- Uses **Selenium** for automated web scraping
- Extracts details such as club names, websites and contact information
- Saves collected data in an **Excel spreadsheet**

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/MehmetMertFidan/Pool-Clubs-Data-Scraper-Upwork-Job-.git
   ```

## Usage
1. Run the scraper script:
   ```bash
   python main.py
   ```
2. The script uses Selenium to automate web browsing, simulating human actions like clicking and scrolling to gather pool club details.
3. It runs in headless mode, meaning no visible browser window will appear while the script is running.
4. Extracted data will be saved as an Excel file (`clubs.xlsx`).


