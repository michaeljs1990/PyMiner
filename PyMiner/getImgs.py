import urllib2
import bs4
import setPath
import os

def saveImgs(img, path):
    filename = os.path.basename(img)
    path = path + filename
    try:
        url = urllib2.urlopen(img).read()
    except Exception:
        url = urllib2.urlopen('http:' + img).read()
    fileDownload = open(path, 'w')
    fileDownload.write(url)
    fileDownload.close()
    fileSize = os.path.getsize(path)
    fileSize = fileSize / 1024
    if len(filename) > 20:
        print "[*] Downloading " + filename[0:20] + ' size: ' + str(fileSize) + 'kB'
    else:
        print "[*] Downloading " + filename + ' size: ' + str(fileSize) + 'kB'
    

def getImgs(sourceCode):
    path = setPath.setPath()
    soup = bs4.BeautifulSoup(sourceCode)
    soup = soup.find_all('a', recursive=True, limit=None)
    for img in soup:
        img = img.get('href')
        try:
            if any(ext in img for ext in ['.jpg', '.png', '.gif', '.jpeg']):
                if os.path.isfile(path + os.path.basename(img)) == False:
                    saveImgs(img, path)
        except Exception, e:
            pass #This is used to escape hrefs that have been empty set
