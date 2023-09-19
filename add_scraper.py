import requests
from bs4 import BeautifulSoup
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS listings_listingmodel (
    title TEXT,
    address TEXT,
    description TEXT,
    image_url TEXT
)
''')

print(cursor)

# Make an HTTP GET request to the Zillow website to retrieve the HTML for the page
URL = "https://www.daft.ie/property-for-rent/monaghan"
page = requests.get(URL)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

# Find all the property listings on the page
listings = soup.find_all(text = "Monaghan")
#listings = soup.find_all("div")
print(listings)


# Iterate through each listing and extract the data
for listing in listings:
    print(listing)
    title = listing.find('h3', class_='list-card-title').text
    address = listing.find('address').text
    description = listing.find('div', class_='list-card-body').text
    image_url = listing.find('img')['src']

    # Insert the data into the SQLite database
    cursor.execute('''
        INSERT INTO listings (title, address, description, photo_main)
        VALUES (?, ?, ?, ?)
    ''', (title, address, description, image_url))

# Commit the changes to the database
conn.commit()

# Close the connection to the database
conn.close()