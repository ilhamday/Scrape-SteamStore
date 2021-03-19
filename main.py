import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('steamstore_chace')

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
}

url = 'https://store.steampowered.com/search/?filter=topsellers'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# Check if get the data from cache
print(f"Used Cache: {res.from_cache}")

steams = soup.findAll('a', attrs={'class':'search_result_row ds_collapse_flag'})

titles = []
for s in steams:
    print('---')
    title = s.find('span', attrs={'class': 'title'}).text

    # Get span element
    platform_list = []
    platform = s.find('p').findAll('span')

    # Loop through span
    for pl in platform:
        # if attribute class has more than 1 value, get the last one
        if len(pl.attrs['class']) > 1:
            p = pl.attrs['class'][1]
        else:
            p = pl.attrs['class'][0]
        
        platform_list.append(p)

    price = s.find('div', attrs={'class': 'search_price'}).text
    img_link = s.find('img').attrs
    img_link = img_link['src']
   
    print(f'{title} -- {price} -- {img_link} -- {platform_list}')