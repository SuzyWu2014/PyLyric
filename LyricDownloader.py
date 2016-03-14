#---------------------------------------------------------------------------------
#Name:		Lyric Downloader
#Author:	Shujin Wu		
#Description: Search and download lyric for given song 
#---------------------------------------------------------------------------------

import urllib
from bs4 import BeautifulSoup

def azlyrics(song,artist):
	song=song.replace(" ","")
	artist=artist.replace(" ","")
	url='http://www.azlyrics.com/lyrics/'+artist+'/'+song+'.html' 
	htmlText=urllib.urlopen(url).read()
	soup = BeautifulSoup(htmlText,"lxml")
	find_lyrics=soup.find_all("div")
	div = [x for x in find_lyrics if str(x).find("class=") == -1]
	if(len(div)>1): 
		return div[1]
	else:
		return -1


song=raw_input("Enter the correct name of the song:	").strip(" ").lower()
artist=raw_input("Enter the correct name of the artist:	").strip(" ").lower()
lyric=azlyrics(song,artist)
print lyric

	