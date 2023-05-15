import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(res.text, 'html.parser')

posts = soup.select('.athing')
print(posts[0].select('.titleline')[0].select('a')[0].get('href'))
votes = soup.select('.score')

def create_custom_hn(links):
    hn = []
    for ind, post in enumerate(posts):
        post_id = post.get('id')
        link = post.select('.titleline')[0].select('a')[0].get('href')
        if link.startswith('http'):
            pass
        else:
            link = 'https://news.ycombinator.com/'+link

        score = soup.select('#score_'+str(post_id)) 
        if score:
            a = int(score[0].text.replace(' points',''))
            #print(a)
        else:
            a = 0
        if a > 100:
            print(post_id, 'score = ' + str(a), link)

create_custom_hn(posts)