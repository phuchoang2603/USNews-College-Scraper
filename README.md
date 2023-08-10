# US News Data Scraper and Merger

## Overview

This Python project aims to scrape relevant data from the US News website, process and clean the obtained data, and finally merge it with an existing common dataset in CSV format. The goal is to create a comprehensive dataset that combines the information from the US News website with the existing data.

## Features

1. **Web Scraping**: The project uses web scraping techniques to extract data from the US News website. It focuses on specific data points of interest, such as university rankings, acceptance rates, and other relevant metrics.

2. **Data Processing and Cleaning**: The scraped data is processed and cleaned to ensure consistency and accuracy. Textual data is standardized, missing values are handled, and any inconsistencies are addressed.

3. **Merge with Common Dataset**: The cleaned US News data is merged with an existing common dataset in CSV format. This allows for the combination of the US News data with other relevant information.

## Getting Started

1. **Prerequisites**: Ensure you have Python installed on your system. You may also need to install necessary Python packages (e.g., `pandas`, `beautifulsoup4`, `requests`, `fuzzywuzzy`) using the provided `requirements.txt` file.

2. **Running the Code**: The main script for the project is `main.py`. This script orchestrates the entire process, including web scraping, data processing, and merging.

3. **Input Data**: The project assumes the existence of an existing common dataset in CSV format. Make sure this dataset is available with the expected structure (e.g., common columns, standard naming) before running the code.

4. **Output Data**: The merged dataset is saved as `4.csv` in the `csv` output directory.

## Usage

1. Modify the web scraping code in `fetch.py` to extract the specific data points you need from the US News website.

2. Adjust the data processing and cleaning steps in `clean.py` as necessary to ensure the data is in the desired format for merging.

3. Run the main script using `python main.py` to execute the entire process.

## Notes

- This project is designed to be a starting point for your specific use case. You may need to customize it further based on the specific data you're interested in and the structure of your existing common dataset.

- Be respectful and mindful of web scraping guidelines and terms of use of the US News website. Ensure that you're scraping data in a responsible and ethical manner.
