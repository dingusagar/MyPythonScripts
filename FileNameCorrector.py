from bs4 import BeautifulSoup
import urllib2
import os
import re

def retriveName(tag,index):
    specialChar = ' '
    extension = '.mp4'
    nameWithVideId = tag['data-title'] + '-' + tag['data-video-id']

    nameWithVideId = re.sub('[;|:]', '-', nameWithVideId)
    if nameWithVideId.startswith('.'):
        nameWithVideId = nameWithVideId[1:]

    # Replace / with _
    nameWithVideId = nameWithVideId.replace("/","_")


    orginalName = nameWithVideId + extension
    newName = str(index) + specialChar + nameWithVideId + extension
    return orginalName,newName


def FileNameCorrector(url,dir):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)

    print soup.title.string

    tdlinks = soup.find_all('tr', attrs={'class': 'pl-video yt-uix-tile '})

    i = 0
    for link in tdlinks:
        i = i + 1
        orginalName,newName = retriveName(link,i)

        if find(newName,dir):
            print "Renamed File Already Exists"
            continue


        if  find(orginalName,dir):
            os.rename(dir+orginalName,dir+newName)
            print "Renaming file to ",newName
            # print "orginal name :",orginalName
            g=5
        else:
            print "------------------> File not found : ",orginalName,"----> Number : ",i


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



# dir - the directory where all the videos are placed
# url is the youtube playlist page where you can find the video titles along with their numbers


url = "file:///media/dingu/D_Box/latest%20tutorials/machine%20learning%20with%20python/Machine%20Learning%20with%20Python%20-%20YouTube.html"
dir = "/media/dingu/D_Box/latest tutorials/machine learning with python/"

if not dir.endswith('/'):
    dir = dir + '/'

FileNameCorrector(url,dir)






