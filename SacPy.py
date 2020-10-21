'''
    https://www.gnu.org/prep/standards/standards.html#Preface
'''

'''
    This function downloads zip file from the web  and extracts files to current local directory
    It will delete or store downloaded zip file based on parameter passed
    
    Inputs Required
         url          - String  - zip file from the web
         targetDir    - String  - Download Local Path. 
                                  Default Directory is your current Directory.
    removeSource      - Boolean - Default value is False 

'''

import wget
import os
import zipfile as zip
from urllib.parse import urlparse

def downloadFromUrl( url, targetDir=".", removeSource=False):

    wget.download(url)
    parseUrl = urlparse(url)
    baseName = os.path.basename(parseUrl.path)

    with zip.ZipFile(baseName, 'r') as zip_ref:
         zip_ref.extractall(targetDir)

    if removeSource:
       os.remove(baseName)
