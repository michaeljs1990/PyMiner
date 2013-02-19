import optparse
import urllib2
import bs4
import os.path

def saveImgs(source):
    filename = os.path.basename(source)
    path = os.path.abspath(filename)
    if len(filename) > 10:
        print "[*] Downloading " + filename[0:10]
    else:
        print "[*] Downloading " + filename
    try:
        url = urllib2.urlopen(source).read()
    except Exception, e:
        url = urllib2.urlopen('http:' + source).read()
    fileDownload = open(path, 'w')
    fileDownload.write(url)
    fileDownload.close()
    

def getImgs(sourceCode):
    soup = bs4.BeautifulSoup(sourceCode)
    soup = soup.body
    soup = soup.find_all('a', recursive=True)
    for img in soup:
        img = img.get('href')
        try:
            if any(ext in img for ext in ['.jpg', '.png', '.gif', '.jpeg']):
                saveImgs(img)
        except Exception, e:
            print e


def getPage(webpage):
    #Grabs source code from page
    url = urllib2.urlopen(webpage)
    data = url.read()
    url.close()
    return data


def main():
    #Command line options parsed with optparse
    usage = 'usage: %prog [options] arg'
    parser = optparse.OptionParser(usage)
    parser.add_option('-w', '--web', dest='webpage', help='webpage that you want data from')
    parser.add_option('-i', '--img', dest='images', help='grabs all images from a webpage')
    (options, args) = parser.parse_args()
    if len(args) != 0 or isinstance(options.webpage, str) != True:
        parser.error('Syntax: -w www.example.com --img [imgName]')
    #more exception handeling to be implimented here
    webpage = options.webpage
    images = options.images
    sourceCode = getPage(webpage)
    getImgs(sourceCode)


if __name__ == "__main__":
    main()
