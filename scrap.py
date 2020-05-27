import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res1 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup1 = BeautifulSoup(res1.text, 'html.parser')

story = soup.select('.storylink')
sub = soup.select('.subtext')
story1 = soup.select('.storylink')
sub1 = soup.select('.subtext')

comb = story + story1
comb1 = sub + sub1

def sort_sty_by_votes(hacklist):
	return sorted(hacklist, key= lambda k:k['votes'], reverse=True)

def create_custom_hacker(story, sub):
	hacker = []
	for indx, item in enumerate(story):
		title = item.getText()
		href = item.get('href', None)
		vote = sub[indx].select('.score')
		if len(vote):
			point = int(vote[0].getText().replace(' points', ''))
			if point > 200:
				hacker.append({'title': title, 'link':href, 'votes': point})
	return sort_sty_by_votes(hacker)

pprint.pprint(create_custom_hacker(comb, comb1))
