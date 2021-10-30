# ---------------------------------------------------
#  Code for counting external links on awesome lists
# ---------------------------------------------------

import requests
import pandas as pd
from bs4 import BeautifulSoup

def count_external_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    hrefs = [tag.get('href') for tag in soup.find_all(href=True)]
    external = [x for x in set(hrefs) if x.startswith('http')]
    return len(external)
  
snacks = "https://github.com/alonnir/snacks"
awesome_lists = ["https://github.com/briatte/awesome-network-analysis",
                "https://github.com/ChristosChristofidis/awesome-deep-learning",
                "https://github.com/rossant/awesome-math",
                "https://github.com/tayllan/awesome-algorithms",
                "https://github.com/vinta/awesome-python",
                "https://github.com/qinwf/awesome-R",
                "https://github.com/krzjoa/awesome-python-data-science",
                "https://github.com/mikecroucher/awesome-MATLAB",
                "https://github.com/sspkmnd/awesome-sas",
                "https://github.com/sindresorhus/awesome"]


blank_df = pd.DataFrame(columns=['url', 'external_links_count'])

for n,i in enumerate(awesome_lists):
    blank_df.loc[n] = [i, count_external_links(i)]
    
blank_df.sort_values(by="external_links_count", ascending=False, inplace=True)

print(blank_df)
