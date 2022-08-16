from fileinput import filename
import pandas as pd
import urllib.request

def url_to_jpg(i, url, file_path):
    filename = 'image-{}.jpg'.format(i+670)
    full_path = '{}{}'.format(file_path,filename)
    urllib.request.urlretrieve(url,full_path)
    print('{} saved.'.format(filename))
    return None

FileName = 'urls2.txt'
FilePath = 'images/'

urls = pd.read_csv(FileName, error_bad_lines=False)

for i, url in enumerate(urls.values):
    try:
        url_to_jpg(i,url[0], FilePath)
    except:
        pass
