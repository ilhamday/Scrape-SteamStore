import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template


# initialization flask
app = Flask(__name__)

@app.route('/')
def top_sellers():

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }

    url = 'https://store.steampowered.com/search/?filter=topsellers'

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    steams = soup.findAll('a', attrs={'class':'search_result_row ds_collapse_flag'})

    return render_template('grid_template.html', top_sellers=steams)

if __name__ == '__main__':
    app.run(debug=True)