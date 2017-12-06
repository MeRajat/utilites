# create folder !mkdir clinical_data

import re
import pandas as pd
from bs4 import BeautifulSoup
import requests

regex = re.compile('[^0-9a-zA-Z]')

data = pd.read_csv('SearchResults.csv', header=0)
folder = 'clinical_data/'
def process_text(text):
    text = regex.sub(' ', text)
    text = re.sub(' +',' ', text)
    return text

def write_text(seq):
    url = seq[7]
    fname = url.split('/')[-1]
    r  = requests.get(url)
    data = r.text
    cleantext = BeautifulSoup(data).text
    text = process_text(cleantext)
    with open(f'{folder}{fname}.txt', 'w') as f:
        f.write(text)
       
data.apply(write_text, axis=1)
