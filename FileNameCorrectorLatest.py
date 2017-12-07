
"""
Give the directory where the videos files are stored 
and the url of the playlist
 This script scraps the filename one by one from playlist,
finds the closest match file in the given directory,
renames the file in dir by appending the index number.

If the file already has a prefix index , it ignores it 
"""



from bs4 import BeautifulSoup
import urllib2
import os
import re
import difflib

def testIfPrefixIsAlreadyAdded(name):
    """
    This is to test whether number prefix is already there as part of a previous run of the same script
    """
    try:
        val = int(name)
        return True
    except:
        return False

def ScrapDataFromPlaylist(url):
    
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    print soup.title.string
    tdlinks = soup.find_all('span', attrs={'id': 'video-title'})
    return tdlinks

def FileNameCorrector(url,dir):
    
    tdlinks = ScrapDataFromPlaylist(url)
    filenames = os.listdir("/media/dingu/D_Box/newnewTutorials/stat2/")

    i = 0
    for l in tdlinks:
    	orginalName = l.text.strip()
        i = i + 1

        print "\n\n\n"
        print i,"  [ Orinal filename from playlist ] : " + orginalName      

        closestMatches =  difflib.get_close_matches(orginalName,filenames,1,0.85)
        if closestMatches:
            filetoRename = closestMatches.pop()
            print "[ Closest Match found ] : ",filetoRename
            firstWord= filetoRename.split()[0]

            if not testIfPrefixIsAlreadyAdded(firstWord):                
                newName = str(i) + " " +filetoRename
                os.rename(dir+filetoRename,dir+newName)
                print "[ Renamming to ]  : ",newName
            else:
                print "[ Error ]---->> Number prefix already there : ",filetoRename
        else:
            print "[ Error ] ----->>Cannot find a closest match file in the dir"            



def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



# dir - the directory where all the videos are placed
# url is the youtube playlist page where you can find the video titles along with their numbers


url = "file:///media/dingu/D_Box/newnewTutorials/Dingu/Statistics%20-%20YouTube%20-%20YouTube.html"
dir = "/media/dingu/D_Box/newnewTutorials/stat2/"

if not dir.endswith('/'):
    dir = dir + '/'

FileNameCorrector(url,dir)






