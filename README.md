# Plant Database Web Scraper

This project is a web scraper designed to scrape plant data from the www.mein_schoener_garten.de plant database. It allows you to retrieve information about various plants such as their names, categories, and other details.

## Installation

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Install the required dependencies:
    - requests_html


## Usage

To scrape all plants from the mein_schoener_garten.de database, simply run the `msg_scraper.py` file eg from your command line: *python msg_scraper.py*

This will retrieve the links to all plant pages and then parse the plant data for each page. The progress will be displayed in the console.

If you want to scrape plants from a specific category, you can modify the URL in the `get_plant_links` function in the `msg_scraper.py` file. Simply replace the current URL with the URL of the desired category. For example:

```python
# Example: Scrape plants from the "trees" category
url = "https://www.mein_schoener_garten.de/baeume-und-straeucher/"

After modifying the URL, run the msg_scraper.py file to scrape plants from the specified category.


## Output

The script will save the scraped data into a file called 'plants.json' in the same folder.
It is in the JSON format and can easily be loaded into a pandas DataFrame using pd.read_json() method.

