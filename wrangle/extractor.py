import bs4

def allafrica(html):
    'Extracts title, publication, date, authory and content from all_africa html'

    soup = bs4.BeautifulSoup(html,'lxml')
    
    try:
        title = soup.find('title').text 
    except:
        title = ''

    try:
        publication = soup.find(name='div', attrs={"class":"publication"}).text.replace('\n','')
    except:
        publication = 'allafrica'
    
    try:
        date = soup.find(name='div', attrs={"class": "publication-date"}).text
    except:
        data = ''

    try:
        author = soup.find(name='cite', attrs={"class":"byline"}).text
        author = author[3:]
    except IndexError:
        author = soup.find(name='span', attrs={"class":"kindofstory"}).text
    except AttributeError:
        author = ''
        
        
    story_content = '\n '.join([p.text for p in soup.select('p.story-body-text')])
    
    content = {
                'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }

    return content

def panorama(html):
    soup = bs4.BeautifulSoup(html,'lxml')
    inner = soup.find('div', attrs={'class':'news-inner'})
    date = inner.find('span').text
    title = inner.find('h3', attrs={'class':'fb fs26'}).text
    # publication = inner.find('div', attrs={'class':'publications-share'})
    publication = 'panorama'
    story_content = inner.find('p')
    author = ''
    content = {
                'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }
    return content

def maannews(html):
    soup = bs4.BeautifulSoup(html,'lxml')
    inner = soup.find('div', attrs={'class':'MainContentdiv in-print'})
    title = inner.find('h1', attrs={'class':'title'}).text
    date = inner.find('div', attrs={'class':'stamp'}).text
    author = ''
    publication = 'maannews'
    story_content = inner.find('div', attrs={'class':"BodyDiv"}).text
    content = { 'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }
    return content

def alwatanvoice(html):
    soup = bs4.BeautifulSoup(html,'lxml')
    inner = soup.find('div', attrs={'class':'inner-page'})
    title = inner.find('div', attrs={'class':'subtitle'}).text    
    date = soup.find('div', attrs={'class':'publish-date'}).text.replace('\n', '')
    publication = 'alwatanvoice'
    story_content = soup.find(name='div', attrs={'id':'text', 'class':'text'}).text
    author = ''
    content = {
                'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }
    return content

def haqqin(html):
    soup = bs4.BeautifulSoup(html,'lxml')
    inner = soup.find('div', attrs={'class':'article'})
    title = inner.find('h1').text    
    date = soup.find('time', attrs={'class':'datetime'}).text
    author = ''
    main_content = soup.find(name='div', attrs={'class':'article-content'})
    story_content = '\n'.join(p.text for p in main_content.findAll('p'))
    # story_content = main_content.findAll('p')
    publication = 'haqqin'
    content = {
                'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }
    return content

    
def devex(html):
    soup = bs4.BeautifulSoup(html,'lxml')
    inner = soup.find('div', attrs={'itemprop':'articleBody'})
    title = inner.find('div', attrs={'itemscope':'' ,'itemtype':"http://schema.org/NewsArticle"}).text
    date = soup.find('span', attrs={'class':'caption', 'itemprop':'date', 'itemtype':"http://schema.org/NewsArticle" }).text
    publication = 'devex'
    story_content = '\n'.join(p.text for p in inner.findAll('p'))
    author = ', '.join([a.text for a in soup.find('i').findAll('a')])
    content = {
                'title': title,
                'publication': publication,
                'date': date,
                'author': author,
                'story_content' : story_content,
                }
    return content


scraper_directory = {
    'devex': devex,
    'haqqin': haqqin,
    'alwatanvoice': alwatanvoice,
    'maannews': maannews,
    'panorama': panorama,
    'allafrica': allafrica,
} 





