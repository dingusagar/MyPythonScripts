"""
This script is the modified one , due to the change in the attributes of youtube playlist page 
"""



from bs4 import BeautifulSoup
import urllib2
import os
import re

# def retriveName(tag,index):
#     specialChar = ' '
#     extension = '.mp4'
#     nameWithVideId = tag['data-title'] + '-' + tag['data-video-id']

#     nameWithVideId = re.sub('[;|:]', '-', nameWithVideId)
#     if nameWithVideId.startswith('.'):
#         nameWithVideId = nameWithVideId[1:]

#     # Replace / with _
#     nameWithVideId = nameWithVideId.replace("/","_")


#     orginalName = nameWithVideId + extension
#     newName = str(index) + specialChar + nameWithVideId + extension
#     return orginalName,newName



def ChangeSomeChars(name):
	newName = re.sub('[;|:]', '_', name)
	if newName.startswith('.'):
		newName = newName[1:]
	newName = newName.replace("/","_")
	return newName
    



def addExtension(name):
	extension = ".mp4"
	return name+extension


def retriveName2(name,index):
	existingName = ChangeSomeChars(name)
	existingName = addExtension(existingName)
	newName = str(index)+' '+ existingName
	return existingName,newName


def FileNameCorrector(url,dir):
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)

    print soup.title.string

    tdlinks = soup.find_all('span', attrs={'id': 'video-title'})
    


    i = 0
    for l in tdlinks:
    	link = l.text.strip()
        i = i + 1
        orginalName,newName = retriveName2(link,i)

        print "O : " + orginalName
        print "N : " +newName

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


url = "file:///media/dingu/D_Box/newnewTutorials/Dingu/Statistics%20-%20YouTube%20-%20YouTube.html"
dir = "/media/dingu/D_Box/newnewTutorials/Dingu/"

if not dir.endswith('/'):
    dir = dir + '/'

FileNameCorrector(url,dir)






