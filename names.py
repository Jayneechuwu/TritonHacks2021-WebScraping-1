from bs4 import BeautifulSoup
import requests
yelp_search = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Downtown%2C+San+Diego%2C+CA&ns=1"
yelp_html = requests.get(yelp_search).text
print(yelp_html[:300])
soup = BeautifulSoup(yelp_html, "html.parser") # Pass in the HTML text to parser
titles = soup.find_all("a", class_="css-166la90") # Find all "a" elements with this class specific class
# Print them :)
for x in titles:
    print(x['name'])