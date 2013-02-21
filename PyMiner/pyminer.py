import optparse
import urllib2
import getImgs


def getPage(webpage):
    #Grabs source code from page program terminated if url is invalid.
    #Needs a rewrite from urllib2 to python-request lib to do problems
    #with pulling down some pages.
    try:
        if webpage.find('http://') != -1:
            url = urllib2.urlopen(webpage)
        else:
            webpage = 'http://' + webpage
            url = urllib2.urlopen(webpage)
        data = url.read()
        url.close()
        return data
    except Exception:
        print "Problem getting page source. This could be caused by slow server response time or a bad url."


def main():
    #Command line options parsed with optparse
    usage = 'usage: %prog [options] arg'
    parser = optparse.OptionParser(usage)
    parser.add_option('-w', '--web', dest='webpage', help='webpage that you want data from')
    (options, args) = parser.parse_args()
    if len(args) != 0 or isinstance(options.webpage, str) != True:
        parser.error('Syntax: -w www.example.com --img [imgName]')
    #more exception handeling to be implimented here
    webpage = options.webpage
    sourceCode = getPage(webpage)
    getImgs.getImgs(sourceCode)


if __name__ == "__main__":
    main()
