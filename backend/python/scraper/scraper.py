# Main scraper file handles:
# -creation and initialization of scraper objects for ALL NEWS CATEGORIES
# -invoking methods to scrape news data and store in database
from GNews import GNewsScraper

# Categories to feed into scraper
categories = [
        'gaming',
        'photography',
        'music',
        'cars',
        'movies'
        'finance',
        'cuisine',
        'fashion',
        'technology',
        'sports'
]

#Scrape each category and store in database
for category in categories:
    scraper = GNewsScraper(category, 1)
    scraper.extract_info()
    #scraper.send_to_firebase()
    scraper.print_to_console()