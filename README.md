# MyPythonScripts
Brand new time saver scripts written in python


<B>FileNameCorrector.py</b><br>
you downloaded a playlist from youtube. But later when you try to watch it offline, you see that the videos are all jumbled up 
due to file names. I faced this problem when I downloaded a playlist using youtube-dl. Even though youtube-dl provides you an 
option to name the downloaded files according to your choice, many of us forget to do so (or unaware of this option).
Once you are done with downloading  you got no choice but to manually 
search and find the video in the chronological order.

This simple python script accepts the directory of your downloaded videos and the html page of your youtube playlist.
It will scrap the html page, extract the video names in the right order and rename the videos in your directory so that you have your videos in the 
same order as in the playlist.

for eg:
the script replaces a video named "Machine Learning - Linear Regression" to "1 Machine Learning - Linear Regression" so that this video appears first in your directory. 


<b>How it works</b>
Give the directory where the videos files are stored 
and the url of the playlist
 This script scraps the filename one by one from playlist,
finds the closest match file in the given directory,
renames the file in dir by appending the index number.
If the file already has a prefix index , it ignores it 

#### photOrganizer.py
Simply organises your photos and videos into folders according to creating date
