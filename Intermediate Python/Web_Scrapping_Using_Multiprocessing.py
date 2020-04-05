import bs4 as bs
from multiprocessing import Pool
import string
import requests
import random

def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['https://', starting, '.com'])
    return url

def handle_local_links(url, links):
    if link.startswith('/'):
        return ''.join([url, link])
    else :
        return link

def get_links(url):
    try :
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode("ascii")) for link in links]
        return links

    except TypeError as e:
        print(e)
        print("Got a Type Error")
        return []
    except IndexError as e:
        print(e)
        print("Got a Index Error")
        return []
    except AttributeError as e:
        print(e)
        print("Got a Attribute Error")
        return []
    except Exception as e:
        print(e)
        print("Got some Error")
        #log this error
        return []


def main():
    how_many = 50
    p = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = p.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    p.close()

    with open('urls.txt', 'w') as f:
        f.write(str(data))
    

if __name__ == '__main__':
    main()
    
