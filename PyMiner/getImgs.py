import urllib2
import bs4
import setPath
import os

def saveImgs(img, path):
    filename = os.path.basename(img)
    path = path + filename
    if os.path.exists(path):
        return
    try:
        url = urllib2.urlopen(img).read()
    except Exception:
        url = urllib2.urlopen('http:' + img).read()
    fileDownload = open(path, 'w')
    fileDownload.write(url)
    fileDownload.close()
    fileSize = os.path.getsize(path)
    fileSize = fileSize / 1024
    if len(filename) > 10:
        print "[*] Downloading " + filename[0:10] + ' size: ' + str(fileSize) + 'kB'
    else:
        print "[*] Downloading " + filename + ' size: ' + str(fileSize) + 'kB'
    

def getImgs(sourceCode):
    path = setPath.setPath()
    soup = bs4.BeautifulSoup(sourceCode)
    soup = soup.find_all('a', recursive=True, limit=None)
    print soup
    return
    for img in soup:
        img = img.get('href')
        try:
            if any(ext in img for ext in ['.jpg', '.png', '.gif', '.jpeg']) and type(img) != None:
                saveImgs(img, path)
        except Exception, e:
            print e
