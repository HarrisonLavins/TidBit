import requests
from bs4 import BeautifulSoup

img_size = '' #uncomment to return full-size image
article_URLs = []
img_URLs = []       
article_headlines = []
article_descriptions = []
article_times_updated = []
article_sources = []


response = requests.get('https://news.google.com/search?q='+'sports')
soup = BeautifulSoup(response.text, 'html.parser')

card = soup.main.find('c-wiz').div.div
print("Getting first card on page...")


#Get card figure tag
card_figure = card.find("figure")

img_URL = card_figure.find('img')['src']             #Get URL from webpage
print("Found card picture: ",img_URL)

if (img_URL.find('/attachments') != -1):             #If the returned image URL is a relative path,
    img_URL = img_URL.replace('/attachments', 'https://news.google.com/attachments') #replace it with the absolute path

format_index = img_URL.index("=")                    #Find first index of the default pre-formating string
img_URL = img_URL[0:format_index]+img_size    #Replace the default string with format for our desired size
            
print("Reformatted card picture: ", img_URL)

card_article = card.find("article")
#Follow the acticle URL, and if it is redirected, save only the final destination URL
raw_article_URL = card_article.find("a")['href'].replace('.', 'https://news.google.com')
print("Found article URL: ", raw_article_URL)

response = requests.get(raw_article_URL)
if response.history: #if the response was redirected:
    article_URLs.append(response.url) #Save redirected URL
else:
    print ("Article source URL request was not redirected")
    article_URLs.append(response.url) #Save redirected URL

print("UPDATED article URL: ", article_URLs[0])


 #Collect and store other article data
article_headlines.append(card_article.find('h3').find('a').get_text())
print("Found article headline: ", article_headlines[0])
article_descriptions.append(card_article.find('h3').next_sibling.get_text())
print("Found article description: ", article_descriptions[0])
article_times_updated.append(card_article.find('time').get_text())
print("Found article time: ", article_times_updated[0])
article_sources.append(card_article.find('time').previous_sibling.get_text())
print("Found article source: ", article_sources[0])



