import json

from requests_html import HTMLSession

s = HTMLSession()

def get_plant_links(page_no):
    """
    Retrieves the links to plant pages from a specific page number.

    Args:
        page_no (int): The page number (as shown in the pagination links in the browser) from which to retrieve the plant links.

    Returns:
        list: A list of strings containing the links to the plant pages.
    """

    url = f'https://www.mein-schoener-garten.de/pflanzen?page={page_no-1}'
    links = []
    r = s.get(url)

    # identify the listed plants via css tags
    plants = r.html.find('div.caption.caption-teaser h3')

    # extract the links to the respective plant's page
    for plant in plants:
        links.append(plant.find('a', first=True).attrs['href'])

    return links


def parse_plants(url):
    """
    Parses the plants data from the given URL and returns a dictionary with plant facts.
    Parameters:
        url (str): The URL of the website containing the plants data.
    Returns:
        dict: A dictionary containing the plant facts, where the keys are the categories and the values are the corresponding items.
    """

    r = s.get(url)

    # get the name
    name = r.html.find('h1.h2.text-headline', first=True).text.strip()

    # find the wrapper for the plant facts table
    plant_facts_raw = r.html.find('div.plant-facts__item--wrapper')

    # initialize the plant's dictionary with the name
    plant_facts = {'Name': name}

    # parse the plant facts and store them in the dictionary
    for fact in plant_facts_raw:
        cat = fact.find('dt', first=True).text.strip()

        items = fact.find('dd', first=True).text.strip().replace('\n', ', ')

        plant_facts[cat] = items

    return plant_facts

# set the parameters for scraping
page = 1
dicts = []

# get the first set of plant links
urls = get_plant_links(page)

# continue until no more plant links are retrieved (aka. page number out of scope)
while urls:
    print(f'Parsing page {page}')
    new_dicts = [parse_plants(u) for u in urls]
    dicts = dicts + new_dicts

    page += 1
    urls = get_plant_links(page)
    print(f'{len(dicts)} plants collected so far')

#save the data to a json file for further processing
with open('plants.json', 'w') as outfile:
    json.dump(dicts, outfile)
print(f'No more pages to parse. {len(dicts)} plants collected and saved to plants.json.')