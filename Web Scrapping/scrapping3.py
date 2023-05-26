from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

links = soup.select('.titleline > a')
votes = soup.select('.subtext')
links2 = soup.select('.titleline > a')
votes2 = soup.select('.subtext')
# print(votes[0])
# print(links[0])
megalink = links + links2
megavotes = votes + votes2

def create_costum_hn(links,votes):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        vote = votes[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            # print(points)
            if points < 99:
                hn.append({'title':title,'link':href,'votes':points})
    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key= lambda k:k['votes'],reverse=True)

pprint.pprint(create_costum_hn(megalink,megavotes))
