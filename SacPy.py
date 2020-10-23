'''
    https://www.gnu.org/prep/standards/standards.html#Preface
'''

import wget
import os
from urllib.parse import urlparse
import zipfile

'''
    This function downloads zip file from the web  and extracts files to current local directory
    It will delete or store downloaded zip file based on parameter passed
    
    Inputs Required
         url          - String  - zip file from the web
         targetDir    - String  - Download Local Path. 
                                  Default Directory is your current Directory.
    removeSource      - Boolean - Default value is False 

'''
def downloadFromUrl( url, targetDir=".", removeSource=False):

    wget.download(url)
    parseUrl = urlparse(url)
    baseName = os.path.basename(parseUrl.path)
    try:
       with zipfile.ZipFile(baseName, 'r') as zip_ref:
            zip_ref.extractall(targetDir)
    except  (IOError, zipfile.BadZipfile) as e:
            os.remove(baseName)
            print('cannot unzip file')    

    if removeSource:
       os.remove(baseName)
