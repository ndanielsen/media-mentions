"""
Open and extracts data from .docx files.

Converts .doc to .docx

By Nathan Danielsen 
"""
from __future__ import print_function, division

from glob import glob
import StringIO
import zipfile
import subprocess
import os
import sys
import json
import re
# from pydocx import PyDocX
from bs4 import BeautifulSoup

import logging
### config logging
logging.basicConfig(filename='html_extactor.log',level=logging.DEBUG)



data_files = []

for root, subFolders, files in os.walk('./data'):
    for file in files:
        data_files.append(os.path.join(root,file))

doc_files =  [filename for filename in data_files if filename.endswith(".doc")]
docx_files =  [filename for filename in data_files if filename.endswith(".docx")]
html_files  = [f for f in glob('./html/*') if f.endswith('html')]

def docxs_to_list_o_dicts(docx_files):
    headers = []
    rows = []
    for docx in docx_files:
        html = PyDocX.to_html(docx)
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('tr')
        headers.append([col.text for col in data[0]])
        table = list([row.findAll('td') for row in data[1:]])
        for row in table:
            outlet = row[0].text
            headline = row[1].text
            try:
                url = row[1].find('a', href=True)['href']
            except:
                url = ''
            date = row[2].text
            topic = row[3].text
            
            rows.append({'outlet':outlet, 'headline':headline, 'date':date, 'topic':topic, 'url':url, 'docx':docx})
    return rows 

def write_to_json(list_o_dics):
    with open('./data/extracted_stories.json', 'w+') as data_file:
        json.dump(list_o_dics, data_file)

def html_to_list_dicts(html):
    rows = []
    with open(html, 'rU') as html_text:
        soup = BeautifulSoup(html_text, 'html.parser')
        data = soup.find_all('tr')
        table = list([row.findAll('td') for row in data[1:]])
        doc = re.search(r'\/html\/(.*)\.', html).group(1)
        try:
            for row in table:
                outlet = row[0].text
                try:
                    headline = row[1].text
                except Exception, e:
                    headline = ''
                    logging.debug('No headline:  %s', html)
                try:
                    url = row[1].find('a', href=True)['href']
                except:
                    url = ''
                    logging.debug('Headline: %s ---No Url: %s',headline, html)
                date = row[2].text
                topic = row[3].text
                rows.append({'outlet':outlet, 'headline':headline, 'date':date, 'topic':topic, 'url':url, 'docx':doc})    
        except:
            logging.debug('File: %s error, ', html)
    return rows 

if __name__ == '__main__':

    print('Before: ', len(html_files))
    list_o_dict = []
    [list_o_dict.append(rows) for doc in html_files for rows in html_to_list_dicts(doc)]
    # print(list_o_dict)
    write_to_json(list_o_dict)
    print('done:', len(list_o_dict))


