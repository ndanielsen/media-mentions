'''
Converts all .doc and .docx to html using LibreOffice

https://ask.libreoffice.org/en/question/50421/how-run-soffice-command-as-python-process/

http://stackoverflow.com/questions/30125574/error-calling-libreoffice-from-python/30125689#30125689
'''
from __future__ import print_function, division
import subprocess
import os
import glob
import logging


### config logging
logging.basicConfig(filename='fileconversion.log',level=logging.DEBUG)


data_files = []


### map all files in the data folder and save to a list
for root, subFolders, files in os.walk('./data'):
    for file in files:
        data_files.append(os.path.join(root,file))


### identifiy all .doc and .docx files
doc_files =  [filename for filename in data_files if filename.endswith(".doc")]
docx_files =  [filename for filename in data_files if filename.endswith(".docx")]
all_files = doc_files + docx_files



### Using libreoffice from cli, convert all .docs to html and log exceptions
for filename in doc_files:
    try:
        subprocess.call(['/Applications/LibreOffice.app/Contents/MacOS/soffice', '--headless', '--convert-to', '"html:XHTML Writer File:UTF8"', '--outdir', 'html', filename])
        # logging.info('File: %s processed', filename)
    except Exception:
        logging.debug('File: %s error', filename)



if __name__ == '__main__':
    print(len(data_files))
    print('Done')
