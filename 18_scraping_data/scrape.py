import requests
from bs4 import BeautifulSoup
import pprint
from time import sleep

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k["votes"], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):

        title = links[idx].getText()
        href = links[idx].get('href', None) # 2nd parameter is default
        vote = subtext[idx].select('.score')
        
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})

    return hn



master_list = []
page_rng = range(1, 5)

for page in page_rng:
    url_path = "https://news.ycombinator.com/news?p=" + str(page)
    res = requests.get(url_path)
    soup = BeautifulSoup(res.text, 'html.parser')

    # dot (.) signifies a class.
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    master_list = master_list + create_custom_hn(links, subtext)

    sleep(3)

pprint.pprint(sorted(master_list, key= lambda k: k["votes"], reverse=True))